from django.http import HttpResponse
from django.template import loader

def home(request):

    template = loader.get_template('home.html')
    render = template.render()

    return HttpResponse(render)
