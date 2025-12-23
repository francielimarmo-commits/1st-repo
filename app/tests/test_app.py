import os
import re

# Importa o app Flask do seu app.py
from app import app as flask_app


def test_home_returns_200():
    client = flask_app.test_client()
    res = client.get("/")
    assert res.status_code == 200


def test_health_returns_ok_and_checked_at():
    client = flask_app.test_client()
    res = client.get("/health")
    assert res.status_code == 200

    data = res.get_json()
    assert data["status"] == "ok"
    assert "checked_at" in data

    # formato esperado: YYYY-MM-DD HH:MM:SS
    assert re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", data["checked_at"])


def test_version_returns_expected_keys():
    # Garante que variáveis de ambiente não atrapalhem o teste
    os.environ.setdefault("APP_NAME", "Test App")
    os.environ.setdefault("APP_VERSION", "9.9.9")
    os.environ.setdefault("IMAGE_FILE", "pinguim.jpeg")

    client = flask_app.test_client()
    res = client.get("/version")
    assert res.status_code == 200

    data = res.get_json()
    assert "app_name" in data
    assert "version" in data
    assert "image_file" in data

