from rest_framework import serializers
from fitwellNG_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # this fields determines the no of fields from user model
        # that can be retirieved and save via API endpoint request
        fields = ['id', 'email', 'sex', 'height', 'weight', 'dob', 'security', 'security_answer']

