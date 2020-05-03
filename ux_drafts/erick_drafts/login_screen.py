"""
Project iAdvogado

Description:
drawing a login screen.

Author:
Erick Medeiros Anastácio
2020/05/01
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# set window size
Window.size = (320, 420)


class MainWindow(BoxLayout):
    """
    The window definitions.
    Comming from main.kv file.
    """


class MainApp(App):
    """The real thing."""


    def build(self):
        """Required build for app."""
        return MainWindow()


if __name__ == '__main__':
    app = MainApp()
    app.run()
