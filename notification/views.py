from django.http import HttpResponse
from django.template import loader
from notification.models import Notification
from django.views.decorators.cache import never_cache


@never_cache
def index(request, id):
    template = loader.get_template('index.html')

    Notification.objects.filter(id=id).update(is_seen=True)

    context = {
        'notif': Notification.objects.filter(target_user=request.user, is_seen=False)
    }

    if request.user.is_active:
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("<h1>UNAUTHORIZED</h1>")

