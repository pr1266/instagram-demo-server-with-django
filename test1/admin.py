from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name']


admin.site.register(Address)
admin.site.register(City)
admin.site.register(Customer)
admin.site.register(Game)
admin.site.register(G_Category)
admin.site.register(Platform)
admin.site.register(GameOrder)
admin.site.register(GameDelivery)
admin.site.register(A_Category)
admin.site.register(Accessory)
admin.site.register(AccessoryOrder)
admin.site.register(AccessoryDelivery)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)