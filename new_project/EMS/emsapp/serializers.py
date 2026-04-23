from rest_framework import serializers
from .models import Company, Employee


# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'


# Company Serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def validate_name(self, value):
        if "test" in value.lower():
            raise serializers.ValidationError("Invalid company name")
        return value