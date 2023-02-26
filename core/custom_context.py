from devx.core.models import Application


def site_globals(request):
    ApplicationDB=Application.objects.filter(status="Accepted")
    context={
        'money':0,
        "seats_reserved":0
    }
    return context