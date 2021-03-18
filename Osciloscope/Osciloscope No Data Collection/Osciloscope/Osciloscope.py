import random as R
import math as M
from graphics import *
import tkinter as TK
import time as T

def Trunkate(value):
    if int(value) == value:
        return value
    elif int(value) <(int(value)+.5):
        return M.floor(value)
    elif int(value) >=(int(value)+.5):
        return M.ceiling(value)

class DataPoint:
    def __init__(self, Time, Volt, xscale, yscale, win, XAXIS):
        self.Time = Time
        self.Volt = Volt
        self.win = win
        self.XAXIS = XAXIS
        self.X = Trunkate(float(self.Time)*xscale)
        self.Y = self.win.getHeight() -Trunkate(float(self.Volt)*yscale+(500-XAXIS))

        self.Point = Point(self.X,self.Y )
        
    def getPoint(self):
        return self.Point

    def plotPoint(self):
        self.Point.setOutline("green")
        self.Point.draw(self.win)
    
def generateNumbers(Final, dt):
    t = 0
    Tau =1
    Vo = 10
    f=.5
    w=2*M.pi*f

    Time = []
    Voltage = []
    while(t<=Final):
        V=0
        #if t != 0:
            #V  = 2*M.sin(1/t)+M.cos(1/t)+.5*t
        x = R.uniform (0,.02)
        #V = Vo*M.exp(-t/Tau)
        V = M.sin(t)
        
        
        #V=(Vo*M.sin(w*t))+3
        Time.append(t)
        Voltage.append(R.uniform(V-x, V+x))
        t=t+dt
    return Voltage, Time


def main():
    L = 1000
    W = 500
    Final = float(input("How many seconds do you want the reading to go to? "))
    dt = float(input("How many seconds do you want to increment? "))
    Vd = float(input("How many volts per line division? "))
    Td = float(input("How many seconds per line division? "))
    win = GraphWin("Osiloscope", L, W)
    Data = []
    j=0
    GV = 0
    LV = 0
   
    Voltage, Time = generateNumbers(Final, dt)
    for i in Voltage:
        if i <=LV:
            LV = i
        if i >= GV:
            GV = i
        
    if LV >0:
        LV = 0
    Vtot = M.fabs(GV) + M.fabs(LV)
    XAxis = (GV*(W)/Vtot)

    for i in Time:
        Data.append(DataPoint(i,Voltage[j], L/Final, W/Vtot, win, XAxis))
        j= j +1
    for i in Data:

        i.plotPoint()

    i = 0
    while (i <= int (GV)+2):
        TestLine = Line (Point(0, -i*(W/Vtot)+ XAxis), Point(L, -i*(W/Vtot)+ XAxis))
        if i == 0:
            TestLine.setOutline("blue")
        TestLine.draw(win)
        i = i +Vd
    i = 0
    while (i >= int (LV)-2):
        TestLine = Line (Point(0, -i*(W/Vtot)+ XAxis), Point(L, -i*(W/Vtot)+ XAxis))
        if i == 0:
            TestLine.setOutline("blue")
        TestLine.draw(win)
        i = i -Vd
    i = 0
    while(i <= Final):
        TestLine = Line (Point(i*200, 0), Point(i*200, W))
        TestLine.draw(win)
        i = i +Td
    for i in range(len(Data)):
        if i + 1 >=len (Data):
            break
        PLine = Line(Data[i].getPoint(), Data[i+1].getPoint())
        PLine.setOutline("green")
        PLine.draw(win)
    
    win.getMouse()
    win.getMouse()
main()