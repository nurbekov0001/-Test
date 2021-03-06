from django.urls import path
from webapp.views import (
    index_view,
#     book_view,
#     book_create_view,
#     book_update_view,
#     book_delete_view
)
#
urlpatterns = [
    path('', index_view, name='book_list'),
    # path('<int:pk>/', book_view, name='book_view'),
    # path('add/', book_create_view, name='book_add'),
    path('<int:pk>/update/', book_update_view, name='book_update'),
    path('<int:pk>/delete/', book_delete_view, name='book_delete'),
]