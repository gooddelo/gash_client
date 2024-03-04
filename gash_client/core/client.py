from faststream.rabbit import RabbitBroker

from gash_client.config import UserQueuesV1, GASH_EXCHANGE, ResourceQueuesV1, ScopeQueuesV1, PermitQueuesV1
from gash_client.core.permit.dto import PermitRequestDTO
from gash_client.core.resource.dto import ResourceCreateDTO, ResourceUpdateDTO, ResourcePropertiesDTO
from gash_client.core.scope.dto import ScopeCreateDTO, ScopeUpdateDTO, ScopePropertiesDTO
from gash_client.core.user.dto import UserCreateDTO, UserPropertiesDTO, UserUpdateDTO


class GashClient:
    __slots__ = ('broker',)

    def __init__(self, broker: RabbitBroker):
        self.broker = broker
    
    async def user_create(self, message: UserCreateDTO):
        await self.broker.publish(message, UserQueuesV1.CREATE, GASH_EXCHANGE)

    async def user_update(self, message: UserUpdateDTO):
        await self.broker.publish(message, UserQueuesV1.UPDATE, GASH_EXCHANGE)
        
    async def user_delete(self, message: UserPropertiesDTO):
        await self.broker.publish(message, UserQueuesV1.DELETE, GASH_EXCHANGE)
    
    async def resource_create(self, message: ResourceCreateDTO):
        await self.broker.publish(message, ResourceQueuesV1.CREATE, GASH_EXCHANGE)

    async def resource_update(self, message: ResourceUpdateDTO):
        await self.broker.publish(message, ResourceQueuesV1.UPDATE, GASH_EXCHANGE)
        
    async def resource_delete(self, message: ResourcePropertiesDTO):
        await self.broker.publish(message, ResourceQueuesV1.DELETE, GASH_EXCHANGE)
    
    async def scope_create(self, message: ScopeCreateDTO):
        await self.broker.publish(message, ScopeQueuesV1.CREATE, GASH_EXCHANGE)

    async def scope_update(self, message: ScopeUpdateDTO):
        await self.broker.publish(message, ScopeQueuesV1.UPDATE, GASH_EXCHANGE)
        
    async def scope_delete(self, message: ScopePropertiesDTO):
        await self.broker.publish(message, ScopeQueuesV1.DELETE, GASH_EXCHANGE)

    async def permit_get(self, message: PermitRequestDTO) -> bool:
        return await self.broker.publish(message, PermitQueuesV1.GET, GASH_EXCHANGE, rpc=True)
