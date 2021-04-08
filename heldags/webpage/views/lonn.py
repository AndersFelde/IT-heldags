from django.shortcuts import render
#  from webpage.models import TestModal


def lonn(request):
    dict = {}
    # setter det til false slik at den ikke loader tabellen i html, hvis brukeren ikke har skrevet noe
    if request.method == "POST":
        # betyr at brukeren har sendt inn form
        data = request.POST

        age = data.get("age")
        hours = data.get("hours")

        if not validateInput(age, hours):
            # ville ha returnPage funksjon fordi ellers ville den her bli for mye copy-paste
            return returnPage(request, dict)

        age = int(age)
        hours = int(hours)

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
