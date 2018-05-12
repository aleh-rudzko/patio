from rest_framework import routers

from property.api.views import UserViewSet, ModelViewSet, TypeViewSet, AddressViewSet, EntityViewSet, DepartmentViewSet, \
    EquipmentViewSet, ServiceViewSet, RepairViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'models', ModelViewSet)
router.register(r'types', TypeViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'entities', EntityViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'equipments', EquipmentViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'repairs', RepairViewSet)

