from bson.objectid import ObjectId

from modules.comments.errors import CommentNotFoundError
from modules.comments.internal.comments_utils import CommentsUtil
from modules.comments.internal.store.comments_repository import CommentsRepository
from modules.comments.types import Comment, GetCommentParams


class CommentReader:
    @staticmethod
    def get_comments_by_id(*, params: GetCommentParams) -> Comment:
        comment_bson = CommentsRepository.collection().find_one({"_id": ObjectId(params.comment_id)})
        if comment_bson is None:
            raise CommentNotFoundError(comment_id=params.comment_id)
        return CommentsUtil.convert_comment_bson_to_comment(comment_bson)
