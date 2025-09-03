import flet as ft

def main(page: ft.Page):
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Olá, mundo Flet python", size=30, weight="bold"),
            ),
            expand=True,
        ),
        ft.Image(
            src="ferrari.jpg",
            fit=ft.ImageFit.CONTAIN,
            error_content=ft.Text("Não foi possível carregar a imagem"),
            width=500
            
        ),
    )

ft.app(target=main)
