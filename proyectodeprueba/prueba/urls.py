from django.urls import path
from . import views

urlpatterns = [
    path('', views.indice, name='indice'),

    path('obtener_pizza/<pizza_id>/',
         views.obtener_pizza, name="obtener_pizza"),
    path('todas/', views.obtener_todas_las_pizza,
         name="obtener_todas_las_pizzas"),
    path('todes/', views.PizzaView.as_view(), name='todes las pizzas'),
    path('detalle/<pk>/', views.PizzaDetalleView.as_view(),
         name='detalle_pizzero'),
    path('obtener_cocinero/<cocinero_id>/',
         views.obtener_cocinero, name="obtener_cocinero"),
    path('cocineros/', views.obtener_todos_los_cocinero,
         name="obtener_todos_los_cocineros"),
    path('detalle_cocinero/<pk>/',
         views.CocineroDetalleView.as_view(), name='detalle cocinero'),
    path('formulario/', views.obtener_formulario, name="obtener_formulario")
]
