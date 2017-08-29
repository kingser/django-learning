from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name='bike'
urlpatterns =[
    url(r'^$',views.index),
    url(r'^image$',views.image,name='image'),
    url(r'^imageSumbit$',views.imageSubmit ,name='imageSubmit'),

]