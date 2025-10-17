from django.http import JsonResponse

def calculate_tax(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    elif income <= 1000000:
        return (income - 500000) * 0.2 + 12500
    else:
        return (income - 1000000) * 0.3 + 112500

def tax_calculator(request):
    income = request.GET.get('income', 100000)
    try:
        income = float(income)
    except ValueError:
        return JsonResponse({"error": "Income must be a number"})
    
    tax = calculate_tax(income)
    return JsonResponse({"income": income, "tax": tax})
