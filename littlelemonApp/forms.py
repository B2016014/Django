from django.forms import ModelForm
from .models import booking


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = booking
        fields = "__all__"