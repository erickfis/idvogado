"""
Project iAdvogado

Description:
the main script

Author:
Erick Medeiros Anastácio
2020/04/30

"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()


if __name__ == '__main__':
    TestApp().run()
