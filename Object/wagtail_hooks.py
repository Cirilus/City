from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup

from .models import News, Advertisement, Company


class CompanyAdmin(ModelAdmin):
    model = Company
    menu_label = "Компании"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "description", "email", "phone",
                    "location", "latitude", "longitude", "category",
                    "administrator")


modeladmin_register(CompanyAdmin)


class AdvertisementAdmin(ModelAdmin):
    model = Advertisement
    menu_label = "Объявление"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "body", "email", "phone",
                    "created_at", "administrator", "is_active",)


modeladmin_register(AdvertisementAdmin)


class NewsAdmin(ModelAdmin):
    model = News
    menu_label = "Новости"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "body", "created_at",
                    "administrator", "is_active")


modeladmin_register(NewsAdmin)
