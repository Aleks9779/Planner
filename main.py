from kivy.app import App
from kivy.lang import Builder
from frontend.widgets import MainScreen

class Planner(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    Planner().run()
