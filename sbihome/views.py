from django.shortcuts import render, redirect
from django.utils import timezone
from .models import member
import requests
import pandas as pd
import json
from src.lib import message

# def sbihomepage(request):
#     return render(request, "index.html", {})
# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
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
        return render(request, 'contact.html', response)
        #return redirect('sbihome')
        # return HttpResponseRedirect(reverse('sbihome:index'))
    # else:
    #     return render(request, 'index.html')

def sms(request):
    if request.method == 'GET':
        return render(request, 'sendsms.html')
    elif request.method == 'POST':
        send_msg = request.POST.get('sendmsg')
        response = {}
        if send_msg == '':
            response['error'] = '메세지를 확인하세요.'
        else:
            print(send_msg)
            member_type = 2
            base_id = 'appssITu2KHnI0zUO'
            table_id = 'tblLGqfVdDK7C1YH3'
            url = "https://api.airtable.com/v0/" + base_id + "/" + table_id
            params = {"maxRecords": 50}

            api_key = 'keyl1hCA8uM5W73Bl'  # ★★★API Key
            headers = {'Authorization': 'Bearer ' + api_key}

            response = requests.get(url, params=params, headers=headers)
            # 정상 select all
            airtable_response = response.json()
            airtable_records = airtable_response['records']
            if member_type == 0:
                members = airtable_records
            elif member_type == 1:  # 무료회원
                members = [x for x in airtable_records if x['fields']['Status'] == '무료']
            elif member_type == 2:  # 무료회원
                members = [x for x in airtable_records if x['fields']['Status'] == '유료']

            phonelist = []
            for p in members:
                # membeer_name  = p['fields']['이름']
                # member_phone  = p['fields']['전화번호_010']
                phonelist.append(p['fields']['전화번호_010'])
            print(phonelist)



            response['error'] = '정상 발송되었습니다.'
        return render(request, 'sendsms.html', response)


def saveEnquery(request):
    if request.method == 'POST':
        member_name = request.POST.get('member_name')
        member_email = request.POST.get('member_email')
        member_cellphone = request.POST.get('member_cellphone')
        regdate = timezone.now()
        print('dddddddd')
        en=member(member_name=member_name, member_email=member_email, member_cellphone=member_cellphone)
        en.save()
        return render(request, 'contact.html')
        #return redirect('sbihome')
        # return HttpResponseRedirect(reverse('sbihome:index'))
    else:
        return render(request, 'contact.html')

# def contact(request):
#     return render(request, 'contact.html')




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

