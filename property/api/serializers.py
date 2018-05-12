from django.contrib.auth.models import User
from rest_framework import serializers

from property.models import Model, Type, PropertyAddress, Entity, Department, Employee, Equipment, Service, Repair


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAddress
        fields = '__all__'


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    entity = EntitySerializer()
    address = AddressSerializer()

    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    model = ModelSerializer()
    employee = EmployeeSerializer()

    class Meta:
        model = Equipment
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class RepairSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    equipment = EquipmentSerializer()

    class Meta:
        model = Repair
        fields = '__all__'
