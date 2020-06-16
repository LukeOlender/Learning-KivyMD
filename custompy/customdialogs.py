from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder


class CustomDialogs(MDDialog):
    Builder.load_file(f'kv/customdialogcontent.kv')

    def open_alert_dialog(self):
        d = MDDialog(title='This is the title', text='This is informative text', buttons=[
                     MDFlatButton(text='CANCEL', on_release=lambda *args: d.dismiss()),
                     MDFlatButton(text='OK', on_release=lambda *args: d.dismiss())],
                     size_hint=(.8, .5), auto_dismiss=False)
        d.open()

    def open_simple_dialog(self):
        d = MDDialog(title='Something went wrong', type='simple', radius=[20, 7, 20, 7], size_hint=(.8, .5),
                     buttons = [MDFlatButton(text='Too Bad', on_release=lambda *args: d.dismiss())])
        d.open()

    def open_confirmation_dialog(self):
        d = MDDialog(title='Confirm?', type='confirmation', buttons=[
                     MDFlatButton(text='CANCEL', on_release=lambda *args: d.dismiss()),
                     MDFlatButton(text='OK', on_release=lambda *args: d.dismiss())],
                     size_hint=(.8, .5), auto_dismiss=False)
        d.open()

    def open_custom_dialog(self):
        d = MDDialog(type='custom', content_cls=CustomDialogContent(), buttons=[
                     MDFlatButton(text='CANCEL', on_release=lambda *args: d.dismiss()),
                     MDFlatButton(text='OK', on_release=lambda *args: d.dismiss())],
                     size_hint_x=.7, auto_dismiss=False)
        d.open()


class CustomDialogContent(MDBoxLayout):
    pass
