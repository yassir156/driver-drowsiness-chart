import cv2
import numpy as np

import matplotlib
matplotlib.use('WXAgg') # not sure if this is needed

from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

import wx

class VideoPanel(wx.Panel):

    def _init_(self, parent, size):
        wx.Panel._init_(self, parent, -1, size=size)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.parent = parent
        self.SetDoubleBuffered(True)
    
    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self)
        dc.Clear()
        if self.parent.bmp:
            dc.DrawBitmap(self.parent.bmp,0,0)


class MyFrame(wx.Frame):
    def _init_(self, fp):
        wx.Frame._init_(self, None)
        
        self.bmp = None
        
        self.cap = cv2.VideoCapture(fp)
        ret, frame = self.cap.read()
        h,w,c = frame.shape

        print (w,h,c)

        videopPanel = VideoPanel(self, (w,h))

        self.videotimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnUpdateVidoe, self.videotimer)
        self.videotimer.Start(1000/30.0)

        self.graph = Figure() # matplotlib figure
        plottPanel = FigureCanvas(self, -1, self.graph)
        self.ax = self.graph.add_subplot(111)

        y = frame.mean(axis=0).mean(axis=1)
        self.line, = self.ax.plot(y)
        self.ax.set_xlim([0,w])
        self.ax.set_ylim([0,255])

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(videopPanel)
        sizer.Add(plottPanel)
        self.SetSizer(sizer)

        self.Fit()
        self.Show(True)


    def OnUpdateVidoe(self, event):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_buf = wx.ImageFromBuffer(frame.shape[1], frame.shape[0], frame)
            self.bmp = wx.BitmapFromImage(img_buf)

            # modify this part to update every 10 sec etc...
            # right now, it's realtime update (every frame)
            y = frame.mean(axis=0).mean(axis=1)
            self.line.set_ydata(y)
            self.graph.canvas.draw()

        self.Refresh()


if _name_ == '_main_':

    fp = "Jenny Mayhem and The Fuzz Orchestrator - Gypsy Gentleman (Live at the Lodge on Queen).mp4"
    app = wx.App(0)
    myframe = MyFrame(fp)
    app.MainLoop()