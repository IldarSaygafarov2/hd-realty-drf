from django.db import models


class GoalChoices(models.TextChoices):
    BUY = "buy", "Купить"
    SELL = "sell", "Продать"


class OperationTypeChoices(models.TextChoices):
    RENT = "rent", "Аренда"
    BUY = "buy", "Покупка"
