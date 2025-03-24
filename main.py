from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from worldbuilder.world_manager import WorldManager

class HomeScreen(Screen):
    pass

class CreateWorldScreen(Screen):
    pass

class RaevynApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(CreateWorldScreen(name='create_world'))
        return sm

if __name__ == '__main__':
    raevynApp().run()