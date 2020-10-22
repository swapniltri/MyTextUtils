from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    djtext=request.POST.get('text','default')
    djtext1=djtext
    checkbox_input=request.POST.get('removepunc','off')
    extra_Space=request.POST.get('extraSpace','off')
    newLineRemove=request.POST.get('newLineRemover','off')
    countChar=request.POST.get('countChar','off')
    capitalise=request.POST.get('capitalise','off')

    punctuations='''!"#$%&'()*+,-./:;?@[\]^_`{|}~'''

    if checkbox_input=='on':
        analysed=''
        for i in djtext:
            if i not in punctuations:
                analysed=analysed+i
        djtext=analysed

    if extra_Space=='on':
        analysed=''
        for i in range(len(djtext)-1):
            if not(djtext[i]==' ' and djtext[i+1]==' '):
                analysed=analysed+djtext[i];
        djtext=analysed

    if newLineRemove=='on':
        analysed=''
        for char in djtext:
            if not(char=="\n" and char=="\r"):
                analysed=analysed+char
        djtext=analysed

    if capitalise=='on':
        analysed=''
        for char in djtext:
            analysed=analysed+char.upper()
        djtext=analysed

    params={'input_text':djtext1,'analysed_text':djtext}
    return render(request,'punctuate.html',params)