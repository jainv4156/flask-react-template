from datetime import datetime

from bson.objectid import ObjectId
from pymongo import ReturnDocument

from modules.comments.errors import CommentNotFoundError
from modules.comments.internal.comments_utils import CommentsUtil
from modules.comments.internal.store.comments_model import CommentsModel
from modules.comments.internal.store.comments_repository import CommentsRepository
from modules.comments.types import (
    Comment,
    CommentDeletionResult,
    CreateCommentsParams,
    DeleteCommentParams,
    UpdateCommentParams,
)


class CommentWriter:
    @staticmethod
    def create_comment(*, params: CreateCommentsParams) -> Comment:
        comment_bson = CommentsModel(
            comment_content=params.comment_content, task_id=params.task_id, account_id=params.account_id
        ).to_bson()

        query = CommentsRepository.collection().insert_one(comment_bson)
        created_comment_bson = CommentsRepository.collection().find_one({"_id": query.inserted_id})

        return CommentsUtil.convert_comment_bson_to_comment(created_comment_bson)

    @staticmethod
    def delete_comment(*, params: DeleteCommentParams) -> None:
        comment_bson = CommentsRepository.collection().find_one_and_delete(
            {"_id": ObjectId(params.comment_id), "account_id": params.account_id}
        )
        if comment_bson is None:
            raise CommentNotFoundError(comment_id=params.comment_id)
        return CommentDeletionResult(comment_id=params.comment_id, deleted_at=datetime.now(), success=True)

    @staticmethod
    def update_comment(*, params: UpdateCommentParams) -> Comment:
        updated_comment_bson = CommentsRepository.collection().find_one_and_update(
            {"_id": ObjectId(params.comment_id), "account_id": params.account_id},
            {"$set": {"comment_content": params.comment_content, "updated_at": datetime.now()}},
            return_document=ReturnDocument.AFTER,
        )

        if updated_comment_bson is None:
            raise CommentNotFoundError(comment_id=params.comment_id)

        return CommentsUtil.convert_comment_bson_to_comment(updated_comment_bson)
