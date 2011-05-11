from models import Request


class RequestProcessor:
    def process_request(self, request):
        Request.objects.create(request=request)
        return None
