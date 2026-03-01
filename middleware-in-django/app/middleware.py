class MiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response 
        print("This initializes and runs only one time")

    def __call__(self, request):  

        # Before view
        print("This runs before view")

        response = self.get_response(request)

        # After view
        print("This runs after view")

        return response
    
class FatherMiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response 
        print("This Father initializes and runs only one time")

    def __call__(self, request):  

        # Before view
        print("Father Middleware runs before view")

        response = self.get_response(request)

        # After view
        print("Father Middleware runs after view")

        return response