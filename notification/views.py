from django.http import HttpResponse
from django.template import loader
from notification.models import Notification


# Create your views here.
def index(request, id):
    template = loader.get_template('index.html')

    Notification.objects.filter(id=id).update(is_seen=True)

    context = {
        'notif': Notification.objects.filter(target_user=request.user, is_seen=False)
    }

    return HttpResponse(template.render(context, request))
