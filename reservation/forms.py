from django import forms
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

from reservation.models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'email', 'phone', 'number', 'date']
        model = Reservation

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label='date',  # date format is  "yyyy-mm-dd"
                                              widget=AdminJalaliDateWidget(
                                              )
                                              # optional, to use default datepicker
                                              )
