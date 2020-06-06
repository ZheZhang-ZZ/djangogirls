from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

Post.objects.all()
User.objects.all()
me = User.objects.get(username='zz33286108')

Post.objects.create(author=me, title='Sample title', text='Test') #创建文章1

Post.objects.create(author=me, title='An article about learning python',
text='Life is short, so I learn Python') #创建文章2

Post.objects.create(author=me, title='A very lucky day', text='Today is \
  Saturday, June 6th, meaning that today is 666 day. Hahaha') #创建文章3

Post.objects.create(author=me, title='I have a dream', 
text='I hope that I can be very rich') #创建文章4

Post.objects.filter(title__contains='title') #筛选标题中包含title字符串的文章

Post.objects.filter(published_date__lte=timezone.now()) #获取过去所有通过python终端发布的文章

post = Post.objects.get(title="Sample title") #把这篇文章发布



