#!/usr/bin/python

from gi.repository import Gtk
import sys


class GUI:
    def __init__(self):

        self.window = Gtk.Window()
        self.window.set_title ("Hola Mundo")
        self.window.connect('destroy', self.destroy)
        button = Gtk.Button(label="Clickame!")
        button.connect("clicked", self.on_button_clicked)
        self.window.add(button)
        self.window.show_all()

    def destroy(self,window):
        Gtk.main_quit()
    def on_button_clicked(self, widget):
        print "Hola Mundo"

def main():
    app = GUI()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())