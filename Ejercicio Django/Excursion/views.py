from django.shortcuts import render, redirect
from .models import Elemento, SelElemento, req


# Create your views here.
def home(request):
    elemento=Elemento.objects.all()
    selemento=SelElemento.objects.all() 

    return render(request, 'aplicacion.html',{"selementos":selemento,"elementos":elemento})


def seleccionarElementos(request):
    #Calcula la eficiencia de cada elemento y lo guarda el la base de datos.
    for i in range(Elemento.objects.count()):
     gain=Elemento.objects.all()[i]
     gain.gain=gain.calorias/gain.peso
     gain.save()

    
    # Variableas auxiliares para sumar peso y calorias que se llevan.
    pes=0
    cal=0
    #Elimino la selección anterior 
    db_2=SelElemento.objects.all()
    db_2.delete()

    # Obtengo los valores de frontend por el metodo POST y los guardo.
   
    requeC=request.POST['numCalorias']
    requeP= request.POST['numPeso']
    
    
    
    # loop para seleccionar los elementos.
    for i in range(Elemento.objects.count()):
    #for i in range(2):
        if (int(requeP) > pes):
            if (int(requeC) >= cal):
                db_1=Elemento.objects.order_by('-gain')[i]
                db_2=SelElemento.objects.create(ID=db_1.ID,nombre=db_1.nombre,calorias=db_1.calorias,peso=db_1.peso)
                db_2.save()
                pes= pes+ db_1.peso
                cal= cal + db_1.calorias
            else:
                break 
        else:
            break 

    return redirect('/')

