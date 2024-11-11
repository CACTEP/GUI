#  import plotly.express as px
import plotly.graph_objects as go
import flet as ft
from flet.plotly_chart import PlotlyChart
from kaleido.scopes.plotly import PlotlyScope
scope = PlotlyScope(
    plotlyjs="https://cdn.plot.ly/plotly-latest.min.js"
    # plotlyjs="D:\Образование\МФТИ\desktop\GUI\mvp\plotly-latest.min.js"
)


def main(page: ft.Page):
    def create_plot_clicked(e: ft.ControlEvent):
        print(e.__repr__())

    def add_plot_clicked(e: ft.ControlEvent):
        print(e.__repr__())

    def save_to_clicked(e: ft.ControlEvent):
        print(e.__repr__())

    def drop_plot_clicked(e: ft.ControlEvent):
        print(e.__repr__())

    def coordinate_system_radiogroup_changed(e: ft.ControlEvent):
        coordinate_system_radiogroup_changed_text.value = f"Система координат: {e.control.value}"
        page.update()
        print(e.__repr__())
        vision_plot.update()
    coordinate_system_radiogroup_changed_text = ft.Text()

    vision_plot = ft.Placeholder()

    nav_rail = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Text(value="Определение функции графика"),
                    ft.TextField(label="Стартовое значение Х", input_filter=ft.InputFilter(regex_string=r"^[\-]?\d*[\.\,]?\d*$")),
                    ft.TextField(label="Конечное значение Х", input_filter=ft.InputFilter(regex_string=r"^[\-]?\d*[\.\,]?\d*$")),
                    ft.TextField(label="Шаг итерации для Х", input_filter=ft.InputFilter(regex_string=r"^[\-]?\d*\.\,]?\d*$")),
                    ft.Divider(data="TEST", tooltip="testtest", color=ft.colors.AMBER_500),
                    ft.TextField(label="Формула зависимости У от Х", bgcolor=ft.colors.BLUE_GREY_900, input_filter=ft.InputFilter(regex_string=r"^[\-]?\d*[\.\,]?\d*$")),
                    ft.Divider(data="TEST", tooltip="testtest", color=ft.colors.AMBER_500),
                ])
            ),
            ft.Divider(data="TEST", tooltip="testtest", color=ft.colors.PINK_200),
            ft.FilledButton(text="Построить график", on_click=create_plot_clicked),
            ft.Divider(),
            ft.ElevatedButton(text="Добавить график", on_click=add_plot_clicked, disabled=True),
        ])
    )

    content_area = ft.Container(
        content=ft.Column([
            ft.Container(
                content=vision_plot,
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=500,
                height=300,
                border_radius=10
            ),
            ft.Divider(),
            coordinate_system_radiogroup_changed_text,
            ft.Divider(),
            ft.RadioGroup(content=ft.Row([
                ft.Radio(value="cartesian", label="Декартова система координат"),
                ft.Radio(value="polar", label="Полярная система координат")]),
                on_change=coordinate_system_radiogroup_changed),
            ft.Divider(),
            ft.Row([
                ft.FilledTonalButton(text="Сохранить в PNG", on_click=save_to_clicked),
                ft.FilledTonalButton(text="Сбросить график", on_click=drop_plot_clicked),
            ])

        ])
    )

    page.add(
        ft.Row([
            nav_rail,
            content_area
        ])
    )


ft.app(target=main)