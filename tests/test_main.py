from uuid import uuid4

import pytest
from faststream.rabbit import RabbitBroker

from tests.conftest import AMQP_CONFIG
from gash_client.core.client import GashClient
from gash_client.core.user.dto import UserCreateDTO


@pytest.mark.asyncio
async def test_main():
    broker = RabbitBroker(AMQP_CONFIG.connection_url())
    await broker.connect()
    client = GashClient(broker)
    await client.user_create(UserCreateDTO(id_=f'{uuid4()}', role='client'))
    await broker.close()
