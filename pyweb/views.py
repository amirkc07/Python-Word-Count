from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request,'home.html')

def counts(request):
    fulltext=request.GET['fulltext']

    wordlist=fulltext.split()

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] +=1
        else:
             worddictionary[word]=1

    return render(request,'counts.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary':worddictionary})
