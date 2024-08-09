from django.urls import path
from . import views

app_name = 'posts' # アプリケーション内で使用する名前を定義する

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # トップページのURLパターンと対応するビュー
    path('create/', views.CreateView.as_view(), name='create'),
]