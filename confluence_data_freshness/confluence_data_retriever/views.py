import re

from .confluence.service.confluence_api import ConfluenceAPI
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import redirect, render

def children(request, hud_page_id):
    template_name = 'confluence_data_retriever/children.html'

    confluence_api = ConfluenceAPI()
    response = confluence_api.get_child(hud_page_id)
    children_list = response['results']

    return render(request, template_name, {'children_list': children_list})
        

class SearchView(generic.TemplateView):
    template_name = 'confluence_data_retriever/search.html'


def search(request):
    hub_page_url = request.POST['hub_page_url'] 
    search_string = re.search('\d{1,60}', hub_page_url, re.IGNORECASE)

    if search_string:
        hub_page_id = search_string.group(0)
    
    return redirect(f'children/{hub_page_id}')
