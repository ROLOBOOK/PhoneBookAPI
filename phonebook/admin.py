from django.contrib import admin
from .models import PhoneNumber, Employee, Organization


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'phone_type', 'employee',)


admin.site.register(PhoneNumber, PhoneNumberAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'current_position', 'organization', 'display_phone_number')

    def display_phone_number(self, obj):
        return ', '.join(str(phone_number) for phone_number in obj.phone_numbers.all())


admin.site.register(Employee, EmployeeAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'descriptions', 'display_employees')

    def display_employees(self, obj):
        return ', '.join(str(full_name) for full_name in obj.employees.all())


admin.site.register(Organization, OrganizationAdmin)
