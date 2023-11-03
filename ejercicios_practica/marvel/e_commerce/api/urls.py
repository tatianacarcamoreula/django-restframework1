from django.urls import path
from e_commerce.api.views import *


urlpatterns = [
    path('comic-list/', comic_list_api_view),
    path('comic-retrieve/', comic_retrieve_api_view),
    path('comic-create/', comic_create_api_view),
    path('comic-list-filtered/', comic_list_filtered_api_view),
    path('comic-filter-stock_qty/', comic_filter_stock_qty_api_view),
]