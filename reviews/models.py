from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    # maximum rate for rating is 5
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.user_name} rated {self.rating} stars"
