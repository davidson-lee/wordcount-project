from django.http import HttpResponse
from django.shortcuts import render
import operator
import re

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = list(filter(lambda x: x.isalpha(), map(lambda k: re.compile('[\W_]+').sub('', k).lower(), fulltext.split())))

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        elif word:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')