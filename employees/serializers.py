from rest_framework import serializers
from employees.models import User

# class CompanaySerializer(serializers.Serializer):
#     class Meta:
#         model = Company
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    # comapny = CompanaySerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'