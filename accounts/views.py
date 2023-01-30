from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
import re


#로그인 함수
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'good_login.html')

            #return redirect('rwordpage')
        else:
            return render(request, 'bad_login.html')
           
    else:
        return render(request, 'login.html')

#로그아웃
def logout(request):
    auth.logout(request)
    return redirect('rwordpage')

#회원가입
def signup(request):
    if request.method == "POST":
        # 이메일의 형식에 맞게 입력되었는지 확인
        if not re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$',(request.POST['username'])):
                return render(request, 'bad_signup.html')
                #return JsonResponse({'message':'INVALID_EMAIL_FORMAT'}, status=400)
        if User.objects.filter(username=request.POST['username']).exists():
                return render(request, 'bad_alreadyexist.html')
        if request.POST['password'] == request.POST['repeat']:
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, new_user)
            return redirect('rwordpage')
        else:
            #비밀번호 확인이 일치하지 않는 경우
            return render(request, 'bad_pwcheck.html')
    return render(request, 'signup.html')
