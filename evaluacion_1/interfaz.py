import flet as ft

def main(page: ft.Page):
    def dropdown_changed(e):
        t.value = f"Selecciona para cambiar la opcion de {seleccion.value}"
        page.update()

    t = ft.Text()
    seleccion = ft.Dropdown(
        on_change=dropdown_changed,
        options=[
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Terciario"),
            ft.dropdown.Option("Cuaternario"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Hexadecimal"),
        ],
        width=200,
    )

    txt_number = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=400)


    page.add(t, seleccion, txt_number)

ft.app(target=main)