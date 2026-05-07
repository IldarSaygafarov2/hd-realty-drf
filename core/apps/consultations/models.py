from django.db import models

from core.apps.common.models import BaseModel


class NamePhoneFieldsModel(BaseModel):
    name = models.CharField("Имя", max_length=150)
    phone = models.CharField("Телефон", max_length=32)

    class Meta:
        abstract = True


class ConsultationRequest(NamePhoneFieldsModel):
    """Заявка с формы «Получите экспертную оценку»."""

    class Goal(models.TextChoices):
        BUY = "buy", "Купить"
        SELL = "sell", "Продать"

    goal = models.CharField(
        "Цель",
        max_length=16,
        choices=Goal.choices,
    )
    comment = models.TextField("Комментарий", blank=True)

    class Meta:
        verbose_name = "Заявка на консультацию"
        verbose_name_plural = "Заявки на консультацию"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.phone})"


class ContactRequest(NamePhoneFieldsModel):
    """Заявка с формы «Оставьте заявку — подскажем следующий шаг»."""

    comment = models.TextField("Комментарий менеджера", blank=True)

    class Meta:
        verbose_name = "Заявка на обратный звонок"
        verbose_name_plural = "Заявки на обратный звонок"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.phone})"


class NextStepRequest(NamePhoneFieldsModel):
    """Заявка с формы «Оставьте заявку — подскажем следующий шаг»."""

    task_description = models.TextField("Описание задачи", blank=True)

    class Meta:
        verbose_name = "Заявка «Подскажем следующий шаг»"
        verbose_name_plural = "Заявки «Подскажем следующий шаг»"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.phone})"
