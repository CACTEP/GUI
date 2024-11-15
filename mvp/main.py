import flet as ft
import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
from plot import Plot
from flet_value import *

matplotlib.use("svg")
fig, ax = plt.subplots()
vision_plot = MatplotlibChart(fig, expand=True, original_size=False, transparent=False, isolated=True)


def main(page: ft.Page):
    page.scroll = "adaptive"
    page.window.height = 768
    page.window.width = 1024
    is_polar = False
    x = (1, 10, 1)
    f = "x*x"
    plot = Plot()

    def add_plot_clicked(e: ft.ControlEvent):
        if (value_x_start.value != "" and value_x_stop.value != "" and
                value_x_step.value != "" and value_func.value != ""):
            nonlocal x
            x = (float(value_x_start.value), float(value_x_stop.value), float(value_x_step.value))
            nonlocal f
            f = str(value_func.value)
            plot.add_plot(x, f)
            status_field.value = plot.add_plot(x, f)
            page.update()
        else:
            status_field.value = "Не все поля заполнены, данные не отправлены. Нужно ввести значения!"
            page.update()

    def coordinate_system_radiogroup_changed(e: ft.ControlEvent):
        nonlocal is_polar
        if e.data == "cartesian":
            is_polar = False
        elif e.data == "polar":
            is_polar = True
        else:
            print(e.__repr__())
        status_field.value = f"Выбрана система координат: {e.data}"
        page.update()

    def show_plot_clicked(e: ft.ControlEvent):
        if is_polar:
            plot.get_fig_p(vision_plot.figure)
        else:
            plot.get_fig_c(vision_plot.figure)
        vision_plot.update()
        status_field.value = "Построено отображение графика(ов)"
        page.update()

    def drop_plot_clicked(e: ft.ControlEvent):
        plot.drop_plots()
        vision_plot.figure.clf()
        vision_plot.update()
        status_field.value = "Все данные графиков удалены, отображение деактивировано"
        page.update()

    def save_file_result(e: ft.FilePickerResultEvent):
        filename = e.path if e.path else "Cancelled!"
        if filename != "Cancelled!":
            plot.save_plots(vision_plot.figure, filename)
            '''
            # встроенная во flet реализация не поднимается
            save_file_dialog.save_file(file_name="New plot.png", file_type=ft.FilePickerFileType.CUSTOM,
                                       allowed_extensions=["png"])
            '''
            status_field.value = f"График сохранен: '{str(filename)}'"
        else:
            status_field.value = f"Ошибка сохранения: '{str(filename)}'"
        page.update()

    save_file_dialog = ft.FilePicker(on_result=save_file_result)
    page.overlay.extend([save_file_dialog])

    nav_rail = ft.Container(
        content=ft.Column([
            values_container,
            ft.ElevatedButton(text="Отправить данные", on_click=add_plot_clicked, disabled=False),
            ft.Divider(),
            ft.RadioGroup(content=ft.Column([
                ft.Radio(value="cartesian", label="Декартова система координат"),
                ft.Radio(value="polar", label="Полярная система координат")]),
                on_change=coordinate_system_radiogroup_changed),
            ft.FilledButton(text="Отобразить график(и)", on_click=show_plot_clicked),
            ft.FilledTonalButton(text="Сбросить график", on_click=drop_plot_clicked),
            ft.FilledTonalButton(text="Сохранить в PNG",
                                 on_click=lambda _: save_file_dialog.save_file(), disabled=page.web),
        ])
    )

    content_area = ft.Container(
        content=vision_plot,
        margin=1,
        padding=1,
        alignment=ft.alignment.top_left,
        width=500,
        height=500,
        border_radius=1
    )

    status_field = ft.TextField(value="Здесь отображается статус последнего действия", read_only=True, expand=True)

    page.add(
        ft.Row([
            ft.Column([
                nav_rail,
            ]),
            ft.Column([
                content_area,
                status_field,
            ]),
        ])
    )
    page.theme = ft.Theme(color_scheme_seed="orange")
    page.update()


ft.app(target=main)
