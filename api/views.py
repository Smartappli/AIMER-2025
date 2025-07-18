from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from api.graphql.v1 import schema_v1

# API GraphQL v1
graphql_view_v1 = csrf_exempt(GraphQLView.as_view(schema=schema_v1, graphiql=True))

