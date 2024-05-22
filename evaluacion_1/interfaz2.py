from funciones2 import GaussJordan
import flet as ft
import random
import re

def resolucion_page_init(page: ft.Page):
    page.window_bgcolor = ft.colors.WHITE
    page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    contenedores_matriz = []
    solucion = []
    gj = GaussJordan()

    def on_change_textfield(e):
        error_text_cont.visible = False
        solucion = [1]
        solucion.clear()
        container_res.visible = False

    def on_change(e):
        on_change_textfield(e)
        actua_resolver_boton()

    def on_change_tam_num(e):
        tam_matriz.value = ""
        page.update()

    def generar_matriz(e):
        value = tam_matriz.value
        if tam_matriz.value == "Error":
            tam_matriz.value = "Error"
            page.update()
            return
        if not value or int(value) <= 0 or int(value) >=15:
            tam_matriz.value = "Error"
            page.update()
            return
        n = int(value)
        for i in range(n):
            contenedores_filas = []
            for j in range(n+1):
                txt = ft.TextField(width=50, 
                                color=ft.colors.BLACK,
                                text_align=ft.TextAlign.CENTER,
                                on_change=on_change,)
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
        tam_matriz.disabled = True
        actua_resolver_boton()
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
        return matriz_datos
    
    def verificar_datos():
        for control in contenedores_matriz:
            if isinstance(control, ft.Row):
                for txt in control.controls:
                    if isinstance(txt, ft.TextField):
                        value = txt.value
                        if not value or not re.match(r'^-?\d*\.?\d+$', value):
                            return False
        return True
    
    def actua_resolver_boton():
        boton_resolver_cont.visible = True
        boton_resolver_cont.disabled = not verificar_datos()
        page.update()

    def resolver(e):
        if not verificar_datos():
            return
        matriz_datos = []
        matriz_datos = obtener_datos()
        global solucion
        solucion = []
        gj.set_matriz(matriz_datos)
        try:
            solucion = gj.resolver_m()
            fila_res = ft.Column(spacing=10, 
                                 alignment=ft.MainAxisAlignment.CENTER)
            for i, value in enumerate(solucion, start=1):
                text = ft.Text(f"X{i} = {value}", color="black",)
                fila_res.controls.append(text)
            container_res.content = fila_res
            container_res.visible = True
        except ValueError as e:
            error_text_cont.visible = True
        actua_resolver_boton()
        page.update()

    def llenar_random(e):
        for control in contenedores_matriz:
            if isinstance(control, ft.Row):
                for txt in control.controls:
                    if isinstance(txt, ft.TextField):
                        txt.value = str(random.randint(-99, 99))
        contenedor_matriz.update()
        actua_resolver_boton()
        error_text_cont.visible = False
        page.update()

    def eliminar_clicked(e):
        global solucion
        solucion = [1]
        contenedores_matriz.clear()
        contenedor_matriz.controls = []
        solucion.clear()
        error_text_cont.visible = False
        container_res.visible = False
        boton_m.disabled = False
        boton_random_container.visible = False
        boton_eliminar_cont.visible = False
        boton_resolver_cont.visible = False
        tam_matriz.disabled = False
        tam_matriz.value = ""
        page.update()

    def verificar_numero(e):
        value = e.control.value
        if not value or not re.match(r'^-?\d+$', value) or int(value) <= 0:
            e.control.value = ""            
        else:
            e.control.error_text = ""

    

    titulo = ft.Container(content=ft.Text(
                            "Eliminacion Gauss-Jordan",
                            size=50,
                            color=ft.colors.BLACK,
                            weight=ft.FontWeight.NORMAL,),
                            alignment=ft.alignment.center,
                            )

    error_text_cont = ft.Container(content=ft.Text(
                            "El sistema no tiene solución", 
                            color="red"),
                        visible=False,
                        alignment=ft.alignment.center)
    
    tam_matriz = ft.TextField(label="Ingresar (n):",
                              value="", 
                              width=100, 
                              color=ft.colors.BLACK, 
                              text_align=ft.TextAlign.CENTER,
                              on_change=verificar_numero,
                              on_focus=on_change_tam_num)
    
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
                       boton_eliminar_cont,]

    contenedor_matriz = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
    contenedor_matriz.controls = []

    container_res = ft.Container()

    column2 = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
    column2.controls = [contenedor_matriz,
                        error_text_cont]

    column3 = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
    column3.controls = [container_res]

    contenedor_todo = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
    contenedor_todo.controls = [column,
                    column2,
                    column3]

    page.add(titulo, contenedor_todo)
