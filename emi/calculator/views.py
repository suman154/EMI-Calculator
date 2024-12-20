from django.shortcuts import render
from django.http import JsonResponse
import math
# Create your views here.


def emi_calculator(request):
    if request.method == "POST":
        try:
            loan_amount = float(request.POST.get("loan_amount", 0))
            loan_rate = float(request.POST.get("loan_rate", 0))
            loan_tenure = int(request.POST.get("loan_tenure", 0))
            tenure_type = request.POST.get("tenure_type", "Months")

            if tenure_type == "Years":
                loan_tenure *= 12  # Convert years to months

            monthly_rate = loan_rate / (12 * 100)  # Annual rate to monthly rate
            emi = (loan_amount * monthly_rate * math.pow(1 + monthly_rate, loan_tenure)) / (math.pow(1 + monthly_rate, loan_tenure) - 1)
            total_payment = emi * loan_tenure
            total_interest = total_payment - loan_amount

            return JsonResponse({
                "emi": round(emi, 2),
                "total_interest": round(total_interest, 2),
                "total_payment": round(total_payment, 2),
            })
        except Exception as e:
            return JsonResponse({"error": str(e)})
    return render(request, "calculator/emi_calculator.html")
