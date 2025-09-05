from enum import Enum


class ContentPermissionType(Enum):
    """Permission types related to content"""

    READ_ARTICLE = "READ_ARTICLE"
    UPDATE_ARTICLE = "UPDATE_ARTICLE"
    DELETE_ARTICLE = "DELETE_ARTICLE"
