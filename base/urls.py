from django.urls import path
from . import views
urlpatterns = [
path('',views.upload_view,name='upload-views'),
path('create_df/',views.create_df,name='create-df')
]