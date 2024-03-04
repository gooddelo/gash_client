from typing import List, TypeVar, Generic

from pydantic import Field

from gash_client.core.base.dto import DTO, PropertiesDTO


ScopePropertiesDTOType = TypeVar("ScopePropertiesDTOType", bound=PropertiesDTO)
ResourcePropertiesDTOType = TypeVar("ResourcePropertiesDTOType", bound=PropertiesDTO)


class UserCreateDTO(DTO, Generic[ScopePropertiesDTOType, ResourcePropertiesDTOType]):
    id_: str
    role: str
    resources: List[ResourcePropertiesDTOType] = Field(default_factory=list)
    belong_scopes: List[ScopePropertiesDTOType] = Field(default_factory=list)


class UserUpdateDTO(DTO, Generic[ScopePropertiesDTOType, ResourcePropertiesDTOType]):
    id_: str
    old_role: str
    new_role: str | None = None
    new_resources: List[ResourcePropertiesDTOType] | None = None
    new_belong_scopes: List[ScopePropertiesDTOType] | None = None


class UserPropertiesDTO(PropertiesDTO):
    attr: str = Field(alias="role")

    @property
    def role(self):
        return self.attr
