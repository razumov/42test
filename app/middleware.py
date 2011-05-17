from models import Request


class RequestProcessor:
    def process_request(self, request):
        data = {}
        data['Path'] = request.path
        data['Method'] = request.method
        data['Meta'] = str(request.META)
        req = Request(request=data)
        req.save()
        return None

