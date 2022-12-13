from django.shortcuts import render, redirect
from django.utils import timezone
from .models import member
# def sbihomepage(request):
#     return render(request, "index.html", {})
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        member_name = request.POST.get('member_name')
        member_email = request.POST.get('member_email')
        member_cellphone = request.POST.get('member_cellphone')
        regdate = timezone.now()
        response = {}
        if member_name == '' or member_cellphone == '':
            response['error'] = '가입정보를 확인하세요.'
        else:
            print('dddddddd')
            response['error'] = '회원가입이 정상등록되었습니다.'
            en=member(member_name=member_name, member_email=member_email, member_cellphone=member_cellphone, regdate=regdate)
            en.save()
        return render(request, 'index.html', response)
        #return redirect('sbihome')
        # return HttpResponseRedirect(reverse('sbihome:index'))
    # else:
    #     return render(request, 'index.html')

def saveEnquery(request):
    if request.method == 'POST':
        member_name = request.POST.get('member_name')
        member_email = request.POST.get('member_email')
        member_cellphone = request.POST.get('member_cellphone')
        regdate = timezone.now()
        print('dddddddd')
        en=member(member_name=member_name, member_email=member_email, member_cellphone=member_cellphone)
        en.save()
        return render(request, 'index.html')
        #return redirect('sbihome')
        # return HttpResponseRedirect(reverse('sbihome:index'))
    else:
        return render(request, 'index.html')

# def saveEnquery(request):
#     if request.method == 'POST':
#         member_name = request.POST.get('member_name')
#         member_email = request.POST.get('member_email')
#         member_cellphone = request.POST.get('member_cellphone')
#         regdate = timezone.now()
#         print('dddddddd')
#         en=member(member_name=member_name, member_email=member_email, member_cellphone=member_cellphone)
#         en.save()
#         # return render(request, 'sbihome', context={'text': member_name})
#         #return redirect('sbihome')
#         return HttpResponseRedirect(reverse('sbihome:index'))
#     else:
#         return render(request, 'index.html')


# def post(request):
#     if request.method == 'POST':
#         post = member()
#         post.member_name = request.POST['member_name']
#         post.member_email = request.POST['member_email']
#         post.member_cellphone = request.POST['member_cellphone']
#         post.regdate = timezone.now()
#         post.save()
#         return redirect('sbihomepage')
#     return redirect('sbihomepage')

