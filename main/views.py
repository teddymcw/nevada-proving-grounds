from django.shortcuts import render_to_response
#i don't see why any of this is necessary at the moment
from payments.models import User


def index(request):
    uid = request.session.get('user')
    if uid is None:
        return render_to_response('index.html')
    else:
        return render_to_response(
            'user.html', {'user': User.get_by_id(uid)}
        )
