# analyze.py
import flet as ft

def analyze_page(page: ft.Page):
    uploaded_images = []
    image_gallery = ft.Column(scroll=ft.ScrollMode.AUTO, spacing=10)
    upload_section = ft.Column(visible=False)

    def go_back(e):
        page.go("/")

    def toggle_upload_section(e):
        upload_section.visible = not upload_section.visible
        page.update()

    def handle_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            for f in e.files:
                upvote_count = ft.Text("0", width=30, text_align=ft.TextAlign.CENTER)
                downvote_count = ft.Text("0", width=30, text_align=ft.TextAlign.CENTER)
                comment_field = ft.TextField(label="Add a comment", expand=True)
                comments_display = ft.Column()

                def upvote_click(ev):
                    upvote_count.value = str(int(upvote_count.value) + 1)
                    page.update()

                def downvote_click(ev):
                    downvote_count.value = str(int(downvote_count.value) + 1)
                    page.update()

                def submit_comment(ev):
                    if comment_field.value.strip():
                        comments_display.controls.append(
                            ft.Text(f"💬 {comment_field.value}", italic=True)
                        )
                        comment_field.value = ""
                        page.update()

                image_card = ft.Container(
                    content=ft.Column(
                        [
                            ft.Image(src=f.path, width=200, height=200, fit=ft.ImageFit.CONTAIN),
                            ft.Text("Prediction: [placeholder result]", weight=ft.FontWeight.BOLD),
                            ft.Text("Confidence: [placeholder confidence]"),
                            ft.Row(
                                [
                                    ft.IconButton(ft.icons.THUMB_UP, on_click=upvote_click),
                                    upvote_count,
                                    ft.IconButton(ft.icons.THUMB_DOWN, on_click=downvote_click),
                                    downvote_count,
                                ],
                                alignment=ft.MainAxisAlignment.START,
                                spacing=5,
                            ),
                            ft.Row(
                                [comment_field, ft.IconButton(ft.icons.SEND, on_click=submit_comment)],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            comments_display
                        ],
                        spacing=10
                    ),
                    padding=10,
                    border=ft.border.all(1, ft.colors.GREY_600),
                    border_radius=10,
                )

                uploaded_images.append(image_card)

            image_gallery.controls = uploaded_images
            page.update()

    file_picker = ft.FilePicker(on_result=handle_file_result)
    page.overlay.append(file_picker)

    upload_section.controls = [
        ft.ElevatedButton(
            text="Pick Images",
            icon=ft.icons.UPLOAD_FILE,
            on_click=lambda _: file_picker.pick_files(allow_multiple=True)
        ),
        ft.Text("Uploaded Image Analysis:", style=ft.TextThemeStyle.TITLE_MEDIUM),
        image_gallery
    ]

    page.views.append(
        ft.View(
            "/analyze",
            controls=[
                ft.AppBar(
                    title=ft.Text("Analyze Potholes"),
                    leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=go_back),
                ),
                ft.Column(
                    controls=[
                        ft.Text("Pothole Severity Classification", size=24, weight=ft.FontWeight.W_600),
                        ft.Text("Upload road images to analyze severity automatically."),
                        ft.TextButton("📂 Show/Hide Image Upload", on_click=toggle_upload_section),
                        upload_section
                    ],
                    expand=True,
                    spacing=20,
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
    )
