from django.shortcuts import render
from random import randint
#  from webpage.models import TestModal

switchDict = {True: "mange kast", False: "ett kast"}


def throwDices(times):
    throws = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for _ in range(times):
        throw = randint(1, 6)
        throws[throw] += 1

    return throws


def terningkast(request):
    throws = False
    #  for at den skal være definert, slipper å lage render() to ganger

    if request.method == "POST":
        data = request.POST
        if data.get("switchMode") == "True":
            request.session["terningkast"] = not request.session["terningkast"]
        elif data.get("throwDices") == "True":
            times = int(data.get("amountDices"))
            throws = throwDices(times)

    if request.session.get("terningkast") == None:
        #  gjelder hvis det er første gangen brukeren er på siden, da er ikke den satt
        request.session["terningkast"] = True

    return render(request,
                  "webpage/terningkast.html",
                  context={
                      "terningkastState": request.session["terningkast"],
                      "switch": switchDict[request.session.get("terningkast")],
                      "throws": throws
                  })
