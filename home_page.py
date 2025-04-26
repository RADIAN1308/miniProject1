# home.py
import flet as ft
from app import analyze_page

def main(page: ft.Page):
    page.title = "CityFix - Home"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212"

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.Text("Welcome to CityFix", size=28, weight=ft.FontWeight.BOLD),
                        ft.Text("Classify potholes by severity using AI!", size=18),
                        ft.ElevatedButton("Analyze roads", icon=ft.Icons.SEARCH,
                                          on_click=lambda e: page.go("/analyze")),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER
                )
            )
        elif page.route == "/analyze":
            analyze_page(page)

        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
