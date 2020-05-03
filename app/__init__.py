"""
Project iAdvogado

Description:
init file for app module

Author:
Erick Medeiros Anastácio
2020/05/03
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from app.screens import MainWindow


class MainApp(App):
    """The real thing."""

    def build(self):
        """Required build for app."""
        return MainWindow()
