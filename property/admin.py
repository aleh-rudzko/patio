from django.contrib import admin

# Register your models here.
from property.models import Type, Model, Service, Department, Employee, Entity, PropertyAddress, Repair, Equipment


class TypeAdmin(admin.ModelAdmin):
    pass


class ModelAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(admin.ModelAdmin):
    pass


class EmployeeAdmin(admin.ModelAdmin):
    pass


class EntityAdmin(admin.ModelAdmin):
    pass


class PropertyAddressAdmin(admin.ModelAdmin):
    pass


class ServiceAdmin(admin.ModelAdmin):
    pass


class RepairAdmin(admin.ModelAdmin):
    pass


class EquipmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Type, TypeAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Entity, EntityAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(PropertyAddress, PropertyAddressAdmin)
admin.site.register(Repair, RepairAdmin)
admin.site.register(Equipment, EquipmentAdmin)
