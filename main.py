"""
Project iAdvogado.

Description:
The main app.

Author:
Erick Medeiros Anastácio
2020/05/03
"""

from kivy.core.window import Window
from app import MainApp

# set window size and window dpi
Window.size = (320, 645)
Window.dpi = 96

if __name__ == '__main__':
    app = MainApp()
    app.run()
