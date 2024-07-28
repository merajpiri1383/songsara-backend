from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination) : 
    page_size = 20
    display_page_controls = True
