from flask import Blueprint

from modules.comments.rest_api.comments_router import CommentsRouter


class CommentsRestApiServer:
    @staticmethod
    def create() -> Blueprint:
        comments_api_blueprint = Blueprint("comments", __name__)
        return CommentsRouter.create_route(blueprint=comments_api_blueprint)
