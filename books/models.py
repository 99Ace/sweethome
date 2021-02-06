from django.db import models

# Create your models here.
class Expense(models.Model):

    # LINK TO USER 
    # user = models.ForeignKey(
    #     User, 
    #     on_delete=models.CASCADE
    # )
    # NAME OF PRODUCT
    name = models.CharField(
        max_length=60,
        blank=False
    )
    # COST INCURRED
    price = models.DecimalField(
        blank=False,
        max_digits=5,
        decimal_places=2
    )
    # NAME OF VENDER
    vendor = models.CharField(
        max_length=60,
        blank=False
    )
    # CATEGORY OF EXPENSE
    CATEGORY = [
        ('Grocery','Grocery'),
        ('Education','Education'),
        ('Transport','Transport'),
        ('Vacation','Vacation'),
        ('Dining-out','Dining Out'),
        ('Insurance','Insurance'),
        ('Utilities','Utilities'),
    ]
    category = models.CharField(
        max_length=15,
        choices=CATEGORY,
        default='Grocery',
        blank=False
    )
    def __str__(self):
        return (self.name)
