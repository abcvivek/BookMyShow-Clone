from django.db import models
from django.forms import ModelForm
from dashboard.models import show
from django.contrib.auth.models import User

# Create your models here.


TICKET_STATUS_CHOICES = (
    (1, 'AVAILABLE'),
    (2, 'BLOCKED'),
    (3, 'BOOKED')
)

class booking(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    row_num = models.PositiveSmallIntegerField(null=False, blank=False)
    col_num = models.PositiveSmallIntegerField(null=False, blank=False)
    show = models.ForeignKey(show,related_name="booking_show",null=False,on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="booking_user",null=False,default=None, on_delete=models.CASCADE)
    status = models.IntegerField(choices=TICKET_STATUS_CHOICES, default=1)
    session = models.CharField(blank=False, null=False, max_length=200)

    class Meta:
        unique_together = ('show', 'row_num', 'col_num')


class TicketsForm(ModelForm):
    class Meta:
        model = booking
        fields = ['name','age','row_num', 'col_num',]