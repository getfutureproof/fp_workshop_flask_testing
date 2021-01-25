import pytest
import json
# - Homepage
#    - GET, gives us 200, and some welcome message
#    - POST is invalid
# - Index HTML
#    - GET with a list of things as HTML
# - Index JSON
#    - GET with a list of things as JSON
# - Like
#    - POST to to like something
#    - GET is invalid


def test_homepage(client):
    get_res = client.get("/")
    assert get_res.status_code == 200
    assert "You are successfully connected to the server." in get_res.get_data(as_text=True)
    post_res = client.post("/")
    assert post_res.status_code != 200


def test_html_index(client):
    res = client.get("/gifs/html")
    assert res.status_code == 200
    assert "Look at these wonderful gifs" in res.get_data(as_text=True)


def test_json_index(client):
    res = client.get("/gifs/json")
    assert res.status_code == 200
    json_response = res.get_json()
    assert "gifs" in json_response
    assert len(json_response["gifs"]) > 0


def test_like_gif(client):
    post_res = client.post("/like", json={
        "gif_id": 1,
        "action": "like"
    })
    assert post_res.status_code == 204
    
    get_res = client.get("/like")
    assert get_res.status_code != 200
