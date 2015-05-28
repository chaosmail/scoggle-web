def host(request):
    url = 'https://' if request.is_secure() else 'http://'
    url += request.get_host()
    return {'host': url}