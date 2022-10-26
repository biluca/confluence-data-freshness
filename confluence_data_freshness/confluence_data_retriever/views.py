from bdb import Breakpoint
import re

from django.views import generic
from django.shortcuts import redirect, render
from django.http import HttpResponse
import pandas as pd
import json
from .confluence.extractor import Extractor
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

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

@method_decorator(csrf_exempt, name='dispatch')
def get_csv(request):
    body_unicode = request.body.decode('utf-8')
    x = body_unicode.replace("'", '"')
    body = json.loads(x)
    

    output_df = pd.DataFrame(body)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=export.csv'
    output_df.to_csv(path_or_buf=response, sep=',', encoding='utf-8')
    
    return response
