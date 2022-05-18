from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import resimcekmee

Window.clearcolor = ("#add8e6")

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass #resimcekmee.Program()

class FourWindow(Screen):
    pass

class FiveWindow(Screen):
    pass

class SixWindow(Screen):
    pass

class SWindow(Screen):
    pass

class NWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
class MyMainApp(App):
    def build(self):
        self.title="GİRİŞ FORMU"
        return kv

if __name__ == "__main__":
    MyMainApp().run()
    resimcekmee.Program().run()



