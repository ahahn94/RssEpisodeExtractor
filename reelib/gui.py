# This program will collect all links to episodes in a paged rss feed.
# It will also work on feeds without pagination.
# This program is published under the terms of the GNU GPL Version 2.
# Copyright ahahn94 2018
import os
import threading

import gi

from reelib import functions

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject


class GUI:

    def __init__(self):
        """
        Main program
        """
        # Create builder and load gui file.
        builder = Gtk.Builder()
        my_dir = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(my_dir, "gui.glade")
        builder.add_from_file(my_file)
        go = builder.get_object
        # Bind gui elements to objects.
        self.window = go("window")
        self.entry_url = go("entry_url")
        self.button_load = go("button_load")
        self.label_status = go("label_status")
        self.spinner_status = go("spinner_status")
        self.image_done = go("image_done")
        self.textview_output = go("textview_output")
        # Setup gui.
        self.label_status.set_text("Status: Ready")
        self.spinner_status.hide()
        self.window.set_title("RSS Episode Extractor")
        # Connect slots.
        self.button_load.connect("clicked", self.button_load_clicked)
        self.entry_url.connect("activate", self.button_load_clicked)
        # Show gui.
        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show()
        Gtk.main()

    def button_load_clicked(self, widget):
        """
        Run when button_load is clicked.
        :param widget: button_load.
        """
        # Init feed_url and pages
        self.feed_url = self.entry_url.get_text()
        self.pages = []
        del self.pages[:]
        # Update ui.
        self.image_done.hide()
        self.label_status.set_text("Status: Loading pages, please wait...")
        self.label_status.show()
        self.spinner_status.show()
        # Load pages.
        self.thread = PageWorker(self.pages_loaded_callback, self)
        self.thread.start()

    def pages_loaded_callback(self):
        """
        Callback method.
        """
        # Update ui.
        self.label_status.set_text("Status: All pages loaded. Processing...")
        # Process links.
        self.thread = LinkWorker(self.links_loaded_callback, self)
        self.thread.start()

    def links_loaded_callback(self):
        """
        Callback method.
        """
        # Update ui and show links.
        self.spinner_status.hide()
        self.label_status.set_text("Status: All done!")
        self.image_done.show()


class PageWorker(threading.Thread):
    """
    Thread to prevent the gui from freezing while loading pages.
    """

    def __init__(self, callback, gui):
        """
        Constructor.
        :param callback: Callback method.
        :param gui: GUI.
        """
        threading.Thread.__init__(self)
        self.callback = callback
        self.gui = gui

    def run(self):
        """
        Run thread.
        """
        self.gui.pages.extend(functions.get_pages(self.gui.feed_url))
        GObject.idle_add(self.callback)
        return


class LinkWorker(threading.Thread):
    """
    Thread to prevent the gui from freezing while processing links.
    """

    def __init__(self, callback, gui):
        """
        Constructor.
        :param callback: Callback method.
        :param gui: GUI.
        :param gui: GUI.
        """
        threading.Thread.__init__(self)
        self.callback = callback
        self.gui = gui

    def run(self):
        """
        Run thread.
        """
        links = []
        del links[:]  # Avoid crashes when first processing a small feed and than a huge feed.
        for page in self.gui.pages:
            links.extend(functions.get_links(page))
        links_string = ""
        for link in links:
            links_string = links_string + link + "\n"
        textbuffer = self.gui.textview_output.get_buffer()
        links_string = links_string[:-1]  # Remove last linebreak.
        textbuffer.set_text(links_string)
        GObject.idle_add(self.callback)
        return


gui = GUI()
