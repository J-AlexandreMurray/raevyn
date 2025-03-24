from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from database import add_world

Builder.load_file("kv/create_world.kv")

class CreateWorldScreen(Screen):
    def save_world(self):
        name = self.ids.name_input.text
        description = self.ids.description_input.text
        add_world(name, description)
        self.manager.current = "home"