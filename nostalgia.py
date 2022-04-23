import webbrowser
import random
from tkinter import *

from sympy import capture

window = Tk()
window.title('Nostalgia Generator')
window.geometry('600x400+50+50')

zoobooks = "https://www.youtube.com/watch?v=S8EvnM2XUTI"
zoopals = "https://www.youtube.com/watch?v=FncC-sn_VFk"
chia = "https://www.youtube.com/watch?v=tzY7qQFij_M"
toothtunes = "https://www.youtube.com/watch?v=sHL2-YzHuKc"
pillowpets = "https://www.youtube.com/watch?v=eVJ-Lt6Atfs"
fushighi = "https://www.youtube.com/watch?v=myIR__htBgc"
floam = "https://www.youtube.com/watch?v=OwiAbiGP0xA"
empire = "https://www.youtube.com/watch?v=uwJQQux0TF0"
danimals = "https://www.youtube.com/watch?v=zK1tueX3QVM"
bendaroos = "https://www.youtube.com/watch?v=0L0UAyEy6hs"
pot = "https://www.youtube.com/watch?v=Rh8GbPnoqCI"
jets = "https://www.youtube.com/watch?v=G_VtQPYq8kI"
bk = "https://www.youtube.com/watch?v=xu_bE7g2wqM"
doodle = "https://www.youtube.com/watch?v=JQVfsY0-ZR0"
caprison = "https://www.youtube.com/watch?v=tEx5gXI2DZM"
pops = "https://www.youtube.com/watch?v=2t5dGplliwg"
chef = "https://www.youtube.com/watch?v=6rTzaDEk9Bo"
education = "https://www.youtube.com/watch?v=WYS5NtRXlZQ"
kid = "https://www.youtube.com/watch?v=3xTgluQk-i8"
heel = "https://www.youtube.com/watch?v=nMFSWnghig0"
blendy = "https://www.youtube.com/watch?v=_EnRzHOx6OY"
sand = "https://www.youtube.com/watch?v=03602TWAiWA&t=8s"

links = []

links.append(zoobooks)
links.append(zoopals)
links.append(chia)
links.append(toothtunes)
links.append(pillowpets)
links.append(fushighi)
links.append(floam)
links.append(empire)
links.append(danimals)
links.append(bendaroos)
links.append(pot)
links.append(jets)
links.append(bk)
links.append(doodle)
links.append(caprison)
links.append(pops)
links.append(chef)
links.append(education)
links.append(kid)
links.append(heel)
links.append(blendy)
links.append(sand)

def openweb():
    webbrowser.open(random.choice(links))

menu = Button(window, text = "Nostalgia", command = openweb)
menu.place(x=300, y=200)

window.mainloop()