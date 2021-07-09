from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    custom pagination class,
    allowing you to set the item limit per page
    """
    page_size_query_param = 'limit'
