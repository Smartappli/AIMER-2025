from django.urls import path
from api.views import graphql_view_v1

urlpatterns = [
    path("graphql/", graphql_view_v1, name="graphql"),
]