import pytz as pytz
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class Mailing(models.Model):

    GENDER = (
        ("M", "Male"),
        ("F", "Female")
            )
    MOBILE_CODE = [
        ("920", "Мегафон"),
        ("910", "МТС"),
        ("905", "Билайн"),
        ("900", "Теле2")
    ]
    beginning_date = models.DateTimeField("Начало рассылки")
    message = models.TextField(default="Мы хотим предложить Вам курсы по программированию со скидкой 90%",
                               verbose_name="Сообщение рассылки")
    gender_filter = models.CharField(max_length=1, choices=GENDER, verbose_name="Пол пользователя")
    operator_code_filter = models.CharField(max_length=3, choices=MOBILE_CODE,
                                            verbose_name="Код мобильного оператора")
    ending_date = models.DateTimeField(verbose_name="Окончание рассылки")

    def __str__(self):
        return f"Рассылка от {self.beginning_date}"


class Client(models.Model):

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    GENDER = (
        ("M", "Male"),
        ("F", "Female")
            )

    mobile_validator = RegexValidator(regex=r"^7\d{10}$")
    mobile_number = models.CharField(max_length=11, validators=[mobile_validator])
    email = models.CharField()
    name = models.CharField()
    surname = models.CharField()
    gender = models.CharField(max_length=1, choices=GENDER, verbose_name="Пол пользователя")
    timezone = models.CharField(choices=TIMEZONES, default="UTC")
