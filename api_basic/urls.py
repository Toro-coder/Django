from django.urls import path
from .views import article_list, article_detail, GenericAPIView, ArticleAPIView, ArticleDetails

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail)
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view())
]
