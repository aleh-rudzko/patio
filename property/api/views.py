from django.contrib.auth.models import User
from rest_framework import viewsets
from property.api.serializers import UserSerializer, ModelSerializer, TypeSerializer, AddressSerializer, \
    EntitySerializer, DepartmentSerializer, EmployeeSerializer, EquipmentSerializer, ServiceSerializer, RepairSerializer
from property.models import Model, Type, PropertyAddress, Entity, Department, Equipment, Service, Repair, Employee


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = PropertyAddress.objects.all()
    serializer_class = AddressSerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class RepairViewSet(viewsets.ModelViewSet):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
