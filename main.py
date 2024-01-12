from kivymd.app import MDApp
from kivy.lang import Builder
from datetime import datetime
#from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from entry import dEntry
import sqlite3

#Window.size = (500, 500)
#define different screens

class Content(MDBoxLayout):
    pass

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
class StatsWindow(Screen):
    pass
class MenuWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        kv = Builder.load_file('main.kv')
        self.tags = []
        # create/connect to database
        conn = sqlite3.connect("stats_db.db")
        # create cursor that will do things to/in db
        c = conn.cursor()

        c.execute("""CREATE TABLE if not exists stats(
                    date text not null primary key,
                    wakeup_time text,
                    oob_time text,
                    slp_ql text,
                    dream text,
                    wtb_time)
                """)

        conn.commit()
        conn.close()
        self.entries = {}
        self.current_date = datetime.today().strftime('%Y-%m-%d')
        self.num_days = 0
        return kv

    def make_entry(self, task):
        wakeup_time = self.root.get_screen('start').ids.input.text
        oob_time = self.root.get_screen('oob').ids.input.text
        slp_ql = self.root.get_screen('slpql').ids.input.text
        dream = self.root.get_screen('dreams').ids.input.text
        dtasks = task
        self.num_days += 1
        return dEntry(wakeup_time, oob_time, slp_ql, dream, dtasks)

    #print current date's stats
    def p_stats(self):
        print(self.current_date)
        print(self.num_days)
        daily_stats = self.entries[self.current_date]
        print(f"You woke up at: {daily_stats.wakeup_time}")
        print(f"You got out of bed at: {daily_stats.oob_time}")
        print(f"Sleep quality was: {daily_stats.slp_ql}")
        print(f"Today's dreams: {daily_stats.dream}")
        if daily_stats.dtasks:
            print(f"Today's tasks: {daily_stats.dtasks}\n")
        if daily_stats.wtb_time:
            print(f"Bedtime was: {daily_stats.wtb_time}\n")
        #print(self.entries)

    #adds tag to list of tags, prints tags
    def collect_tag(self):
        tag = self.root.get_screen('tags').ids.input.text
        if self.current_date not in self.entries:
            new_entry = self.make_entry(tag)
            self.entries[self.current_date] = new_entry
        else:
            old_entry = self.entries[self.current_date]
            old_entry.update_todays_tasks(tag)
        self.p_stats()

    #allows rentry of multiple tags
    def clear_tag_input(self):
        self.root.get_screen('tags').ids.input.text = ""

    def update_wtb_time(self):
        wtb_time = self.root.get_screen('bedtime').ids.input.text
        old_entry = self.entries[self.current_date]
        old_entry.get_wtb_time(wtb_time)

    #resets screen text inputs for next day
    def clear_inputs(self):
        self.root.get_screen('start').ids.input.text = ""
        self.root.get_screen('oob').ids.input.text = ""
        self.root.get_screen('slpql').ids.input.text = ""
        self.root.get_screen('dreams').ids.input.text = ""
        self.root.get_screen('bedtime').ids.input.text = ""

    def submit(self):
        date = datetime.today().strftime('%Y-%m-%d')
        wakeup_time = self.root.get_screen('start').ids.input.text
        oob_time = self.root.get_screen('oob').ids.input.text
        slp_ql = self.root.get_screen('slpql').ids.input.text
        dream = self.root.get_screen('dreams').ids.input.text
        wtb_time = self.root.get_screen('bedtime').ids.input.text

        # create/connect to database
        conn = sqlite3.connect("stats_db.db")
        # create cursor that will do things to/in db
        c = conn.cursor()
        #Add record
        c.execute("INSERT INTO stats (date,wakeup_time,oob_time,slp_ql,dream,wtb_time) VALUES (?, ?, ?, ?, ?, ?)", (date,wakeup_time,oob_time,slp_ql,dream,wtb_time))

        conn.commit()
        conn.close()


    def show_stats(self):
        # create/connect to database
        conn = sqlite3.connect("stats_db.db")
        # create cursor that will do things to/in db
        c = conn.cursor()

        #get stats from db
        c.execute("SELECT * FROM stats")
        records = c.fetchall()
        word = ""
        wt = ""
        oobt = ""
        slpql = ""
        drm = ""
        wtb = ""
        #loop through records
        for record in records:
            print(record)
            word = f"{word}\n{record[0]}"
            wt = f"{wt}{record[1]}"
            oobt = f"{oobt}{record[2]}"
            slpql = f"{slpql}{record[3]}"
            drm = f"{drm}{record[4]}"
            wtb = f"{wtb}{record[5]}"
            self.root.get_screen('stats').ids.stats_label.text = f"{word} stats\n Wakeup Time: {wt}\n Out of Bed Time: {oobt}\n Sleep Quality: {slpql}\n Dreamt about: {drm}\n Bedtime: {wtb}"

        conn.commit()
        conn.close()

MainApp().run()

