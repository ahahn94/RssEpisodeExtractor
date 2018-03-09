# Part of RssEpisodeExtractor.
# This program is published under the terms of the GNU GPL Version 2.
# Copyright ahahn94 2018

def get_help_cli():
    help_text = "RssEpisodeExtractor\n" \
                "Copyright ahahn94 2018\n" \
                "This program is licensed under the GNU GPL v2\n\n" \
                "Just run rssepisodeextractor link_to_feed and the links will be printed to the cli.\n\n" \
                "If you run rssepisodeextractor you will be asked for your url.\n\n" \
                "To follow links in case of redirection, use rssepisodeextractor -redirect link_to_feed.\n" \
                "This is much slower than just grabbing the feeds links, so please be patient.\n\n" \
                "If you want to download the files directly from the cli, run rssepisodeextractor yourfeedurl | xargs wget.\n" \
                "Be aware that this can take some time, depending on the number of episodes and the connection speed.\n\n" \
                "Depending on your internet connection speed and the feed size, it may take a while until you get some output."
    return help_text

def get_help_gui():
    help_text = "RssEpisodeExtractor\n" \
                "Copyright ahahn94 2018\n" \
                "This program is licensed under the GNU GPL v2\n\n" \
                "Just paste the feeds URL into the first textfield and click on \"Load Links\".\n\n" \
                "If you want to follow the links in case of redirection, check the \"Follow Links\" checkbox. " \
                "This can be realy slow, depending on the connection speed and the number of redirects.\n" \
                "The links will each be written to the lower textfield as soon as they are ready, " \
                "so just wait for the first link to appear if there seems to be no progress."
    return help_text
