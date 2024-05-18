import flet as ft
import random

def main(page: ft.Page):
    page.window_bgcolor = ft.colors.WHITE
    page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    contenedores_matriz = []

    def generar_matriz(e):
        n = int(tam_matriz.value)
        for i in range(n):
            contenedores_filas = []
            for j in range(n):
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
        page.update()

    def llenar_random(e):
        for control in contenedores_matriz:
            if isinstance(control, ft.Row):
                for txt in control.controls:
                    if isinstance(txt, ft.TextField):
                        txt.value = str(random.randint(1, 8))
        contenedor_matriz.controls = contenedores_matriz
        page.update()

    def eliminar_clicked(e):
        contenedores_matriz.clear()
        contenedor_matriz.controls = []
        boton_m.disabled = False
        boton_random_container.visible = False
        boton_eliminar_cont.visible = False
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


    contenedor_matriz = ft.Column()
    contenedor_todo = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
    column = ft.Column(alignment=ft.MainAxisAlignment.CENTER)

    column.controls = [tam_matriz, 
                       boton_m, boton_random_container, 
                       boton_eliminar_cont]
    contenedor_todo.controls = [column, 
                    contenedor_matriz]

    page.add(
        contenedor_todo,
    )

ft.app(target=main)