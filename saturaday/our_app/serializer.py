from our_app.models import our_model
from rest_framework.serializers import ModelSerializer

class our_model_serializer(ModelSerializer):

    class Meta:
        model = our_model
        fields = '__all__'