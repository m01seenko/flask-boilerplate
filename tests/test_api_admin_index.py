import http
from flask import Flask


def test_api_admin_wo_index_returns_403(app: Flask) -> None:
    client = app.test_client()
    response = client.get("/admin/")
    assert response.status_code == http.HTTPStatus.FORBIDDEN


def test_api_admin_w_index_returns_403(app: Flask) -> None:
    client = app.test_client()
    response = client.get("/admin/index")
    assert response.status_code == http.HTTPStatus.FORBIDDEN
