from django.shortcuts import render
from django.http import HttpResponse
import string, random
from django.contrib.sites.shortcuts import get_current_site
from short.models import URL
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
# Create your views here.

def home(request):
    current_site = get_current_site(request)
    return HttpResponse("URL SHORTNER")



def shortit(long_url):
    N = 7
    s = string.ascii_uppercase + string.ascii_lowercase + string.digits
    url_id = ''.join(random.choices(s, k=N))
    
    if not URL.objects.filter(hashed=url_id).exists():
        create = URL.objects.create(full_url=long_url, hashed=url_id)
        return url_id
    else:
        shortit(url)

@csrf_exempt
def short_url(request):
    long_url = request.POST.get('url')
    hashed = shortit(long_url)
    current_site = get_current_site(request)
    data = {
        "success" : True,
        "id": hashed,
        "link":"http://{}/{}".format(current_site, hashed),
        "long_url": long_url
    }
    return JsonResponse(data)

def redirect(request, hash_id=None):
    hash_code = rds.get(hash_id)
    if hash_code is not None:
        return redirect(hash_code.decode('ascii'))

    if URL.objects.filter(hashed=hash_id).exists():
        url = URL.objects.get(hashed=hash_id)
        rds.set(hash_id, url.full_url)
        return redirect(url.full_url)
    else:
        return JsonResponse({"succes": False})
