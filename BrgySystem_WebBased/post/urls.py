from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'Post'
urlpatterns = [
    path('postlist/',views.postListView.as_view(),name ="postList"),
    path('event/<int:pk>',views.postDetail.as_view(), name='postDetail'),
    path('events/<int:pk>',views.UserpostDetail.as_view(),name='UserDetail'),
    path('add_Event/',views.addPostView.as_view(),name='add_Post'),
    path('staffPostList/',views.staffListView.as_view(),name='staffList'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
