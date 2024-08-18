from kivy.uix.boxlayout import BoxLayout
from backend.data_manager import add_entry

class MainScreen(BoxLayout):
    def add_activity(self):
        date = self.ids.date_input.text
        activity = self.ids.activity_input.text
        hours = self.ids.hours_input.text
        earnings = self.ids.earnings_input.text
        add_entry(date, activity, hours, earnings)
