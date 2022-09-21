import re

from django.views import generic
from django.shortcuts import redirect, render

from .confluence.extractor import Extractor

def children(request, hub_page_id):
    template_name = 'confluence_data_retriever/children.html'

    extractor = Extractor()
    extractor.append_hub_page(hub_page_id, 0)
    extractor.append_children_pages(hub_page_id, 1)

    all_pages = extractor.get_all_pages()

    return render(request, template_name, {'all_pages': all_pages})
        

class SearchView(generic.TemplateView):
    template_name = 'confluence_data_retriever/search.html'


def search(request):
    hub_page_url = request.POST['hub_page_url'] 
    search_string = re.search('\d{1,60}', hub_page_url, re.IGNORECASE)

    if search_string:
        hub_page_id = search_string.group(0)
    
    return redirect(f'children/{hub_page_id}')
