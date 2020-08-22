import http
from flask import Flask


def test_api_root_wo_index_returns_200(app: Flask) -> None:
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == http.HTTPStatus.OK


def test_api_root_w_index_returns_200(app: Flask) -> None:
    client = app.test_client()
    response = client.get("/index")
    assert response.status_code == http.HTTPStatus.OK
