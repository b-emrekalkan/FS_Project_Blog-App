from rest_framework.pagination import LimitOffsetPagination

#! For 6 posts to appear on each page 👇
class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 6
