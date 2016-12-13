from django.conf.urls import url, include
from todo import views
from rest_framework.routers import DefaultRouter

# Creation of the roiuter and register our viewsets with it
router = DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemViewSet)

# The api urls are now determinined automatically by the router
urlpatterns = [
	url(r'^', include(router.urls)),
]
