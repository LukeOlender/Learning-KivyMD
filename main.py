from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.card import MDCardSwipe
from kivy.lang import Builder
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivy.clock import Clock
from kivy.utils import platform


from custompy.customdialogs import CustomDialogs
from custompy.custompickers import CustomPickers


class StarterScreen(MDScreen):
    pass


class MDTextFieldsScreen(MDScreen):
    pass


class MDButtonsScreen(MDScreen):
    pass


class MDToastScreen(MDScreen):
    pass


class MDDialogsScreen(MDScreen):
    pass


class MDChipsScreen(MDScreen):
    pass


class MDPickersScreen(MDScreen):
    pass


class MDSwitchesScreen(MDScreen):
    pass


class MDMenuScreen(MDScreen):
    pass


class MDCardScreen(MDScreen):
    pass


class MDCardSwipeScreen(MDScreen):
    pass


class MDExpansionPanelScreen(MDScreen):
    pass


class MDBottomNavigationScreen(MDScreen):
    pass


class MDBottomSheetScreen(MDScreen):
    pass


class MDProgressBarScreen(MDScreen):
    pass


class MDSliderScreen(MDScreen):
    pass


class MDSpinnerScreen(MDScreen):
    pass


class MDSnackbarScreen(MDScreen):
    pass


class SwipeToDeleteItem(MDCardSwipe):
    """Card with `swipe-to-delete` behavior."""

    text = StringProperty()


class DrawerContent(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class CustomToolbar(
    ThemableBehavior, RectangularElevationBehavior, MDBoxLayout,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color


class ExpansionPanelContent(MDBoxLayout):
    pass


class MainDemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Green'
        return Builder.load_file('main.kv')

    def on_bottom_navigation(self):
        # Without this, the bottom bar is positioned weird
        self.root.ids.MD_bottom_navigation_screen.ids.bottom_navigation.on_resize()

    def on_start(self):
        self.root.ids.nav_drawer.swipe_distance = 100
        self.custom_dialogs = CustomDialogs()
        self.custom_pickers = CustomPickers()

        # Set up the menus for the menu screen
        menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        self.menu_1 = MDDropdownMenu(
            caller=self.root.ids.MD_menu_screen.ids.button_1, items=menu_items, width_mult=4, position='center')
        self.menu_2 = MDDropdownMenu(
            caller=self.root.ids.MD_menu_screen.ids.custom_toolbar.ids.button_2, items=menu_items, width_mult=4)

        # Set up the swipe cards for card screen
        for i in range(10):
            self.root.ids.MD_card_swipe_screen.ids.MD_card_swipe_demo.add_widget(SwipeToDeleteItem(text=f'Item {i}'))
            self.root.ids.MD_expansion_panel_screen.ids.box.add_widget(
                MDExpansionPanel(
                    icon=r'kivymd/images/kivymd_logo.png',
                    content=ExpansionPanelContent(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text="Text",
                        secondary_text="Secondary text",
                        tertiary_text="Tertiary text",
                    )
                )
            )

        # Update the current toolbar
        current_screen = self.root.ids.screen_manager.current
        toolbar = self.root.ids[current_screen].ids.toolbar
        toolbar.left_action_items = [
            ['menu', lambda x: self.root.ids.nav_drawer.set_state('toggle')]]

        # If on ios, do this to display the ad banner
        if platform == 'ios':
            from pyobjus import autoclass
            self.banner_ad = autoclass('adSwitch').alloc().init()

    def show_banner(self):
        # Show ads
        self.banner_ad.show_ads()

    def hide_banner(self):
        # Hide ads
        self.banner_ad.hide_ads()

    def change_screen(self, screen_name, text):
        screen_manager = self.root.ids.screen_manager
        screen_manager.current = screen_name
        if screen_name != 'MD_menu_screen':
            self.update_toolbar(screen_name, text)

    def update_toolbar(self, screen_name, text):
        # Update the current active toolbar
        toolbar = self.root.ids[screen_name].ids.toolbar
        toolbar.left_action_items = [
            ['menu', lambda x: self.root.ids.nav_drawer.set_state('toggle')]]
        toolbar.title = text

    def toast(self, instance, value):
        toast(value)
        print('Maybe hide ad banner')

    def remove_item(self, instance):
        self.root.ids.MD_card_swipe_screen.ids.MD_card_swipe_demo.remove_widget(instance)

    def show_share_bottom_sheet(self):
        share_sheet = MDGridBottomSheet(radius_from='top_left')
        share_sheet.bind(on_dismiss=lambda *args: print('Hide banner ad'),
                         on_open=lambda *args: print('Show banner ad'))
        data = {
            "Facebook": "facebook-box",
            "YouTube": "youtube",
            "Twitter": "twitter-box",
            "iCloud": "cloud-upload",
            "WhatsApp": "whatsapp",
        }
        for item in data.items():
            share_sheet.add_item(
                text=item[0],
                callback=lambda x, y=item[0]: self.toast(x, y),
                icon_src=item[1]
            )

        share_sheet.open()

    def animate_progressbar(self):

        def set_progress_back(*args):
            # Sets bar back to 0
            self.root.ids.MD_progress_bar_screen.ids.progressbar.value = 0

        def update(*args):
            # Update bar by one 150th until 100
            pb = self.root.ids.MD_progress_bar_screen.ids.progressbar.value
            if pb >= 100:
                Clock.schedule_once(set_progress_back, 1)
                return False
            self.root.ids.MD_progress_bar_screen.ids.progressbar.value += 100/150

        set_progress_back()

        try:
            self.progress.cancel()
        except AttributeError:
            pass

        self.progress = Clock.schedule_interval(update, 0)

    def show_spinner(self):

        def spinner_done(interval):
            self.root.ids.MD_spinner_screen.ids.spinner.active = False
            toast('Done!')

        self.root.ids.MD_spinner_screen.ids.spinner.active = True

        try:
            self.spinner.cancel()
        except AttributeError:
            pass

        self.spinner = Clock.schedule_once(spinner_done, 3)


if __name__ == '__main__':
    MainDemoApp().run()
