from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    print(fulltext)
    counting=len(fulltext.split())
    worddict={}
    for word in fulltext.split():
        if(word in worddict):
            worddict[word]+=1
        else:
            worddict[word]=1
    sortedword = sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':counting,'worddict':sortedword})
def maxword(request):
    return render(request,'about.html')
    '''fulltxt=request.GET['fulltext']
    lines=fulltxt.split("\n")
    print(fulltxt)
    for line in lines:
        counting=len(line.split())
        worddict={}
        for word in line.split():
            if(word in worddict):
                worddict[word]+=1
            else:
                worddict[word]=1
        sortedword = sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
        print(worddict)
    return render(request,'maxwordperline.html',{'line':line,'count':counting,'worddict':sortedword})'''
        
            

