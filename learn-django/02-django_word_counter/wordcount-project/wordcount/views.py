from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

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

def template(request): 
    return render(request,'index.html')