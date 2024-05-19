from interfaz1 import conversiones_page_init
from interfaz2 import resolucion_page_init
import flet as ft

def main(page: ft.Page):
    page.window_bgcolor = ft.colors.WHITE
    page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def open_conversiones(e):
        page.clean() 
        conversiones_page_init(page) 
        print("Abriendo interfaz de conversiones")

    def open_resolucion(e):
        page.clean() 
        resolucion_page_init(page) 
        print("Abriendo interfaz de gauss-jordan")

    conversiones_button = ft.ElevatedButton("Conversiones", 
                                            on_click=open_conversiones,
                                            bgcolor='#923fe5',
                                            color='white',
                                            scale=2
                                            )
    resolucion_button = ft.ElevatedButton("Gauss-Jordan", 
                                            on_click=open_resolucion,
                                            bgcolor='#923fe5',
                                            color='white',
                                            scale=2
                                            )
    titulo = ft.Container(content=ft.Text(
                            "Seleccione el programa a ejecutar",
                            size=50,
                            color=ft.colors.BLACK,
                            weight=ft.FontWeight.NORMAL,),
                            alignment=ft.alignment.center,
                            )

    column = ft.Column(alignment=ft.MainAxisAlignment.CENTER, width=70, height=70)
    

    page.add(titulo, column, conversiones_button, column, resolucion_button)

while True:
    ft.app(target=main)
