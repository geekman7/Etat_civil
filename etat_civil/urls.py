
from django.contrib import admin
from django.urls import path
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.dashboard, name='dashboard'),
    path('login/',users_views.loginPage, name='login'),
    path('register/',users_views.registerPage, name='register'),
    path('users/',users_views.userPage, name='user'),
    path('naissance/',users_views.crudNaissance, name='naissance'),
    path('ajouter_naissance/',users_views.CreateNaissance.as_view(), name='create_naissance'),
    path('profile/',users_views.createProfile.as_view(), name='profile'),
    path('historique/',users_views.historique, name='historique'),
    path('telecharger_en_pdf/',users_views.DownloadPDF.as_view(), name='download'),
    path('vision_en_pdf/',users_views.ViewPDF.as_view(), name='vision'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)