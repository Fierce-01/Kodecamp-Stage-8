from django.urls import path
from .views import home, records, details, book_room

app_name = 'home'

urlpatterns = [
    path('', home, name='homeview'),
    path('details/<int:ID>/', details, name='detailview'),
    path('records/', records, name='recordview'),
    path('book_room/', book_room, name='bookroomview')
]