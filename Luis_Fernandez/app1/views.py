from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
planilla=[
    {
        "Monto":10.0,
        "Tasa":10.0,
        "Plazo":10.0,
        "Cuota":10.0,
        "Total":10.0,
    },
]
def index(request):
    if(request.method=="POST"):
        Monto= int(request.POST.get('txtMonto'))
        Tasa= int(request.POST.get('txtTasa'))
        Plazo= int(request.POST.get('txtPlazo'))
        Tasatem=(Tasa/100/12)
        Cuota=round((Monto*Tasatem)/(1-(1+Tasatem)**-(Plazo*12)),2)
        Total=round((Cuota*(Plazo*12)),2)


        planilla.append({
            "Monto":Monto,
            "Tasa":Tasa,
            "Plazo":Plazo,
            "Cuota":Cuota,
            "Total":Total,
        },)

    ctx={"planilla":planilla}

    return render(request,'planilla/index.html',context=ctx )    
