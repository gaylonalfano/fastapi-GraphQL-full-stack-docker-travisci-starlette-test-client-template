# Starlette TestClient example
import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here


# ----- Graphene Client
# # tests/conftest.py
# import pytest
# import graphene

# from starlette.testclient import TestClient
# from graphene.test import Client

# # Import Query class object for GraphQL
# # from app.main import Query
# from app.main import app

# # from app.main import GraphQLApp

# # For Graphene Client I need to pass schema object
# # ? How to access the app.GraphQLApp.schema property from app.main import app?
# # from app.main import app

# # Define a schema object for Graphene Client
# # schema = graphene.Schema(query=Query)
# # schema = app.__getattribute__("schema")
# # sca = GraphQLApp.schema  # AttributeError: 'GraphQLApp' has no attribute
# # TODO May 11, 2020: Can't seem to access the app.schema but
# # TODO  but there is GraphQLApp.execute() that looks similar to Client.execute


# @pytest.fixture(scope="module")
# def test_app():
#     print(f"schema from GraphQLApp.schema {sca}")
#     client = Client(sca)
#     yield client  # testing happens here
