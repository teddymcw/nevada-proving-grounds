from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.contrib import messages
from forms import VerifyForm, AgainVerifyForm
from models import VerifyMembership, AgainVerifyMembership


def img_upload(request):
    if request.method == 'POST':

        verify_form = AgainVerifyForm(request.POST, request.FILES)      
        try:
            cur_user = request.user
            print cur_user
        except Exception as e:

            cur_user = request.user
            print cur_user
            print e
            print request.user

        if verify_form.is_valid():
            verified_file = AgainVerifyMembership(again_verify_memb=request.FILES['again_verify_memb']) #user=cur_user, #insert at beginning when ready 
            verified_file.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('register'))

    else:
        again_verify_form = AgainVerifyForm()

    context = {'verify_form': again_verify_form}
    return render(request, 'upload_verification.html', context)# Create your views here.

class CbvImgUpView(FormView):
    http_method_names = [u'get', u'post']
    model = AgainVerifyMembership
    template_name = 'again_ver.html'
    form_class = AgainVerifyForm
    form_kwargs = {}


    def get_success_url(self):
        return reverse('contact')

    def form_valid(self, form):
        messages.info(
            self.request,
            "You have successfully uploaded you image. Thank you."
        )
        return super(CbvImgUpView, self).form_valid(form)

    def form_invalid(self, form):
        messages.info(
            self.request,
            "Your submission has not been saved. Try again."
        )
        return super(CbvImgUpView, self).form_invalid(form)

'''example from great blog post on FormView

    def get(self, *args, **kwargs):
        # You can access url variables from kwargs
        # url: /email_preferences/geeknam > kwargs['username'] = 'geeknam'
        # Assign to self.subscriber to be used later
        self.subscriber = get_subscriber(kwargs['username'])

    def post(self, request, *args, **kwargs):
        # Process view when the form gets POSTed
        pass

    def get_initial(self):
        # Populate ticks in BooleanFields
        initial = {}
        for s in self.subscriber.events.all():
            initial[s.value_id] = True
        return initial

    def get_form(self, form_class):
        # Initialize the form with initial values and the subscriber object
        # to be used in EmailPreferenceForm for populating fields
        return form_class(
            initial=self.get_initial(),
            subscriber=self.subscriber
        )

    def get_success_url(self):
        # Redirect to previous url
        return self.request.META.get('HTTP_REFERER', None)

    def form_valid(self, form):
        messages.info(
            self.request,
            "You have successfully changed your email notifications"
        )
        return super(EmailPreferenceView, self).form_valid(form)

    def form_invalid(self, form):
        messages.info(
            self.request,
            "Your submission has not been saved. Try again."
        )
        return super(EmailPreferenceView, self).form_invalid(form)
'''
