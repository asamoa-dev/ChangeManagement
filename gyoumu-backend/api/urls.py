# from django.urls import path, include
# from .views import TestApiView

# urlpatterns = [
#     path('', TestApiView.as_view()),
# ]


from django.urls import path
from .views import SnowflakeDataView

urlpatterns = [
    path('snowflake-data/', SnowflakeDataView.as_view(), name='snowflake-data')
]

