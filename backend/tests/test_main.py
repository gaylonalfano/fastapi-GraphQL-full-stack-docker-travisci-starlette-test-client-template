# tests/test_main.my
# import graphene

from starlette.testclient import TestClient

# from graphene.test import Client

from app.main import app

client = TestClient(app)
# client = Client(app)


def test_main_graphql_get(test_app):
    """Using Starlette Test Client"""
    response = test_app.get(url="/?query={ hello }")
    assert response.status_code == 200
    assert response.json() == {"data": {"hello": "Hello stranger"}}


#     """Using Graphene Test Client"""
#     executed = test_app.execute(query="""{ hello }""")
#     assert executed == {"data": {"hello": "Hello FastAPI with GraphQL"}}


# def test_ping(test_app):
#     response = test_app.get("/ping")
#     assert response.status_code == 200
#     assert response.json() == {"ping": "pong!"}
