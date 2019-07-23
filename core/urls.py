from .views import home_view
from django.urls import path


urlpatterns=[

       path('',home_view,name='home_view'),
           
] 

# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# Create your views here.
