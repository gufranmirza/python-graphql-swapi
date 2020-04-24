from django.conf.urls import url, include
from django.contrib import admin

from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from graphql_playground.views import GraphQLPlaygroundView 

from pythonSWAPI.schema import schema

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/$', csrf_exempt(GraphQLView.as_view(graphiql=False))),
    url(r'^graphql/$', csrf_exempt(GraphQLPlaygroundView.as_view(endpoint="http://127.0.0.1:8000/api/"))),
]