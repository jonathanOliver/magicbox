# """magicBox URL Configuration


from django.conf.urls import url
from . import view
from django.conf.urls.static import static
from django.conf import settings

app_name ='magicBox'

urlpatterns = [
    url(r'^login/$',view.login_view, name="login"),
    url(r'^sidebar/$',view.sidebar_view, name="sidebar"),
    url(r'^dashboard/$',view.dashboard_view, name="dashboard"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
