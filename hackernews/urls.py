from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

app_name = 'hackernews'

urlpatterns = [
    path('admin/', admin.site.urls),
    # change graphiql=False to disable in production environment
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
