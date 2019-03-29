from django.http import HttpResponse
from django.shortcuts import render, render_to_response
# from django.template.context import RequestContext
from collections import Counter

def home(request):
    return HttpResponse('<h1>welcome young padawan</h1>')


def kontol(request): 
    return HttpResponse('''
    <h1><marquee>EH KONTOL</h1></marquee>
    <h1><marquee>EH KONTOL</h1></marquee>
    <h1><marquee>EH KONTOL</h1></marquee>
    <h1><marquee>EH KONTOL</h1></marquee>
    <h1><marquee>EH KONTOL</h1></marquee>
    <h1><marquee>EH KONTOL</h1></marquee>
    <h1><marquee>EH KONTOL</h1></marquee>
    <h1><marquee>EH KONTOL</h1></marquee>
    <h1><marquee>EH KONTOL</h1></marquee>
    <h1><marquee>EH KONTOL</h1></marquee>''')

def meh(request): 
    return render(request,'meh.html')

def count(request): 
    fulltext = request.GET['fulltext']
    counter = Counter(fulltext.split())
    common = counter.most_common(len(counter))
    print('\n\n\n\n', common)
    return render(request, 'count.html',{'fulltext': fulltext, 'length':len(fulltext.split()), 'common': common})

def about(request): 
    return HttpResponse('males jelasin. udah malem. hanya untuk mengikuti challenge nya dari bagian ini. yang penting ini menjelaskan ngapain aja sih ini website. <br> langsung aja  <a href="127.0.0.1:8000/meh/">ke sini bro</>')