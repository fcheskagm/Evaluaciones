import flet as ft

def main(page: ft.Page):
    page.window_bgcolor = ft.colors.WHITE
    page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def generar_matriz(e):
        n = int(tam_matriz.value)
        contenedores_matriz = []
        for i in range(n):
            contenedores_filas = []
            for j in range(n):
                txt = ft.TextField(width=50, color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,)
                contenedores_filas.append(txt)
            contenedores_matriz.append(
                ft.Row(controls=contenedores_filas))
        page.update()
        contenedor_matriz.controls = contenedores_matriz
        page.update()
        row.controls = [contenedor_matriz]

    tam_matriz = ft.TextField(label="Ingresar (n):", width=100, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER,)
    boton_m = ft.ElevatedButton("Generar", on_click=generar_matriz)
    contenedor_matriz = ft.Column()
    row = ft.Row(alignment=ft.MainAxisAlignment.CENTER)

    page.add(
        tam_matriz,
        boton_m,
        row,
    )

ft.app(target=main)