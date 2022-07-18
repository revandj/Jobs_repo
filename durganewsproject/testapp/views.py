from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def movie_view(request):
    head_msg='DURGA MOVIE NEWS'
    m1='OTT is result of covid'
    m2='OTT is result of covid'
    m3='OTT is result of covid'
    m4='OTT is result of covid'
    m5='OTT is result of covid'
    type='movies'
    my_dict={'head_msg':head_msg,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'type':type}
    return render(request,'testapp/news.html',my_dict)
def sports_view(request):
    head_msg='DURGA SPORTS NEWS'
    m1='OTT is result of covid'
    m2='OTT is result of covid'
    m3='OTT is result of covid'
    m4='OTT is result of covid'
    m5='OTT is result of covid'
    type='sports'
    my_dict={'head_msg':head_msg,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'type':type}
    return render(request,'testapp/news.html',my_dict)
def politics_view(request):
    head_msg='DURGA POLITICS NEWS'
    m1='OTT is result of covid'
    m2='OTT is result of covid'
    m3='OTT is result of covid'
    m4='OTT is result of covid'
    m5='OTT is result of covid'
    type='politics'
    my_dict={'head_msg':head_msg,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'type':type}
    return render(request,'testapp/news.html',my_dict)
