from datetime import datetime
class dEntry:

    #starts day counter
    num_days = 0

    def __init__(self, wakeup_time, oob_time, slp_ql, wtb_time, dtasks, dream):

        #increments day counter
        dEntry.num_days += 1

        #assigns total num of days to instance
        self.num_day = dEntry.num_days

        #get current date
        self.date = datetime.today().strftime('%Y-%m-%d')

        #when I woke up
        self.wakeup_time = wakeup_time

        #went I got out of bed
        self.oob_time = oob_time
        self.slp_ql = slp_ql

        #when I went to bed
        self.wtb_time = wtb_time

        #list of tasks completed per day
        self.dream = dream
        self.dtasks = dtasks


    def show_todays_stats(self):
        print(self.date + " Stats")
        print("Wakeup time: " + self.wakeup_time)
        print("Out of bed @: " + self.oob_time)
        print("Went to bed @: " + self.wtb_time)
        print("Everything done today: " + self.dtasks)
        print("Day " + str(self.num_day) + " of stats completed" + "\n")


#today_stats = dEntry("6:30 am", '0', '0', '0', '0')
#tomorrow_stats = dEntry("6:30 am", '0', '0', '0', '0')
#today_stats.show_todays_stats()
#tomorrow_stats.show_todays_stats()