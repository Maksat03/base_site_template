from django.db import models


class Feedback(models.Model):
    company_logo = models.ImageField(upload_to="feedback_company_logos/")
    company_name = models.CharField(max_length=50)
    text = models.TextField()

    # is_needed_to_add_company_logo_into_clients_section = models.BooleanField(default=False)
