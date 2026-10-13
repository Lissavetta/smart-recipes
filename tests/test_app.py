from app import app


def test_index_get_ok():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Умный генератор рецептов".encode("utf-8") in resp.data


def test_index_post_returns_recipe():
    client = app.test_client()
    resp = client.post("/", data={"ingredients": ["яйца", "молоко", "помидоры", "лук"]})
    assert resp.status_code == 200
    assert "Омлет".encode("utf-8") in resp.data


def test_health_endpoint():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_version_endpoint():
    client = app.test_client()
    resp = client.get("/version")
    assert resp.status_code == 200
    assert resp.get_json() == {"version": "1.0.0"}
