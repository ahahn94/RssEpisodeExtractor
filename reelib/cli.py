# This program will collect all links to episodes in a paged rss feed.
# It will also work on feeds without pagination.
# This program is published under the terms of the GNU GPL Version 2.
# Copyright ahahn94 2018

import sys

from reelib import functions


def main(feed_url):
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
        print(link)


# Run the main program.
feedUrl = ""
if len(sys.argv) > 1:
    feedUrl = sys.argv[1]
else:
    feedUrl = input("Please enter the feed url: ")
main(feedUrl)
