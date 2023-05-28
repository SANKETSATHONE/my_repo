from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from our_app.serializer import our_model_serializer
from our_app.models import our_model
from rest_framework import mixins


class our_modelview(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.ListModelMixin,
                    mixins.DestroyModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    serializer_class = our_model_serializer
    queryset = our_model.objects.all()