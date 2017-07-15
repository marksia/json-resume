from django.conf.urls import url

from .views import JsonUploaderView, JSONProfileView

urlpatterns = [
    url(r'^$', JsonUploaderView.as_view(), name="index"),
    url(r'^profile$', JSONProfileView.as_view(), name="profile")
]