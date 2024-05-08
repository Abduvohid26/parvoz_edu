from django.db import models
LEAD, EXPECTATION, SET, = ('lead', 'expectation', 'set')


class Lead(models.Model):
    LEAD_STATUS = (
        (LEAD, LEAD),
        (EXPECTATION, EXPECTATION),
        (SET, SET)
    )
    phone_number = models.CharField(max_length=14)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    lead_status = models.CharField(max_length=100, choices=LEAD_STATUS, default=LEAD)

    def __str__(self):
        return self.phone_number
