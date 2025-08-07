from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class CreateCommentsParams:
    comment_content: str
    task_id: str
    account_id: str


@dataclass(frozen=True)
class CommentSearchByCommentIdParams:
    comment_id: str


@dataclass(frozen=True)
class DeleteCommentParams:
    account_id: str
    comment_id: str


@dataclass(frozen=True)
class UpdateCommentParams:
    account_id: str
    comment_id: str
    comment_content: str


@dataclass(frozen=True)
class CommentDeletionResult:
    comment_id: str
    deleted_at: datetime
    success: bool


@dataclass(frozen=True)
class Comment:
    comment_content: str
    task_id: str
    account_id: str
    created_at: str
    updated_at: str


@dataclass(frozen=True)
class GetCommentParams:
    account_id: str
    comment_id: str


@dataclass(frozen=True)
class CommentErrorCode:
    NOT_FOUND: str = "COMMENT_ERR_01"
    BAD_REQUEST: str = "COMMENT_ERR_02"
