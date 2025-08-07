from dataclasses import asdict
from typing import Optional

from flask import jsonify, request
from flask.typing import ResponseReturnValue
from flask.views import MethodView

from modules.authentication.rest_api.access_auth_middleware import access_auth_middleware
from modules.comments.comment_service import CommentsService
from modules.comments.types import Comment, CreateCommentsParams, DeleteCommentParams, UpdateCommentParams


class CommentsView(MethodView):

    @access_auth_middleware
    def post(self) -> ResponseReturnValue:
        request_data = request.get_json()
        comments_params: CreateCommentsParams
        comment: Comment

        if "comment_content" in request_data and "task_id" in request_data and "account_id" in request_data:
            comments_params = CreateCommentsParams(**request_data)
            comment = CommentsService.add_comments(params=comments_params)
        comment_dict = asdict(comment)
        return jsonify(comment_dict), 201

    @access_auth_middleware
    def get(self, account_id: str, comment_id: Optional[str] = None) -> ResponseReturnValue:
        comments = CommentsService.get_comment_by_id(comment_id=comment_id)
        comments_dict = asdict(comments)
        return jsonify(comments_dict), 200

    @access_auth_middleware
    def delete(self, account_id: str, comment_id: str) -> ResponseReturnValue:
        comment_params = DeleteCommentParams(account_id=account_id, comment_id=comment_id)
        # Assuming a delete method exists in CommentsService
        CommentsService.delete_comment_by_id(params=comment_params)
        return "", 204

    @access_auth_middleware
    def patch(self, account_id: str, comment_id: str) -> ResponseReturnValue:
        request_data = request.get_json()

        update_comment_params = UpdateCommentParams(account_id=account_id, comment_id=comment_id, **request_data)
        updated_comment = CommentsService.update_comment(params=update_comment_params)
        comment_dict = asdict(updated_comment)

        return jsonify(comment_dict), 200
