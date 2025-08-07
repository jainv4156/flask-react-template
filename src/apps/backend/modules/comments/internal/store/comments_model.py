from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from modules.application.base_model import BaseModel


@dataclass
class CommentsModel(BaseModel):
    comment_content: str
    task_id: str
    account_id: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    @classmethod
    def from_bson(cls, bson_data: dict) -> "CommentsModel":
        return cls(
            comment_content=str(bson_data.get("comment_content", "")),
            task_id=str(bson_data.get("task_id", "")),
            account_id=str(bson_data.get("account_id", "")),
            created_at=bson_data.get("created_at"),
            updated_at=bson_data.get("updated_at"),
        )

    @staticmethod
    def get_collection_name() -> str:
        return "comments"
