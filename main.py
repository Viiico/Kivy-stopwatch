from os import times
import time
import math
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

class TestWidget(Widget):
    def __init__(self, **kwargs):
        super(TestWidget, self).__init__(**kwargs)

    def startTimer(self):
        if self.timer == False:
            self.timer = Clock.schedule_interval(self.increment_time, .1)
            self.increment_time(0);
    def increment_time(self, interval):
        self.time = math.floor((self.time + interval)*1000)/1000;
        self.labelCount.text = f"{self.time}"

    def getTimestamp(self):
        if self.timer != False:
            if len(self.timeStamps) >= 15:
                self.timeStamps.pop(0)
            self.timeStamps.append(f"{self.time}\n");
            self.labelStamps.text = ''.join(self.timeStamps)

    def stopTimer(self):
        if self.timer != False:
            self.timer.cancel()
            self.timer = False
    
    def resetTimer(self):
        self.stopTimer()
        if self.timer == False:
            self.time = 0
            self.labelCount.text = '00:00:00'
            self.labelStamps.text = ''
            self.timeStamps = []

Builder.load_string('''
<TestWidget>:
    labelCount: labelCount
    labelStamps: labelStamps
    timer: False
    time: 0
    timeStamps: []
    GridLayout:
        size: root.size
        cols: 2
        BoxLayout:
            orientation: 'vertical'
            Button:
                id: button1
                text: "Start timer"
                on_release: root.startTimer()
            Button:
                id: button2
                text: "Timestamp"
                on_release: root.getTimestamp()
            Button:
                id: button3
                text: "Stop timer"
                on_release: root.stopTimer()
            Button:
                id: button4
                text: "Reset Timer"
                on_release: root.resetTimer()
        GridLayout:
            row_defualt_height: 200
            row_width: sp(100)
            rows: 2
            Label:
                id: labelCount
                text: "00:00:00"
            Label:
                id: labelStamps
                text: ""
''')

class testApp(App):
    def build(self):
        return TestWidget()

if __name__ == "__main__":
    testApp().run()