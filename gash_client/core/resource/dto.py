from typing import List, TypeVar, Generic

from pydantic import Field

from gash_client.core.base.dto import PropertiesDTO, DTO


UserPropertiesDTOType = TypeVar("UserPropertiesDTOType", bound=PropertiesDTO)
ScopePropertiesDTOType = TypeVar("ScopePropertiesDTOType", bound=PropertiesDTO)


class ResourceCreateDTO(DTO, Generic[UserPropertiesDTOType, ScopePropertiesDTOType]):
    id_: str
    type: str
    users: List[UserPropertiesDTOType] = Field(default_factory=list)
    scopes: List[ScopePropertiesDTOType] = Field(default_factory=list)


class ResourceUpdateDTO(DTO, Generic[UserPropertiesDTOType, ScopePropertiesDTOType]):
    id_: str
    old_type: str
    new_type: str | None = None
    new_users: List[UserPropertiesDTOType] | None = None
    new_scopes: List[ScopePropertiesDTOType] | None = None


class ResourcePropertiesDTO(PropertiesDTO):
    attr: str = Field(alias="type")

    @property
    def type(self) -> str:
        return self.attr
