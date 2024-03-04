from typing import List, TypeVar, Generic

from pydantic import Field

from gash_client.core.base.dto import PropertiesDTO, DTO


UserPropertiesDTOType = TypeVar("UserPropertiesDTOType", bound=PropertiesDTO)
ResourcePropertiesDTOType = TypeVar("ResourcePropertiesDTOType", bound=PropertiesDTO)


class ScopePropertiesDTO(PropertiesDTO):
    attr: str = Field(alias="name")

    @property
    def name(self) -> str:
        return self.attr


class ScopeCreateDTO(DTO, Generic[UserPropertiesDTOType, ResourcePropertiesDTOType]):
    id_: str
    name: str
    owner: UserPropertiesDTOType
    users: List[UserPropertiesDTOType] = Field(default_factory=list)
    scopes: List[ScopePropertiesDTO] = Field(default_factory=list)
    resources: List[ResourcePropertiesDTOType] = Field(default_factory=list)


class ScopeUpdateDTO(DTO, Generic[UserPropertiesDTOType, ResourcePropertiesDTOType]):
    id_: str
    old_name: str
    new_name: str | None = None
    new_owner: UserPropertiesDTOType | None = None
    new_users: List[UserPropertiesDTOType] | None = None
    new_scopes: List[ScopePropertiesDTO] | None = None
    new_resources: List[ResourcePropertiesDTOType] | None = None