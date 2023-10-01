from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'restaurant'

class Order(models.Model):
    items = models.ManyToManyField(MenuItem)
    table_number = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.pk}"
    
    class Meta:
        app_label = 'restaurant'

