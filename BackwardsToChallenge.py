#!/usr/bin/env python
# encoding: utf-8
'''
@author: 黄龙士
@license: (C) Copyright 2019-2021,China.
@contact: iym070010@163.com
@software: xxxxxxx
@file: BackwardsToChallenge.py
@time: 2020/1/4 21:00
@desc:
'''
import record as rc
import tkinter as tk
import time

class mainmenu(object):
    def __init__(self):
        self.rec = rc.Recorder()
        self.begin = 0
        self.fina = 0

        self.top=tk.Tk()
        self.top.title('My Window')
        sw = self.top.winfo_screenwidth()
        # 得到屏幕宽度
        sh = self.top.winfo_screenheight()
        # 得到屏幕高度
        ww = 200
        wh = 200
        # 窗口宽高为100
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.top.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        self.label = tk.Label(self.top, text="倒放挑战!", bg='green', fg='white', font=('Arial', 12), width=30, height=2)
        self.record = tk.Button(self.top, text="录  音", command=self.recoding)
        self.quit = tk.Button(self.top, text="停  止", command=self.quit)
        self.back = tk.Button(self.top, text="倒  放", command=self.backing)
        self.play = tk.Button(self.top, text="播  放", command=self.playing)
        self.label.pack(side = tk.TOP)
        self.record.pack(side = tk.TOP)
        self.quit.pack(side=tk.TOP)
        self.back.pack(side = tk.LEFT)
        self.play.pack(side = tk.RIGHT)

        self.top.mainloop()


    def recoding(self):
        self.rec.start()
        self.begin = time.time()
        print("Start recording")

    def quit(self):
        self.rec.stop()
        self.fina = time.time()
        t = self.fina - self.begin
        print('录音时间为%ds' % t)
        self.rec.record("C:\\Users\\62473\\Desktop\\normal.wav")

    def backing(self):
        self.rec.back("C:\\Users\\62473\\Desktop\\back.wav")

    def playing(self):
        self.rec.play()

if __name__ == "__main__":
    a = mainmenu()