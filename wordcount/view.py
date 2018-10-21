from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')
def eggs(request):
    return HttpResponse('<h1>EGGS</h1>')
def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    count=0
    for word in wordlist:
        for c in word:
            count+=1
    avgnum=count/len(wordlist)
    return render(request,'count.html',{'fulltext': fulltext,'count':len(wordlist),'count1':fulltext.count("is"),'avg':avgnum,})


def result(request):
    ft=request.GET['fullt']
    return render(request,'result.html',{'rep':ft.replace('replace1','replace2')})

