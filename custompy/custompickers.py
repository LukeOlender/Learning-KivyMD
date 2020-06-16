from kivymd.uix.picker import MDDatePicker, MDTimePicker, MDThemePicker
from kivy.metrics import dp


class CustomPickers:
    def open_date_picker(self):
        picker = MDDatePicker(callback=self.on_date)
        picker.open()

    def on_date(self, date):
        # 'date' is a datetime object
        print(date)

    def open_time_picker(self):
        picker = MDTimePicker()
        picker.bind(time=self.on_time)
        picker.open()

    def on_time(self, instance, time):
        # 'time'is a datetime object
        print(time)

    def open_theme_picker(self):
        picker = MDThemePicker()
        picker.open()