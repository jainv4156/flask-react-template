from modules.comments.internal.comments_reader import CommentReader
from modules.comments.internal.comments_writer import CommentWriter
from modules.comments.types import (
    Comment,
    CommentSearchByCommentIdParams,
    CreateCommentsParams,
    DeleteCommentParams,
    UpdateCommentParams,
)


class CommentsService:
    @staticmethod
    def add_comments(*, params: CreateCommentsParams) -> Comment:
        comment = CommentWriter.create_comment(params=params)
        return comment

    @staticmethod
    def get_comment_by_id(*, comment_id: str) -> Comment:
        get_comment_params = CommentSearchByCommentIdParams(comment_id=comment_id)
        return CommentReader.get_comments_by_id(params=get_comment_params)

    @staticmethod
    def delete_comment_by_id(*, params: DeleteCommentParams) -> None:
        return CommentWriter.delete_comment(params=params)

    @staticmethod
    def update_comment(*, params: UpdateCommentParams) -> Comment:
        return CommentWriter.update_comment(params=params)
