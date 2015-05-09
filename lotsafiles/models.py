from django.db import models


class VerifyMembership(models.Model):
    # TM 042515 ImageFields are more complicated, refer to docs and Pillow
    # Save these to media folder
    verify_membership_file = models.FileField(upload_to='account_verify/files', null=True, blank=True)
