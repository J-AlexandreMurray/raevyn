# app/screens/import_screen.py
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from app.utils.parser import parse_txt
from kivy.metrics import dp
import os

class ImportScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.close_file_manager,
            select_path=self.load_file,
            preview=True
        )

        self.text_input = TextInput(
            hint_text="Paste your text or load a .txt file",
            size_hint_y=None,
            height=dp(300),
            multiline=True
        )

        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=20)
        layout.add_widget(MDLabel(text="Import Text", halign="center", font_style="H5"))
        layout.add_widget(self.text_input)
        layout.add_widget(MDRaisedButton(text="Open .txt File", on_release=self.open_file_manager))
        layout.add_widget(MDRaisedButton(text="Next", on_release=self.goto_preview))

        scroll = ScrollView()
        scroll.add_widget(layout)
        self.add_widget(scroll)

    def open_file_manager(self, *args):
        self.file_manager.show(os.path.expanduser("~"))

    def close_file_manager(self, *args):
        self.file_manager.close()

    def load_file(self, path):
        if path.endswith('.txt'):
            text = parse_txt(path)
            self.text_input.text = text
            toast("Loaded text file successfully!")
        else:
            toast("Only .txt files are supported in this version.")
        self.close_file_manager()

    def goto_preview(self, *args):
        self.manager.get_screen('preview').load_text(self.text_input.text)
        self.manager.current = 'preview'
