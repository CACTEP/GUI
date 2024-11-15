import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("svg")


class Plot:
    plots: list = []
    # color = random(colors)  # требуется дополнительная проработка для выбора случайных цветов

    class Subplot:
        x: np.ndarray = []
        phi: np.ndarray = []
        y: np.ndarray = []
        rho: np.ndarray = []
        func_str: str = ""
        func_label: str = ""

        def __init__(self, x: tuple, func_str: str):
            self._set_x(*x)
            self._set_func(func_str)
            self._set_y()
            self._set_phi()
            self._set_rho()

        def _set_x(self, start, stop, step):
            self.x = np.arange(start, stop, step)
            # print(self.x)

        def _set_y(self):
            x = self.x
            self.y = np.array(eval(self.func_str))
            # print(self.y)

        def _set_phi(self):
            self.phi = np.arctan2(self.y, self.x)
            # print(self.phi)

        def _set_rho(self):
            self.rho = np.sqrt(self.x**2 + self.y**2)
            # print(self.rho)

        def _set_func(self, func_str):
            if func_str:
                self.func_str = func_str
            else:
                Exception(ValueError(func_str))
            self.func_label = str("$f(x)=" + self.func_str + "$")
            # print(self.func_str)
            # print(self.func_label)

    def add_plot(self, x: tuple, func_str: str):
        if "x" not in func_str:
            return (f"В данных: '{func_str}' отсутствует зависимость от X! "
                    f"Попробуйте еще раз с допустимыми значениями!")
        for char in func_str:
            if char not in "x+-*/0.123456789":
                return (f"Данные: '{func_str}' не приняты! "
                        f"Попробуйте еще раз с допустимыми значениями для формулы зависимости У от Х!")
        self.plots.append(self.Subplot(x, func_str))
        return "Значения по У и Х успешно загружены! Можно отправить следующий набор данных!"

    def drop_plots(self):
        self.plots = []

    # '''
    # функция, которая подлежит замене на flet-встроенную: save_file_dialog.save_file
    def save_plots(self, fig: plt.Figure, filename: str):
        if isinstance(filename, str):
            fig.savefig(filename, format="png", transparent=None)
        else:
            print("Ошибка сохранения")
    # '''

    def get_fig_c(self, fig: plt.Figure):
        fig.clf()
        ax = fig.add_subplot(1, 1, 1)
        # ax = fig.add_axes((0., 0., 1., 1.,), polar=False) # альтернативный вариант - без числовой разметки
        for plot in self.plots:
            ax.plot(
                plot.x,
                plot.y,
                label=plot.func_label
            )
            ax.grid(True)
            ax.legend()

    def get_fig_p(self, fig: plt.Figure):
        fig.clf()
        ax = fig.add_axes((0., 0., 1., 1.,), polar=True)
        for plot in self.plots:
            ax.plot(
                plot.phi,
                plot.rho,
                label=plot.func_label
            )
            ax.legend()
