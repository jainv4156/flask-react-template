from flask import Blueprint

from modules.comments.rest_api.comments_view import CommentsView


class CommentsRouter:
    comments_BY_ID_URL = "<account_id>/comments/<comment_id>"

    @staticmethod
    def create_route(*, blueprint: Blueprint) -> Blueprint:

        blueprint.add_url_rule("/comments", view_func=CommentsView.as_view("comments_view"))

        blueprint.add_url_rule(
            CommentsRouter.comments_BY_ID_URL, view_func=CommentsView.as_view("comment_view_by_id"), methods=["GET"]
        )
        blueprint.add_url_rule(
            CommentsRouter.comments_BY_ID_URL, view_func=CommentsView.as_view("comment_update"), methods=["PATCH"]
        )
        blueprint.add_url_rule(
            CommentsRouter.comments_BY_ID_URL, view_func=CommentsView.as_view("comment_delete"), methods=["DELETE"]
        )
        return blueprint
