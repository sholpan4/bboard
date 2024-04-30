from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template
from django.http import Http404, HttpResponse



def index(request):
    return render(request, 'main/index.html')


def other_page(request, page):
    try:
        template = get_template('main/'+ page + '.html')
    except TemplateDoesNotExist:
        return Http404

    return HttpResponse(template.render(request=request))
