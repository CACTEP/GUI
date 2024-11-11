import flet as ft


class ButtonStyle:
    main_batton_color = {
        ft.ControlState.HOVERED: ft.colors.BLUE_800,
        ft.ControlState.FOCUSED: ft.colors.BLUE_600,
        ft.ControlState.DEFAULT: ft.colors.BLUE_400
    }


class MainButton(ft.FilledButton):
    def __int__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.colors.BLUE_800
        self.color = ft.colors.YELLOW_800
        self.text = text
        self.on_click = on_click


class LimitButton(ft.ElevatedButton):
    def __int__(self, text, on_click, disabled=False, limit=3):
        super().__init__()
        self.bgcolor = ft.colors.BLUE_200
        self.color = ft.colors.YELLOW_200
        self.text = text
        self.on_click = on_click
        self.disabled = disabled
        self.limit = limit  # new custom variable


class PlotButton(ft.FilledTonalButton):
    def __int__(self, text, on_click, disabled=False):
        super().__init__()
        self.bgcolor = ft.colors.BLUE_400
        self.color = ft.colors.YELLOW_400
        self.text = text
        self.on_click = on_click
        self.disabled = disabled

