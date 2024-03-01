from django.http import HttpResponseForbidden

from main.models import IPAddresses


class IPRestrictedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        client_ip = request.META.get('REMOTE_ADDR')
        print(client_ip)

        ip_addresses = IPAddresses.objects.values_list('ip', flat=True)
        print(ip_addresses)
        if client_ip not in ip_addresses and 'admin' in request.path:
            return HttpResponseForbidden('Permission denied for you!')

        return self.get_response(request)
