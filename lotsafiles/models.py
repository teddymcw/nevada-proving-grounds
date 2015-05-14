from django.db import models
#from payments.models import User #for using a OneToOne or FK later


class VerifyMembership(models.Model):
    # TM 042515 ImageFields are more complicated, refer to docs and Pillow
    # Save these to media folder
    #user = models.OneToOneField(User) #need to get this model and form relationship working!
    verify_membership_file = models.FileField(upload_to='account_verification/files', null=True, blank=True)


class AgainVerifyMembership(models.Model):
    # TM 042515 ImageFields are more complicated, refer to docs and Pillow
    # Save these to media folder
    #user = models.OneToOneField(User) #need to get this model and form relationship working!
    again_ver_memb = models.FileField(upload_to='media/acc_verify/files', null=True, blank=True)
