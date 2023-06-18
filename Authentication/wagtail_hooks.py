from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup

from .models import CustomUser


class CustomUserAdmin(ModelAdmin):
    model = CustomUser
    menu_label = "Пользователи"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("phone", "username", "email",
                    "rating", "is_active", "staff",
                    "password")


modeladmin_register(CustomUserAdmin)

