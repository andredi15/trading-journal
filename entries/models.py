from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class Entry(models.Model):
    ONEORB="1-Min ORB"
    FIVEORB="5-Min ORB"
    ABCD="ABCD"
    REVERSAL="Reversal"
    PROFIT="Profit"
    LOSS="Loss"
    RESULT_CHOICES = (
        (PROFIT, "Profit"),
        (LOSS, "Loss")
    )
    STRATEGY_CHOICES = (
        (ONEORB,"1-Min ORB"),
        (FIVEORB,"5-Min ORB"),
        (ABCD,"ABCD"),
        (REVERSAL,"Reversal")
    )

    entered_date=models.DateField(auto_now_add=True)
    ticker=models.CharField(max_length=8, default="")
    strategy=models.CharField(max_length=12, choices=STRATEGY_CHOICES, default="ONEORB")
    result=models.CharField(max_length=6, choices=RESULT_CHOICES, default="PROFIT")
    comments=models.TextField(max_length=300, blank=True)
    image = models.ImageField(upload_to="", null=True, blank=True) #will save to default BASE_DIR which is 'uploads'
    trader = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="entries")

    def __str__(self):
        return f"{self.result} {self.entered_date}"