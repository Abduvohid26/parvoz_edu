from django.urls import path
from .views import LeadAPIView, LeadDetailAPIView, LeadList, ExpectationList, SetList

urlpatterns = [
    path('', LeadAPIView.as_view()),
    path('<int:id>/', LeadDetailAPIView.as_view()),
    path('list/', LeadList.as_view()),
    path('expectation/list/', ExpectationList.as_view()),
    path('set/list/', SetList.as_view()),
]
