from pymongo.collection import Collection
from pymongo.errors import OperationFailure

from modules.application.repository import ApplicationRepository
from modules.comments.internal.store.comments_model import CommentsModel
from modules.logger.logger import Logger

COMMENTS_VALIDATION_SCHEMA = {
    "$jsonSchema": {"bsonType": "object", "required": ["account_id", "comment_content", "created_at", "updated_at"]}
}


class CommentsRepository(ApplicationRepository):
    collection_name = CommentsModel.get_collection_name()

    @classmethod
    def on_init_collection(cls, collection: Collection) -> bool:
        add_validation_command = {
            "collMod": cls.collection_name,
            "validator": COMMENTS_VALIDATION_SCHEMA,
            "validationLevel": "strict",
        }
        try:
            collection.database.command(add_validation_command)
        except OperationFailure as e:
            if e.code == 26:  # NamespaceNotFound MongoDB error code
                collection.database.create_collection(cls.collection_name, validator=COMMENTS_VALIDATION_SCHEMA)
            else:
                Logger.error(message=f"OperationFailure occurred for collection Comments: {e.details}")
        return True
