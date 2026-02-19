from django.shortcuts import render

def index(request):
    result = None

    if request.method == "POST":
        son1 = float(request.POST.get("son1"))
        son2 = float(request.POST.get("son2"))
        amal = request.POST.get("amal")

        if amal == "+":
            result = son1 + son2
        elif amal == "-":
            result = son1 - son2
        elif amal == "*":
            result = son1 * son2
        elif amal == "/":
            if son2 != 0:
                result = son1 / son2
            else:
                result = "0 ga bo‘lish mumkin emas"

    return render(request, "index.html", {"result": result})
