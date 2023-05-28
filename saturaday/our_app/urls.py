from django.contrib import admin
from django.urls import path, include
from our_app.views import our_modelview
from rest_framework.routers import SimpleRouter

our_model_router = SimpleRouter()
our_model_router.register('our_app', our_modelview)

urlpatterns = [
    path('',include(our_model_router.urls))
]