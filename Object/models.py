from django.db import models
from Authentication.models import CustomUser


class CategoryChoice(models.TextChoices):
    FOOD = "fd", "Еда / доставка"
    PRODUCTS = "prod", "Товары"
    SERVICES = "sr", "Услуги"
    BEAUTY = "bt", "Красота"
    HEALTH = "hl", "Здоровье"
    SPORT = "sp", "Спорт"
    ENTERTAINMENT = "en", "Развлечения"
    HOLIDAYS = "hd", "Праздники"
    CULTURE = "cl", "Культура/Кино"
    AUTO = "at", "Авто/мото"
    PROPERTY = "pr", "Недвижимость"
    FINANCE = "fn", "Финансы"
    STUDY = "st", "Обучение"
    HOTELS = "ht", "Гостиницы"
    TOURISM = "tr", "Туризм"


class Company(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    email = models.CharField(max_length=30, verbose_name="Эмайл")
    phone = models.CharField(max_length=30, verbose_name="телефон")
    location = models.TextField(verbose_name="Адрес")
    latitude = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="широта")
    longitude = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="долгота")
    category = models.CharField(max_length=50, choices=CategoryChoice.choices, verbose_name="категория")
    administrator = models.ManyToManyField(CustomUser, related_name="company")
