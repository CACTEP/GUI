import flet as ft


value_x_start = ft.TextField(label="Стартовое значение Х",
                             input_filter=ft.InputFilter(regex_string=r"^[\-]?\d*[\.]?\d*$"),
                             error_text="Допустимо: '-0.123456789'",
                             max_length=20)
value_x_stop = ft.TextField(label="Конечное значение Х",
                            input_filter=ft.InputFilter(regex_string=r"^\d*[\.]?\d*$"),
                            error_text="Допустимо: '0.123456789'",
                            max_length=20)
value_x_step = ft.TextField(label="Шаг итерации для Х",
                            input_filter=ft.InputFilter(regex_string=r"^\d*[\.]?\d*$"),
                            error_text="Допустимо: '0.123456789'",
                            max_length=20)
value_func = ft.TextField(label="Формула зависимости У от Х", bgcolor=ft.colors.BLUE_GREY_900,
                          # input_filter=ft.InputFilter(regex_string=r"^[\-]?\d*[\.]?\d*$"),
                          helper_text="Допустимо: 'x+-*/0.123456789'",
                          max_length=20)

values_container = ft.Container(
    content=ft.Column([
        ft.Text(value="Определение функции графика"),
        value_x_start,
        value_x_stop,
        value_x_step,
        ft.Divider(data="divider", color=ft.colors.AMBER_500),
        value_func,
    ])
)
