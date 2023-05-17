from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def round(x,y,z,a,b,c):
    x=int(x)
    y=int(y)
    z=int(z)
    a=int(a)
    b=int(b)
    c=int(c)
    r= (x-a)*(x-a)+(y-b)*(y-b)+(z-c)*(z-c)
    return r


def calculator(request):
    #데이터 확인
    x = request.GET.get('x')#가격
    y = request.GET.get('y')#맛
    z = request.GET.get('z')#양
    drink = request.GET.get('drink')#술
    delivery = request.GET.get('delivery')#배달
    category = request.GET.get('category')#메뉴
    

    #저장된 값.
    #ex) category 0 한식 1 일식 2중식 3양식 4치킨
    #ex) drink,delivery 0 가능 1 불가능
    menulist=[[0,0,0,0,0,0],[0,0,0,1,1,1],[99,99,99,0,0,0]
    ,[99,99,99,1,1,1],[55,55,55,0,0,0],[55,55,55,1,1,1]]
    #순서대로 가격, 맛, 양, 배달, 술, 메뉴
    menuname=[['음식점a','a설명'],['음식점b','b설명'],['음식점c','c설명'],
    ['음식점d','d설명'],['음식점e','e설명'],['음식점f','f설명'],['err','err']]
    store=''
    explan=''
    #계산
    shortlength=40000
    resultnum=6
    for i in range(len(menulist)):
        if(menulist[i][3]==int(drink) and menulist[i][4]==int(delivery)):
            if(menulist[i][5]==int(category)):
                length=round(x,y,z,menulist[i][0],menulist[i][1],menulist[i][2])
                if(shortlength>=length):
                    shortlength=length
                    resultnum=i

    store=menuname[resultnum][0]
    explan=menuname[resultnum][1]

    #응답
    return render(request,'calculator.html',{'store':store,'explan':explan})