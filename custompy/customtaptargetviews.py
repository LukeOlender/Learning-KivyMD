from kivymd.uix.taptargetview import MDTapTargetView


class CustomTapTargetViews:
    def __init__(self, app):
        self.tap_1 = MDTapTargetView(widget=app.root.ids.MD_tap_target_view_screen.ids.button1,
                                     title_text='This is an MDTapTargetView',
                                     description_text='This is the description', widget_position='left_bottom',
                                     cancelable=True)
        self.tap_2 = MDTapTargetView(widget=app.root.ids.MD_tap_target_view_screen.ids.button2,
                                     title_text='This is an MDTapTargetView',
                                     description_text='This is the description', widget_position='right_top',
                                     cancelable=True)

    def toggle_tap_1(self):
        if self.tap_1.state == 'close':
            self.tap_1.start()
            if self.tap_2.state == 'open':
                self.tap_2.stop()
        else:
            self.tap_1.stop()

    def toggle_tap_2(self):
        if self.tap_2.state == 'close':
            self.tap_2.start()
            if self.tap_1.state == 'open':
                self.tap_1.stop()
        else:
            self.tap_2.stop()
