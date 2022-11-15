from django.shortcuts import redirect
from django.urls import reverse

from .serializers import *


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def post_view(request, slug):
    post = News.objects.get(slug=slug)

    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        post.news_views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        post.news_views.add(Ip.objects.get(ip=ip))
    return redirect(reverse('post', slug))
