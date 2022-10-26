from django.urls import path

from . import views

app_name = "confluence_data_retriever"
urlpatterns = [
    path('children/<int:hub_page_id>', views.children, name='children'),
    path('searching', views.search, name='search_action'),
    path('search', views.SearchView.as_view(), name='search'),
    path('get_csv', views.get_csv, name='get_csv'),
    
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
]
