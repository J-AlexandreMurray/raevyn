from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from database import get_worlds

Builder.load_file("kv/view_worlds.kv")

class ViewWorldsScreen(Screen):
    def on_pre_enter(self):
        self.ids.world_list.text = "\n".join([f"{w[0]}. {w[1]} - {w[2]}" for w in get_worlds()])