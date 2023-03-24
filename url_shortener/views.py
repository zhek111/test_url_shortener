from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortenedURL


def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')
        shortened_url = ShortenedURL.custom_create(original_url)
        return render(request, 'shortened_url.html',
                      {'shortened_url': shortened_url})

    return render(request, 'index.html')


def redirect_url(request, token):
    try:
        shortened_url = get_object_or_404(ShortenedURL, short_token=token)
        shortened_url.increment_clicks()
        return redirect(shortened_url.original_url)
    except ShortenedURL.DoesNotExist:
        return render(request, '404.html', status=404)


def stats(request):
    urls = ShortenedURL.objects.all()
    return render(request, 'stats.html', {'urls': urls})
