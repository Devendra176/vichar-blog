from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import (Homeview,
                    Homeaboutview,
                    RegistrationView,
                    Loginview,
                    BlogListView,
                    CreateBlogPost,
                    BlogIndiviualView,
                    PostDeleteView,
                    PostUpdateview,
                 
                    ProfileView,
                    )

# app_name = 'blog'
urlpatterns = [
    path('', Homeview.as_view(),name='blog-home'),
    path('about/',Homeaboutview.as_view(), name='blog-about'),
    path('registration/', RegistrationView.as_view(), name='blog-registration'),
    path('signin/',Loginview.as_view(), name='blog-signin'),
    path('main/',login_required(BlogListView.as_view()), name='blog-main'),
    path('<pk>/update/', login_required(PostUpdateview.as_view()), name='blog-update'),
    path('create-blog/', login_required(CreateBlogPost.as_view()), name='blog-create'),
    path('<pk>/post/',login_required(BlogIndiviualView.as_view()), name='blog-post'),
    # path('profile/',ProfileView.as_view(),name='blog-profile'),
    # path('bio/',views.bio,name='blog-bio'),
    # path('username/',views.username,name='blog-username'),
    # path('resetpass/',views.resetpass,name='blog-resetpass'),
    path('<pk>/userprofile/',login_required(ProfileView.as_view()),name='blog-userprofile'),
    # path('forget/',views.form_valid,name='blog-forget'),
    # path('forgetpass/',views.otpcheck,name='blog-otp'),
    # path('ChangePassword/',views.changepass,name='blog-changepass'),

    # path('profilepic/',views.profilepic,name='blog-profilepic'),
    # path('cover/',views.cover,name='blog-cover'),
    path('<pk>/delete/',login_required(PostDeleteView.as_view()),name='blog-delete'),
    path('logout/',views.logout, name='logout'),
]
