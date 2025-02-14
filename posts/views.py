from django.shortcuts import render,redirect
from django.views import View
from posts.models import Post
from .forms  import PostForm

class IndexView(View):
  def get(self,request,*args,**kwargs):
    posts =  Post.objects.all()  # すべてのレコードをpostsに代入
    return render(request, 'posts/index.html',{'posts':posts})
  
class CreateView(View):
  def get(self, request, *args, **kwargs):
    form = PostForm()
    return render(request, 'posts/create.html', {'form': form})
  
  def post(self, request, *args, **kwargs):
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      
    # redirectで一覧画面に移動する
    return redirect('posts:index')
