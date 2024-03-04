from gash_client.core.base.dto import DTO
from gash_client.core.resource.dto import ResourcePropertiesDTO
from gash_client.core.scope.dto import ScopePropertiesDTO
from gash_client.core.user.dto import UserPropertiesDTO


class PermitRequestDTO(DTO):
    subject: UserPropertiesDTO
    object: ResourcePropertiesDTO | ScopePropertiesDTO | UserPropertiesDTO
    action: str
