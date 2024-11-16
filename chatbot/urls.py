from django.urls import path
from . import views
from chatbot_project.views import chatbot_response,index

urlpatterns = [
    path('', index, name='index'),
    path('chat/', chatbot_response, name='chatbot_response'),
    
]
