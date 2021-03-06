import asyncio

from mttkinter import mtTkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter.ttk import Notebook

from gui.PlaylistGUI import PlaylistGUI
from gui.MPVGUI import MPVGUI
from gui.RoomGUI import RoomGUI



class MainWindow():
    def __init__(self,interval=1/20):
        self.window = tk.Tk()
        self.interval = interval
        self.window.title("重生之我是欧菲手")
        self.tab_controller: Notebook = ttk.Notebook(self.window)
        self.menu_controller = Menu(self.window)
        self._initialize()

    def _initialize(self):
        self.window.resizable(False,False)
        self.window.geometry("720x480")
        self.tab_controller.pack(expand = 1,fill="both")

    def getTabController(self) -> Notebook:
        return self.tab_controller

    async def _update(self):
        while True:
            self.window.update()
            await asyncio.sleep(self.interval)

    def start(self):
        self.createWidgets()
        return self._update()

    def createWidgets(self):
        mpv = MPVGUI(self)
        room = RoomGUI(self)
        playlist = PlaylistGUI(self)
        room.createWidgets()
        playlist.createWidgets()
        mpv.createWidgets()


        mpv.initialize()
        room.initialize()
        playlist.initialize()




