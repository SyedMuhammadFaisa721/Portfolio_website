from django.http import HttpResponseForbidden
from .models import blockvisitor

class Ipaddressblocker:
    def __init__(self , get_response):
        self.get_response = get_response
    def __call__(self, request):
        allowed_ip= ["192.168.100.68"]
        paths      = ["/admin-login/" , "/admin/" , "/dashboard/"]

        if request.path in paths:
            user_ip = request.META.get("REMOTE_ADDR")

            if user_ip not in allowed_ip:
                blockvisitor.objects.create(
                    visitor_ip = user_ip,
                    paths       = request.path
                )
                return HttpResponseForbidden(
                    "Access Denied"
                )
        return self.get_response(request)