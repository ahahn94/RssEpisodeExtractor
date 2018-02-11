# This program will collect all links to episodes in a paged rss feed.
# It will also work on feeds without pagination.
# This program is published under the terms of the GNU GPL Version 2.
# Copyright ahahn94 2018
import os
import threading

import gi

from reelib import functions
from reelib.functions import get_redirect

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject


class GUI:

    def __init__(self):
        """
        Main program
        """
        # Init data objects.
        self.feed_url = ""
        self.pages = []
        self.links = []
        self.thread = None
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
        self.switch_follow_links = go("switch_follow_links")
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
        # Init feed_url, pages and links
        self.feed_url = self.entry_url.get_text()
        self.pages = []
        self.links = []
        # Update ui.
        self.image_done.hide()
        self.label_status.set_text("Status: Loading pages, please wait...")
        self.label_status.show()
        self.spinner_status.show()
        self.update_output_callback("")
        # Load pages.
        self.thread = PageWorker(self)
        self.thread.start()

    def pages_loaded_callback(self):
        """
        Callback method.
        """
        # Update ui.
        self.label_status.set_text("Status: All pages loaded. Processing...")
        # Process links.
        self.thread = LinkWorker(self)
        self.thread.start()

    def follow_links_callback(self):
        """
        Callback method.
        """
        self.label_status.set_text("Status: Links loaded. Following redirects...")
        self.thread = RedirectWorker(self)
        self.thread.start()

    def all_done_callback(self):
        """
        Callback method.
        """
        # Update ui and show links.
        self.spinner_status.hide()
        self.label_status.set_text("Status: All done!")
        self.image_done.show()

    def update_output_callback(self, text):
        textbuffer = self.textview_output.get_buffer()
        textbuffer.set_text(text)


class PageWorker(threading.Thread):
    """
    Thread to prevent the gui from freezing while loading pages.
    """

    def __init__(self, parent_gui):
        """
        Constructor.
        :param parent_gui: GUI.
        """
        threading.Thread.__init__(self)
        self.gui = parent_gui

    def run(self):
        """
        Run thread.
        """
        del self.gui.pages[:]
        self.gui.pages.extend(functions.get_pages(self.gui.feed_url))
        GObject.idle_add(self.gui.pages_loaded_callback)
        return


class LinkWorker(threading.Thread):
    """
    Thread to prevent the gui from freezing while processing links.
    """

    def __init__(self, parent_gui):
        """
        Constructor.
        :param parent_gui: GUI.
        """
        threading.Thread.__init__(self)
        self.gui = parent_gui

    def run(self):
        """
        Run thread.
        """
        del self.gui.links[:]  # Avoid crashes when first processing a small feed and than a huge feed.
        for page in self.gui.pages:
            self.gui.links.extend(functions.get_links(page))
        if (self.gui.switch_follow_links.get_active()):
            # Skip output if following links is selected.
            GObject.idle_add(self.gui.follow_links_callback)
            return
        else:
            # Generate output and call all_done_callback.
            links_string = ""
            for link in self.gui.links:
                links_string = links_string.__add__(link + "\n")
                GObject.idle_add(self.gui.update_output_callback, links_string)
            GObject.idle_add(self.gui.all_done_callback)
            return


class RedirectWorker(threading.Thread):
    """
    Thread to prevent the gui from freezing while processing redirects.
    """

    def __init__(self, parent_gui):
        """
        Constructor.
        :param parent_gui: GUI.
        """
        threading.Thread.__init__(self)
        self.gui = parent_gui

    def run(self):
        """
        Run thread.
        """
        links_string = ""
        for link in self.gui.links:
            redirect = get_redirect(link)
            links_string = links_string.__add__(redirect + "\n")
            GObject.idle_add(self.gui.update_output_callback, links_string)
        GObject.idle_add(self.gui.all_done_callback)
        return


gui = GUI()
