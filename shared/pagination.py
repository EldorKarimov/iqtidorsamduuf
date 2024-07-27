from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 100
    last_page_strings = ("last_page", )

    def get_paginated_response(self, data):
        paginated_data = {
            "success": True,
            "count": self.page.paginator.count,
            "next":self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data
        }
        return paginated_data