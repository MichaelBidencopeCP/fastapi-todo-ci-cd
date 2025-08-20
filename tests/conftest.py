import asyncio
import pytest
from httpx import AsyncClient, ASGITransport
from todo.main import create_app

@pytest.fixture(scope="session")
def event_loop():
    """
    Create one asyncio event loop for the entire test session.
    Why: async tests need a loop to run on; making it explicit avoids platform quirks.
    """
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture()
def app():
    """
    Build a fresh FastAPI app for each test by calling the factory.
    Fresh app = no cross-test leakage of state or overrides.
    """
    return create_app()

@pytest.fixture()
async def client(app):
    """
    Create an async HTTP client that talks to the app IN MEMORY.
    No real server or sockets; it's fast and respects app lifespan events.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac