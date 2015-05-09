from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import VerifyForm
from models import VerifyMembership


def img_upload(request):
    if request.method == 'POST':

        verify_form = VerifyForm(request.POST, request.FILES)
        hack = 1
        try:
            cur_user = request.user
            cur_user += str(hack)
            hack += 1
            print request.user
        except Exception as e:
            
            print e
            print request.user

        if verify_form.is_valid():
            verified_file = VerifyMembership(user=cur_user, verify_membership_file=request.FILES['verify_membership_file'])
            verified_file.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('account-verify'))

    else:
        verify_form = VerifyForm()

    context = {'verify_form': verify_form}
    return render(request, 'upload_verification.html', context)# Create your views here.
