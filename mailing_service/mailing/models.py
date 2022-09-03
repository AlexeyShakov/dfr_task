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

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"



class Client(models.Model):

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    GENDER = (
        ("M", "Male"),
        ("F", "Female")
            )

    mobile_validator = RegexValidator(regex=r"^7\d{10}$")
    mobile_number = models.CharField(max_length=11, validators=[mobile_validator])
    operator_code = models.CharField(max_length=3, default="---")
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    tag = models.CharField(max_length=1, choices=GENDER, verbose_name="Пол пользователя")
    timezone = models.CharField(max_length=50, choices=TIMEZONES)

    def save(self, *args, **kwargs):
        self.operator_code = self.mobile_number[1:4]
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Message(models.Model):
    SENT = "sent"
    NO_SENT = "no sent"

    STATUS_CHOICES = [
        (SENT, "Sent"),
        (NO_SENT, "No sent"),
    ]

    time_create = models.DateTimeField(verbose_name='Time create', auto_now_add=True)
    sending_status = models.CharField(verbose_name='Sending status', max_length=15, choices=STATUS_CHOICES)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f'Message {self.id} with text {self.mailing} for {self.client}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'




