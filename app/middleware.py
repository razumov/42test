from models import Request


class RequestProcessor:
    def process_request(self, request):
<<<<<<< HEAD
        Request.objects.create(request=request)
        return None
=======
        data = {}
        data['Path'] = request.path
        data['Method'] = request.method
        data['Meta'] = str(request.META)
        req = Request(request=data)
        req.save()
        return None

>>>>>>> t3_middleware
