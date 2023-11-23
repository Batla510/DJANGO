from django.shortcuts import render
from django.http import HttpResponse

def res(request,name,surname,age,interes):
    text = f'<h1> Hello, i am {name} {surname}.</h1>' \
            f'<p>I am {age}</p>' \
            f'<p>I like {interes}</p>'
    return HttpResponse(text)
def about(request,place,uspev,learning):
    about = f'<h1> i am from {place}.</h1>' \
            f'<p>I am {uspev}</p>' \
            f'<p>I {learning}</p>'
    return HttpResponse(about)
def contact(request,github,tg,vk,discord):
    contact = f'<h1> My contact</h1>' \
            f'<p>Github: {github}</p>' \
            f'<p>Telegram: {tg}</p>' \
            f'<p>Vkontakte: {vk}</p>' \
            f'<p>Discord: {discord}</p>'
    return HttpResponse(contact)
