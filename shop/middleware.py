import time

class RequestTimingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time
        path = request.path
        method = request.method
        print(f"⏱ {method} {path} so‘rovi {duration:.2f} sekundda bajarildi.")

        return response
