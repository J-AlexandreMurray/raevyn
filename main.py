# main.py
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from app.screens.import_screen import ImportScreen
from app.screens.quote_preview_screen import QuotePreviewScreen

class EbookSocialShareApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Light"

        sm = MDScreenManager()
        sm.add_widget(ImportScreen(name='import'))
        sm.add_widget(QuotePreviewScreen(name='preview'))
        return sm

if __name__ == '__main__':
    EbookSocialShareApp().run()
