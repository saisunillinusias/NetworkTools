import tkinter as tk
from tkinter import *
import webbrowser
import os
import netifaces

root=Tk()
root.title("Linus NETWORK Tools")
root.iconphoto(False, tk.PhotoImage(file='./admin.png'))


def open():
    gws = netifaces.gateways()
    gatewayss = gws['default'][netifaces.AF_INET][0]
    webbrowser.open_new(gatewayss)
def info():
    s='https://download.glasswire.com/GlassWireSetup.exe'
    webbrowser.open_new(s)
    

def ang():
    sa='https://angryip.org/download/#windows'
    webbrowser.open_new(sa)
  

def ncs():
    nc='https://arcai.com/downloads/'
    webbrowser.open_new(nc)
   

def speed():
    nc='https://www.speedtest.net/'
    webbrowser.open_new(nc)    
 

def infonet():
    os.system("ncpa.cpl")
   


def getc():
    nc='https://www.google.com/intl/en_in/chrome/'
    webbrowser.open_new(nc)    

def pack():
    nc='https://www.netacad.com/courses/packet-tracer'
    webbrowser.open_new(nc)
Button(root,text="Go To Network Admin Main Page",width=50,command=open).pack()
Button(root,text="Network",width=50,command=infonet).pack()
Button(root,text="Speed Test",width=50,command=speed).pack()
Button(root,text="Glass App",width=50,command=info).pack()
Button(root,text="Ip scaner",width=50,command=ang).pack()
Button(root,text="Net Cut",width=50,command=ncs).pack()
Button(root,text="Get chrome",width=50,command=getc).pack()
Button(root,text="cisco App",width=50,command=pack).pack()
Label(root,text="Ⓒ CopyRight to saisunil.s").pack()

root.mainloop()