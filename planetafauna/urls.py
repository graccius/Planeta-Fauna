from django.urls import path, include

urlpatterns = [
    path('', include('animais.urls')), 
    path('api/', include('api.urls')),

]
