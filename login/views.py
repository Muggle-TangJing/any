from django.shortcuts import render,redirect
from .models import User
from . import forms

# Create your views here.
def index(request):
    return render(request,'login/index.html')

def login(request):
    # 不允许重复登录
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == 'POST':
        # username = request.POST.get('username',None)
        # password = request.POST.get('password',None)
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
        # if username and password:
        #     username = username.strip()
            try:
                user = User.objects.get(name = username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = '密码不正确'
            except:
                message = '用户名不存在'
            return render(request,'login/login.html',locals())

    login_form = forms.UserForm()
    return render(request,'login/login.html',locals())

def register(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == 'POST':
        # 实例化一个RegisterForm
        register_form = forms.RegisterFrom(request.POST)
        message = '请检查填写内容'
        if register_form.is_valid():
            # cleaned_data 就是读取表单返回的值，返回类型为字典dict型
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = '两次输入的密码不一致'
                return render(request,'login/register.html',locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已存在，换一个'
                    return render(request,'login/register.html',locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已被注册过，请使用别的邮箱'
                    return  render(request,'login/register.html',locals())
            # new_user = User()
            # new_user.name = username
            # new_user.password = password1
            # new_user.email = email
            # new_user.sex = sex
            new_user = User.objects.create(name=username, password=password1, sex=sex, email=email)
            new_user.save()
            print(new_user)
    register_form = forms.RegisterFrom()
    return render(request,'login/register.html',locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/index/')
    request.session.flush()
    return redirect('/index/')