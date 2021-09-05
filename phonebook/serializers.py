from rest_framework import serializers
from .models import Organization, Employee, PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):
    res_number = serializers.SerializerMethodField()

    class Meta:
        fields = ('res_number',)
        model = PhoneNumber

    def get_res_number(self, obj):
        return f'{obj.phone_type}: {obj.phone_number}'


class EmployeeSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('full_name', 'current_position', 'phone_numbers',)


class OrganizationFullSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('name', 'employees')


class OrganizationNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('name',)
