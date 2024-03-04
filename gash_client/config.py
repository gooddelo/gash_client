from faststream.rabbit import RabbitExchange, RabbitQueue
from faststream.rabbit.shared.utils import build_url
from pydantic_settings import BaseSettings
from yarl import URL


class AMQPConfig(BaseSettings):
    host: str = 'localhost'
    port: int = '5672'
    default_user: str = 'admin'
    default_pass: str = 'password'
    vhost: str = '/'

    def connection_url(self) -> URL:
        return build_url(
            host=self.host, port=self.port, login=self.default_user, password=self.default_pass, virtualhost=self.vhost
        )


AMQP_CONFIG = AMQPConfig()
GASH_EXCHANGE = RabbitExchange("GASH", auto_delete=True)


class UserQueuesV1:
    CREATE = RabbitQueue("v1.user_create", auto_delete=True)
    UPDATE = RabbitQueue("v1.user_update", auto_delete=True)
    DELETE = RabbitQueue("v1.user_delete", auto_delete=True)


class ScopeQueuesV1:
    CREATE = RabbitQueue("v1.scope_create", auto_delete=True)
    UPDATE = RabbitQueue("v1.scope_update", auto_delete=True)
    DELETE = RabbitQueue("v1.scope_delete", auto_delete=True)


class ResourceQueuesV1:
    CREATE = RabbitQueue("v1.resource_create", auto_delete=True)
    UPDATE = RabbitQueue("v1.resource_update", auto_delete=True)
    DELETE = RabbitQueue("v1.resource_delete", auto_delete=True)


class PermitQueuesV1:
    GET = RabbitQueue("v1.permit", auto_delete=True)
