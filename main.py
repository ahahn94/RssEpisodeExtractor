# This program will collect all links to episodes in a paged rss feed.
# It will also work on feeds without pagination.
# This program is published under the terms of the GNU GPL Version 2.
# Copyright ahahn94 2018

import feedparser
import sys
import urllib.request


def main(feed_url):
    """
    Main program.
    :param feed_url: URL to the feed.
    :return: none.
    """
    # Init pages, next_page.
    pages = []  # List of the feeds pages.
    next_page = feed_url  # Next page of the feed.

    first = download(next_page)

    last_page = get_last_page(first)
    next_page = get_next_page(first)
    pages.append(first)

    last_page_processed = False
    if next_page == "":  # If no next page, skip loop.
        last_page_processed = True

    while not last_page_processed:
        page = download(next_page)
        pages.append(page)
        if next_page == last_page:  # if recent page is the last page.
            last_page_processed = True
        next_page = get_next_page(page)

    for page in pages:
        print_links(page)


def download(next_page):
    """
    Download a temporary copy of a page of the feed.
    :param next_page: URL of the next page of the feed.
    :return: Next page.
    """
    request = urllib.request.urlopen(next_page)
    return request.read().decode("utf-8")


def get_last_page(page):
    """
    Get the link to the last page of the feed.
    :param page: Page to extract the URL from.
    :return: URL of the last page of the feed.
    """
    feed = feedparser.parse(page)
    for link in feed.feed.links:
        if link.rel == "last":
            return link.href


def get_next_page(page):
    """
    Get the link to the next page of the feed.
    :param page: Page to extract the URL from.
    :return: URL of the next page of the feed.
    """
    feed = feedparser.parse(page)
    for link in feed.feed.links:
        if link.rel == "next":
            return link.href
    return ""


def print_links(page):
    """
    Print links to console.
    :param page: Page to extract the links from.
    :return: none.
    """
    feed = feedparser.parse(page)
    # iterate over entries.
    for entry in feed.entries:
        # print links.
        for link in entry.enclosures:
            print(link.href)


# Run the main program.
feedUrl = ""
if len(sys.argv) > 1:
    feedUrl = sys.argv[1]
else:
    feedUrl = input("Please enter the feed url: ")
main(feedUrl)
