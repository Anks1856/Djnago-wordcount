from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'Home.html')

def about(request):
    return render(request,'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    # print(fulltext)

    wordrepeat = {}
    List = {}
    for word in wordlist:

        if word in wordrepeat:
            wordrepeat[word] +=1
        else:
            wordrepeat[word]=1
    for word in wordlist:
        List[word]=len(word)
    # print(List)

    bigword = sorted(List.items(), key=operator.itemgetter(1), reverse=True)

    higherwords = sorted(wordrepeat.items(),key=operator.itemgetter(1) ,reverse=True )
    params = {'count': len(wordlist), 'fulltext': fulltext, 'higherwords': higherwords,'bigword':bigword}
    return render(request,'count.html',params)