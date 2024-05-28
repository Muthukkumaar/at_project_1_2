import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_session():
    # Setup code for the entire session
    yield
    # Teardown code for the entire session
