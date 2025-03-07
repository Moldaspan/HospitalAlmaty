from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=255, primary_key=True, db_column="Наименование")
    description = models.TextField(blank=True, null=True, db_column="Описание")
    categories = models.TextField(blank=True, null=True, db_column="Рубрики")
    address = models.CharField(max_length=255, db_column="Адрес")
    district = models.CharField(max_length=255, db_column="Район")
    working_hours = models.CharField(max_length=255, blank=True, null=True, db_column="Часы работы")
    phone_1 = models.CharField(max_length=20, blank=True, null=True, db_column="Телефон 1")
    phone_2 = models.CharField(max_length=20, blank=True, null=True, db_column="Телефон 2")
    phone_3 = models.CharField(max_length=20, blank=True, null=True, db_column="Телефон 3")
    email = models.EmailField(blank=True, null=True, db_column="E-mail")
    website = models.URLField(blank=True, null=True, db_column="Веб-сайт")
    instagram = models.URLField(blank=True, null=True, db_column="Instagram")
    facebook = models.URLField(blank=True, null=True, db_column="Facebook")
    whatsapp = models.URLField(blank=True, null=True, db_column="WhatsApp")
    x = models.FloatField(db_column="x")
    y = models.FloatField(db_column="y")
    gis_url = models.URLField(blank=True, null=True, db_column="2GIS URL")

    class Meta:
        db_table = "hospital"  

