from funciones2 import GaussJordan
import flet as ft
import numpy as np
import random


def main(page: ft.Page):
    page.window_bgcolor = ft.colors.WHITE
    page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    contenedores_matriz = []
    solucion = []
    gj = GaussJordan()

    def generar_matriz(e):
        n = int(tam_matriz.value)
        for i in range(n):
            contenedores_filas = []
            for j in range(n+1):
                txt = ft.TextField(width=50, 
                                   color=ft.colors.BLACK,
                                   text_align=ft.TextAlign.CENTER,)
                contenedores_filas.append(txt)
            contenedores_matriz.append(
                ft.Row(controls=contenedores_filas))
        page.update()
        contenedor_matriz.controls = contenedores_matriz
        page.update()
        boton_random_container.visible = True
        boton_m.disabled = True
        boton_eliminar_cont.visible = True
        boton_resolver_cont.visible = True
        page.update()

    def obtener_datos():
        matriz_datos = []
        for control in contenedores_matriz:
            if isinstance(control, ft.Row):
                fila = []
                for txt in control.controls:
                    if isinstance(txt, ft.TextField):
                        fila.append(float(txt.value))
                matriz_datos.append(fila)
        print(matriz_datos)
        return matriz_datos

    def resolver(e):
        matriz_datos = []
        matriz_datos = obtener_datos()
        global solucion
        solucion = []
        gj.set_matriz(matriz_datos)
        solucion = gj.resolver_m()
        fila_res = ft.Row(spacing=10, alignment=ft.MainAxisAlignment.CENTER)

        for i, value in enumerate(solucion, start=1):
            text = ft.Text(f"X{i} = {value}", color="black",)
            fila_res.controls.append(text)
        container_res.content = fila_res
        container_res.visible = True
        print(solucion)
        page.update()

    def llenar_random(e):
        for control in contenedores_matriz:
            if isinstance(control, ft.Row):
                for txt in control.controls:
                    if isinstance(txt, ft.TextField):
                        txt.value = str(random.randint(1, 8))
        contenedor_matriz.update()

    def eliminar_clicked(e):
        global solucion
        contenedores_matriz.clear()
        contenedor_matriz.controls = []
        solucion.clear()
        container_res.visible = False
        boton_m.disabled = False
        boton_random_container.visible = False
        boton_eliminar_cont.visible = False
        boton_resolver_cont.visible = False
        tam_matriz.value = ""
        page.update()


    
    
    tam_matriz = ft.TextField(label="Ingresar (n):", 
                              width=100, 
                              color=ft.colors.BLACK, 
                              text_align=ft.TextAlign.CENTER,)
    
    boton_m = ft.ElevatedButton("Generar", 
                                on_click=generar_matriz, 
                                disabled=False,
                                bgcolor='#923fe5',
                                color='white',)
    
    boton_random_container = ft.Container(content=ft.ElevatedButton("Random",
                                                                    bgcolor='#923fe5',
                                                                    color='white',
                                                                    on_click=llenar_random), 
                                                                visible=False)
    
    boton_eliminar_cont = ft.Container(content=ft.ElevatedButton("Eliminar",
                                                                 on_click=eliminar_clicked,
                                                                    bgcolor='#923fe5',
                                                                    color='white',
                                                                    ), 
                                                                visible=False)
    
    boton_resolver_cont = ft.Container(content=ft.ElevatedButton("Resolver",
                                                                 on_click=resolver,
                                                                    bgcolor='#923fe5',
                                                                    color='white',
                                                                    ), 
                                                                visible=False)
    
    
    column = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
    column.controls = [tam_matriz, 
                       boton_m, boton_random_container,
                       boton_resolver_cont, 
                       boton_eliminar_cont,
                       ]

    contenedor_matriz = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
    contenedor_matriz.controls = []

    container_res = ft.Container()

    column2 = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
    column2.controls = [contenedor_matriz, 
                        container_res]

    contenedor_todo = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
    contenedor_todo.controls = [column, 
                    column2]

    page.add(
        contenedor_todo,
    )

ft.app(target=main)