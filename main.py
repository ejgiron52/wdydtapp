from kivymd.app import MDApp
from kivy.lang import Builder
from datetime import datetime
from kivy.uix.screenmanager import ScreenManager, Screen
from entry import dEntry

#define different screens

class StartWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class SlpQualWindow(Screen):
    pass
class DreamsWindow(Screen):
    pass
class TagsWindow(Screen):
    pass
class BedTimeWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        kv = Builder.load_file('main.kv')
        self.tags = []
        return kv

    def make_entry(self):
        wakeup_time = self.root.get_screen('start').ids.input.text
        oob_time = self.root.get_screen('oob').ids.input.text
        slp_ql = self.root.get_screen('slpql').ids.input.text
        dream = self.root.get_screen('dreams').ids.input.text
        dtasks = self.tags
        wtb_time = self.root.get_screen('bedtime').ids.input.text
        return dEntry(wakeup_time, oob_time, slp_ql, dream, dtasks, wtb_time)

    #print current date's stats
    def p_stats(self):
        current_date = datetime.today().strftime('%Y-%m-%d')
        print(current_date)
        daily_stats = self.make_entry()
        print(f"You woke up at: {daily_stats.wakeup_time}")
        print(f"You got out of bed at: {daily_stats.oob_time}")
        print(f"Sleep quality was: {daily_stats.slp_ql}")
        print(f"Today's dreams: {daily_stats.dream}")
        if daily_stats.dtasks:
            print(f"Today's tasks: {daily_stats.dtasks}\n")
        if daily_stats.wtb_time:
            print(f"Bedtime was: {daily_stats.wtb_time}\n")

    #adds tag to list of tags, prints tags
    def collect_tag(self):
        tag = self.root.get_screen('tags').ids.input.text
        self.tags.append(tag)
        self.p_stats()

    #allows rentry of multiple tags
    def clear_tag_input(self):
        self.root.get_screen('tags').ids.input.text = ""

    #resets screen text inputs for next day
    def clear_inputs(self):
        self.root.get_screen('start').ids.input.text = ""
        self.root.get_screen('oob').ids.input.text = ""
        self.root.get_screen('slpql').ids.input.text = ""
        self.root.get_screen('dreams').ids.input.text = ""
        self.root.get_screen('bedtime').ids.input.text = ""

MainApp().run()

