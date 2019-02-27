from rest_framework.views import APIView
from django.shortcuts import render_to_response
import time
import decimal


def fibonacci(n):
    try:
        s5 = decimal.Decimal(5).sqrt()
        return int(((1+s5)**n-(1-s5)**n)/(2**n*s5))
    except Exception as e:
        return str(e)


class FibonacciView(APIView):
    def get(self, request):
        return render_to_response("get_number.html")

    def post(self, request):
        num = int(request.data["fibonacci_no"])
        if num < 0:
            return render_to_response("fibonacci_series.html", context={"data": "Please enter a positive number.",
                                                                        "num": num})
        start = time.perf_counter()
        fib = fibonacci(num)
        end = time.perf_counter() - start

        return render_to_response("fibonacci_series.html", context={"data": fib, "time": '{:f}'.format(end),
                                                                    "num": num})

