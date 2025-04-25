# analyze.py
import flet as ft

def analyze_view(page: ft.Page):
    page.title = "Pothole Severity Classifier"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212"

    uploaded_image = ft.Image(width=300, height=300, fit=ft.ImageFit.CONTAIN)
    result_text = ft.Text(visible=False, size=18, weight=ft.FontWeight.BOLD)
    confidence_text = ft.Text(visible=False, size=16)

    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            uploaded_image.src = file_path
            uploaded_image.visible = True
            page.update()

    def classify_image(e):
        result_text.value = "Risk Level: HIGH"
        result_text.color = ft.colors.RED_ACCENT
        result_text.visible = True

        confidence_text.value = "Confidence Score: 91%"
        confidence_text.color = ft.colors.GREEN_ACCENT
        confidence_text.visible = True
        page.update()

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = ft.colors.WHITE
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = "#121212"
        page.update()

    def go_back(e):
        page.go("/")

    file_picker = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(file_picker)

    page.views.append(
        ft.View(
            "/analyze",
            [
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.ARROW_BACK, tooltip="Back", on_click=go_back),
                        ft.Icon(ft.icons.LOCATION_ON, color=ft.colors.BLUE_GREY_100),
                        ft.Text("Pothole Classifier", size=30, weight=ft.FontWeight.BOLD),
                        ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Swap Theme", on_click=toggle_theme),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Text("Upload a pothole image to classify its severity", size=18),
                ft.ElevatedButton(
                    "Upload Image",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: file_picker.pick_files(allow_multiple=False),
                ),
                uploaded_image,
                ft.ElevatedButton(
                    "Classify Pothole",
                    icon=ft.icons.SEARCH,
                    on_click=classify_image,
                ),
                result_text,
                confidence_text,
                ft.Divider(),
                ft.Text("Built with ❤️ using Flet and Keras", size=12, italic=True)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
