# conftest.py
import pytest
import app

@pytest.fixture
def api(monkeypatch): # Fixtures can use fixtures!
    test_chars = {"characters": ['Bob', 'Jim']}
    monkeypatch.setattr(app, "data", test_chars)
    # Here we are monkey patching a variable but you might well reset a test database here instead.
    api = app.app.test_client()
    return api