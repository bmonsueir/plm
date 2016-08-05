from django.http import HttpResponse
from django.template import loader

from .models import Chemical


def index(request):
    chemical_list = Chemical.objects.order_by('-pub_date')[:5]
    template = loader.get_template('chemicals/index.html')
    context = {
        'chemical_list': chemical_list,
    }
    return HttpResponse(template.render(context, request))
