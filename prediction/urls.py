from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^accessform/',views.accessform, name='accessform')

]

#<input type="text" name="Stock_name" id="Stock_name">
 #   <input type="submit" value="Submit">