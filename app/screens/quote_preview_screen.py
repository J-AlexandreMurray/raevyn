# app/screens/quote_preview_screen.py
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView
from app.utils.formatter import extract_quotes

class QuotePreviewScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.quote_box = MDBoxLayout(orientation='vertical', padding=20, spacing=10, size_hint_y=None)
        self.quote_box.bind(minimum_height=self.quote_box.setter('height'))

        scroll = ScrollView()
        scroll.add_widget(self.quote_box)

        container = MDBoxLayout(orientation='vertical')
        container.add_widget(MDLabel(text="Quote Preview", halign="center", font_style="H5", size_hint_y=None, height=50))
        container.add_widget(scroll)
        container.add_widget(MDRaisedButton(text="Back", on_release=self.go_back, size_hint_y=None, height=50))

        self.add_widget(container)

    def load_text(self, full_text):
        self.quote_box.clear_widgets()
        quotes = extract_quotes(full_text)
        for q in quotes:
            self.quote_box.add_widget(
                MDCard(
                    MDLabel(text=q.strip(), padding=10, theme_text_color="Primary"),
                    orientation="vertical",
                    size_hint_y=None,
                    height=120,
                    padding=10,
                    ripple_behavior=True
                )
            )

    def go_back(self, *args):
        self.manager.current = 'import'
