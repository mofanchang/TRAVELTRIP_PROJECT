from django.db import models

class Trip(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    available_seats = models.IntegerField(default=0)

    # 推薦邏輯需要的欄位
    location = models.CharField(max_length=100)
    duration = models.IntegerField()  # 行程天數

    # 新增欄位
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
