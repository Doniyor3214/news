from django.shortcuts import render, redirect
from .forms import NewsForm, CategoryForm, CommentForm, UserForm, Comment, LoginForm, UserEditForm, PasswordForm
from .models import News, Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def Logout(request):
    logout(request)
    messages.info(request, 'Siz muvaffaqiyatli log out bo\'ldiz!')
    return redirect('index')

    

def delete(request, id): 
    News.objects.get(id=id).delete()
    return redirect('index')



def index(request):
    news = News.objects.all()

    if request.POST:
        news_id = request.POST['one']
        one_news = News.objects.get(id=news_id)
        print(one_news)
        if request.user in one_news.likes.all():
            one_news.likes.remove(request.user)
        else:
            one_news.likes.add(request.user)    
   
    return render(request, "index.html", {"news": news})


def CreateCategory(request):
    form = CategoryForm()

    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            name = category.name
            messages.info(request, f'Siz  muvaffaqiyatli "{name}" bolimini yaratdiz !')
        return redirect('index')
    return render(request, 'create_category.html', {'form': form})


def Login(request):       
    login_form = LoginForm()
    if request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():           
           username = login_form.cleaned_data['username']
           password = login_form.cleaned_data['password']
           user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Siz , {user.username}, login qilindiz !")
        return redirect('index')
    return render(request, 'login.html', {'form': login_form})        

# def css(request):
#     blackground_image = 'static/pictures.jpg'
#     return render(request, 'css.html', {'blackground_image': blackground_image})
 

        
def user_register(request):

    form = UserForm()

    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            parol = form.cleaned_data['password']
            user.set_password(parol)
            user.save()
            return redirect('index')
    return render(request, 'register.html', {'form': form})    

def createNews(request):
    form = NewsForm()

    if request.POST:
        form = NewsForm(request.POST, files=request.FILES)
        if form.is_valid():
            News.objects.create(
                author = request.user,
                title = form.cleaned_data['title'],
                text = form.cleaned_data['text'],
                tur = form.cleaned_data['tur'],
                rasm = form.cleaned_data['rasm']
                    )   
            return redirect('index')
    return render(request, 'create_news.html', {'form': form})    

def editnews(request,id):
    edit_news =News.objects.get(id=id)
    form = NewsForm(instance=edit_news)
    if request.method =='POST':
        form=NewsForm(request.POST, files=request.FILES, instance=edit_news)
        if form.is_valid():
            edit_news.title=form.cleaned_data['title']
            edit_news.text=form.cleaned_data['text']
            edit_news.tur=form.cleaned_data['tur']
            edit_news.rasm=form.cleaned_data['rasm']
            edit_news.save()
            return redirect('detail', edit_news.id)         
    return render(request, 'edit.html', {'form':form})

def user_edit(request):
    form = UserEditForm(instance=request.user)
    if request.POST:
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'register.html', {'form': form})

def password_edit(request):
    form =PasswordForm()
    if request.POST:
        form =PasswordForm(request.POST)
        p_1 = form.data['password_1']
        p_2 = form.data['password_2'] 
        user = request.user
        if user.check_password(p_1):
            user.set_password(p_2)
            user.save()
            return redirect('index')
    return render(request, 'register.html', {'form':form})



def detail(request,id):
    f = News.objects.get(id=id)
    f.views+=1
    f.save()
    form=CommentForm()
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                izoh=form.cleaned_data['izoh'],
                user=request.user,
                news=f
                )
        return redirect('detail', f.id)
    return render(request, 'one.html', {'yangilik': f, 'form': form })


def createComment(request, id):
    a= News.objects.get(id=id)
    form = CommentForm()
    if request.POST:
        if not request.user.is_authenticated:
            return redirect('login')
        form=CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                izoh =form.cleaned_data['izoh'],
                user=request.user,
                news=a
            )
                          
        return redirect('detail', a.id)
    return render(request, 'one.html', {'one':a, 'form': form})    


def delete_comment(request,id):
    Comment.objects.get(id=id)
    if request.POST:
        Comment.delete()
        return render(request, 'one.html')
  





    

