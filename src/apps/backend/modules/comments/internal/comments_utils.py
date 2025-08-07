from typing import Any

from modules.comments.internal.store.comments_model import CommentsModel
from modules.comments.types import Comment


class CommentsUtil:
    @staticmethod
    def convert_comment_bson_to_comment(comment_bson: dict[str, Any]) -> Comment:
        validated_comment_data = CommentsModel.from_bson(comment_bson)
        return Comment(
            comment_content=validated_comment_data.comment_content,
            task_id=validated_comment_data.task_id,
            account_id=validated_comment_data.account_id,
            created_at=validated_comment_data.created_at,
            updated_at=validated_comment_data.updated_at,
        )
