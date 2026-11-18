
import pytest

from app import create_app


@pytest.fixture
def client(monkeypatch, tmp_path):

    import config

    # Use a temporary database during tests
    monkeypatch.setattr(
        config.Config,
        "DATABASE_PATH",
        tmp_path / "test_chatbot.db"
    )

    from routes import chat_routes

    # Mock Gemini so tests do not need an API key
    monkeypatch.setattr(
        chat_routes,
        "generate_ai_response",
        lambda message, history: "This is a test AI response."
    )

    app = create_app()

    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_home_page(client):

    response = client.get("/")

    assert response.status_code == 200


def test_health_endpoint(client):

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json["status"] == "healthy"


def test_chat_endpoint(client):

    response = client.post(
        "/api/chat",
        json={"message": "Hello Gemini"}
    )

    assert response.status_code == 200

    assert response.json["success"] is True

    assert response.json["reply"] == "This is a test AI response."


def test_empty_message(client):

    response = client.post(
        "/api/chat",
        json={"message": " "}
    )

    assert response.status_code == 400


def test_chat_history(client):

    client.post(
        "/api/chat",
        json={"message": "Hello"}
    )

    response = client.get("/api/history")

    assert response.status_code == 200

    assert len(response.json["messages"]) == 2


def test_clear_history(client):

    client.post(
        "/api/chat",
        json={"message": "Hello"}
    )

    response = client.delete("/api/history")

    assert response.status_code == 200

    history_response = client.get("/api/history")

    assert history_response.json["messages"] == []
