from rest_framework import pagination
class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = 'limit'
    page_size_query_param = 'page'
    max_page_size = 20