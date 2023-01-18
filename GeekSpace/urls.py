from django.contrib import admin
from django.urls import path
from .views import index
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

from Categories.views import AddGPost, AddCPost, AddCodingPost, AddAPost, GamesList, CryptoList, C_List, AnimeList, GameUpdate, CryptoUpdate, CodeUpdate, AnimeUpdate, GameDeleteView, CodingDeleteView, CryptoDeleteView, AnimeDeleteView
from users.views import login_view, signup, profile, pfp

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    
    path('gaming/', GamesList, name='GamesList'),
    path('gaming/add-post',AddGPost, name='AddGPost'),
    path('gaming/update/<int:pk>/', GameUpdate, name='GameUpdate'),
    path('gaming/delete/<int:pk>/', GameDeleteView.as_view(), name='GameDelete'),
       
    path('crypto/', CryptoList, name='CryptoList'),
    path('crypto/add-post', AddCPost, name='AddCPost'),
    path('crypto/update/<int:pk>/', CryptoUpdate, name='CryptoUpdate'),
    path('crypto/delete/<int:pk>/', CryptoDeleteView.as_view(), name='CryptoDelete'),
    
    path('coding/', C_List, name='CodingList'),
    path('coding/add-post', AddCodingPost, name='AddCodingPost'),
    path('coding/update/<int:pk>/', CodeUpdate, name='CodeUpdate'),
    path('coding/delete/<int:pk>/', CodingDeleteView.as_view(), name='CodeDelete'),
    
    path('anime/', AnimeList, name='AnimeList'),
    path('anime/add-post', AddAPost, name='addAPost'),
    path('anime/update/<int:pk>/', AnimeUpdate, name='AnimeUpdate'),
    path('anime/delete/<int:pk>/', AnimeDeleteView.as_view(), name='AnimeDelete'),
    
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'index.html')),
    path('signup/', signup),
    path('profile/', profile, name='profile'),
    path('profile/update/', pfp)



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)