# This program will collect all links to episodes in a paged rss feed.
# It will also work on feeds without pagination.
# This program is published under the terms of the GNU GPL Version 2.
# Copyright ahahn94 2018

import sys

from reelib import functions


def main(feed_url, redirect):
    """
    Main program.
    :param feed_url: URL to the feed.
    :return: none.
    """
    pages = functions.get_pages(feed_url)

    links = []
    for page in pages:
        links.extend(functions.get_links(page))

    for link in links:
        if (redirect):
            print(functions.get_redirect(link))
        else:
            print(link)


# Run the main program.
feedUrl = ""
redirect = False
redirect_option_string = "--redirect"
if len(sys.argv) > 1:
    if (redirect_option_string in sys.argv):
        redirect = True
        sys.argv.remove(redirect_option_string)
    feedUrl = sys.argv[1]
else:
    feedUrl = input("Please enter the feed url: ")
main(feedUrl, redirect)
