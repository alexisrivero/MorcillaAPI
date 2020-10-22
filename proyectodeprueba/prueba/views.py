from django.views import generic
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Pizza
from .models import Cocinero
from datetime import datetime

# Create your views here.


def indice(request):
    return HttpResponse("toma chorizo")


def obtener_cualquier_pizza(request):
    pass


def obtener_pizza(request, pizza_id):
    nombre_pizza = ""
    try:
        p = Pizza.objects.get(pk=pizza_id)
        nombre_pizza = p.nombre
        respuesta = "la pizza que querias es la " + nombre_pizza
    except Pizza.DoesNotExist:
        respuesta = "no existe esa pizza broder"
    return HttpResponse(respuesta)


def obtener_todas_las_pizza(request):
    pizzas = Pizza.objects.all()
    contexto = {
        "pizza_list": pizzas,
        "chorizos": "yes",
    }
    return render(request, 'prueba/index.html', contexto)


class PizzaView(generic.ListView):
    template_name = "prueba/index.html"
    context_object_name = "pizza_list"

    def get_queryset(self):
        return Pizza.objects.all()


class PizzaDetalleView(generic.DetailView):
    model = Pizza
    template_name = "prueba/detalle.html"

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except (ValueError,  Pizza.DoesNotExist) as e:
            self.object = None
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


def obtener_cocinero(request, cocinero_id):
    nombre_cocinero = ""
    try:
        c = Cocinero.objects.get(pk=cocinero_id)
        nombre_cocinero = c.nombre
        respuesta = "tu cocinero es " + nombre_cocinero
    except Cocinero.DoesNotExist:
        respuesta = "ese boliviano no trabaja aca "
    return HttpResponse(respuesta)


def obtener_todos_los_cocinero(request):
    cocinero = Cocinero.objects.all()
    contexto = {
        "cocinero_list": cocinero,
        "quesito": "yes",
    }
    return render(request, 'prueba/cocinero.html', contexto)


class CocineroView(generic.ListView):
    template_name = "prueba/cocinero.html"
    context_object_name = "cocinero_list"

    def get_queryset(self):
        return Cocinero.object.all()


class CocineroDetalleView(generic.DetailView):
    model = Cocinero
    template_name = "prueba/detalle_cocinero.html"
