"""
Project iAdvogado.

Description:
init file for screens module

Author:
Erick Medeiros Anastácio
2020/05/03
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Loading Multiple .kv files
Builder.load_file('app/screens/welcome.kv')
Builder.load_file('app/screens/login.kv')
Builder.load_file('app/screens/main.kv')


class MainWindow(BoxLayout):
    """
    The window definitions.

    Comming from kv file.
    """
