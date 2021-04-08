from django.shortcuts import render
#  from webpage.models import TestModal


def lonn(request):
    dict = {"sent": False}
    if request.method == "POST":
        data = request.POST

        age = data.get("age")
        hours = data.get("hours")

        if not validateInput(age, hours):
            return returnPage(request, dict)

        pay = getHourPay(age)

        dict["hourPay"] = pay
        dict["weekPay"] = pay * hours
        dict["monthPay"] = dict["weekPay"] * 4

        return returnPage(request, dict)
    else:
        return returnPage(request, dict)


def returnPage(request, dict):
    return render(request, "webpage/lonn.html", context=dict)


def getHourPay(age):
    if age <= 15:
        return 60
    else:
        return 80


def validateInput(age, hours):
    try:
        int(age)
        int(hours)
        return True
    except Exception as e:
        return False
