from funciones1 import Conversiones
import random
import flet as ft

def main(page: ft.Page):

    c=Conversiones()

    page.window_bgcolor = ft.colors.WHITE
    page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    original_text_field = ft.TextField(
        value="", 
        text_align=ft.TextAlign.RIGHT,
        color=ft.colors.BLACK
        )
    convertir_text_field = ft.TextField(
        value="", 
        text_align=ft.TextAlign.LEFT, 
        disabled=True, 
        bgcolor='#fbfbfb',
        color=ft.colors.BLACK,
        )
    original_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Terciario"),
            ft.dropdown.Option("Cuaternario"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Hexadecimal"),
        ],
        width=200,
        bgcolor='#923fe5',
        color='white',
    )
    convertir_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Terciario"),
            ft.dropdown.Option("Cuaternario"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Hexadecimal"),
        ],
        width=200,
        bgcolor='#923fe5',
        color='white',
    )

    def set_ori(value):
        if value == "Binario":
            c.set_binario(original_text_field.value)
        elif value == "Decimal":
            c.set_decimal(original_text_field.value)
        elif value == "Terciario":
            c.set_terciario(original_text_field.value)
        elif value == "Cuaternario":
            c.set_cuaternario(original_text_field.value)
        elif value == "Octal":
            c.set_octal(original_text_field.value)
        elif value == "Hexadecimal":
            c.set_hexadecimal(original_text_field.value)

    def get_con(value):
        if value == "Binario":
            return c.get_binario()
        elif value == "Decimal":
            return c.get_decimal()
        elif value == "Terciario":
            return c.get_terciario()
        elif value == "Cuaternario":
            return c.get_cuaternario()
        elif value == "Octal":
            return c.get_octal()
        elif value == "Hexadecimal":
            return c.get_hexadecimal()
        
    def set_borrar():
            c.set_binario()
            c.set_decimal()
            c.set_terciario()
            c.set_cuaternario()
            c.set_octal()
            c.set_hexadecimal()
    

    def boton_clicked(e):
        valor_original = original_dropdown.value
        valor_convertir = convertir_dropdown.value
        if valor_original and valor_convertir:
            if validar_valor_original(original_text_field.value, valor_original):
                set_ori(valor_original)
                c.todas_conversiones(valor_original,valor_convertir)
                convertir_text_field.value = get_con(valor_convertir)
        else:
            convertir_text_field.value = "Valor no válido"
        page.update()

    def validar_valor_original(valor, base):
        if base == "Decimal":
            return all(c in "0123456789" for c in str(valor))
        elif base == "Binario":
            return all(c in "01" for c in valor)
        elif base == "Terciario":
            return all(c in "012" for c in valor)
        elif base == "Cuaternario":
            return all(c in "0123" for c in valor)
        elif base == "Octal":
            return all(c in "01234567" for c in valor)
        elif base == "Hexadecimal":
            return all(c in "0123456789ABCDEF" for c in valor.upper())
        return False

    def random_num(value):
        if value == "Binario":
            c.set_binario("".join(str(random.randint(0, 1)) for _ in range(random.randint(3, 10))))
        elif value == "Decimal":
            c.set_decimal(random.uniform(0,10000))
        elif value == "Terciario":
            c.set_terciario("".join(str(random.randint(0, 2)) for _ in range(random.randint(3, 6))))
        elif value == "Cuaternario":
            c.set_cuaternario("".join(str(random.randint(0, 3)) for _ in range(random.randint(3, 6))))
        elif value == "Octal":
            c.set_octal("".join(str(random.randint(0, 7)) for _ in range(random.randint(3, 6))))
        elif value == "Hexadecimal":
            c.set_hexadecimal("".join(random.choice("0123456789ABCDEF") for _ in range(random.randint(3, 6))))

    def crear_container(content, **kwargs):
        return ft.Container(content=content, **kwargs)

    def eliminar_clicked(e):
        original_text_field.value = ""
        convertir_text_field.value = ""
        original_dropdown.value = ""
        convertir_dropdown.value = ""
        set_borrar()  
        page.update()

    def click_random(e):
        
        valor_original = original_dropdown.value
        random_num(valor_original)
        original_text_field.value = get_con(valor_original)
        page.update()

    page.add(
    ft.Column(
        [
            crear_container(
                ft.Text(
                    "Conversiones Numericas",
                    size=50,
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.NORMAL,
                ),
                alignment=ft.alignment.center,
            ),
            ft.Row(
                [
                    ft.Column(
                        [
                            crear_container(
                                original_dropdown, 
                                alignment=ft.alignment.center, 
                                width=400, 
                                height=100, 
                                bgcolor=ft.colors.WHITE),
                            crear_container(
                                original_text_field, 
                                alignment=ft.alignment.center, 
                                width=400, 
                                height=100, 
                                bgcolor=ft.colors.WHITE),
                            crear_container(
                                ft.ElevatedButton(
                                    "Random",
                                    icon=ft.icons.ALL_INCLUSIVE,
                                    on_click=click_random,
                                    bgcolor='#923fe5',
                                    color='white',
                                ), 
                                alignment=ft.alignment.center, 
                                width=400, 
                                height=100, 
                                bgcolor=ft.colors.WHITE),
                        ],
                        spacing=20,
                    ),
                    crear_container(
                        ft.ElevatedButton(
                        "Convertir", 
                            on_click=boton_clicked,
                            bgcolor='#923fe5',
                            color='white',
                        ),
                        alignment=ft.alignment.center, 
                        width=120, 
                        height=100, 
                        bgcolor=ft.colors.WHITE,
                    ),
                    ft.Column(
                        [
                            crear_container(
                                convertir_dropdown, 
                                alignment=ft.alignment.center, 
                                width=400, 
                                height=100, 
                                bgcolor=ft.colors.WHITE),
                            crear_container(
                                convertir_text_field, 
                                alignment=ft.alignment.center, 
                                width=400, 
                                height=100, 
                                bgcolor=ft.colors.WHITE),
                            crear_container(
                                 ft.ElevatedButton(
                                        "Eliminar", 
                                        icon=ft.icons.RESTORE_FROM_TRASH,
                                        on_click=eliminar_clicked,
                                        bgcolor='#923fe5',
                                        color='white',
                                    ),
                                    alignment=ft.alignment.center, 
                                    width=400, 
                                    height=100, 
                                    bgcolor=ft.colors.WHITE),
                        ],
                        spacing=20,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=50,
            ),
        ],
    ),
)

ft.app(target=main)