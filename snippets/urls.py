from snippets import views
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns


# version 1
# http://127.0.0.1:8000/snippets/2/?format=json
# http://127.0.0.1:8000/snippets/2/?format=html
# urlpatterns = [
#     path('', views.snippet_list),
#     path('<int:pk>/', views.snippet_detail),
# ]

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)