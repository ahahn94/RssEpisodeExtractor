# This program will collect all links to episodes in a paged rss feed.
# It will also work on feeds without pagination.
# This program is published under the terms of the GNU GPL Version 2.
# Copyright ahahn94 2018

import feedparser
import sys
import urllib.request


# Main program
def main(feedUrl):
    # Init pages, nextPage, lastPage.
    nextPage = ""  # Link to next page of the feed.
    pages = []  # List of the feeds pages.
    nextPage = feedUrl  # Next page of the feed.
    lastPage = feedUrl  # Last page of the feed.

    first = download(nextPage)

    lastPage = getLastPage(first)
    nextPage = getNextPage(first)
    pages.append(first)

    lastPageProcessed = False
    if (nextPage == ""):  # If no next page, skip loop.
        lastPageProcessed = True

    while not lastPageProcessed:
        page = download(nextPage)
        pages.append(page)
        if (nextPage == lastPage):  # if recent page is the last page.
            lastPageProcessed = True
        nextPage = getNextPage(page)

    for page in pages:
        printLinks(page)


# Download a temporary Copy of a page of the feed.
def download(nextPage):
    request = urllib.request.urlopen(nextPage)
    return request.read().decode("utf-8")


# Get the link to the last page of the feed.
def getLastPage(page):
    feed = feedparser.parse(page)
    for link in feed.feed.links:
        if (link.rel == "last"):
            return link.href


# Get the link to the next page of the feed.
def getNextPage(page):
    feed = feedparser.parse(page)
    for link in feed.feed.links:
        if (link.rel == "next"):
            return link.href
    return ""


# Print links to console.
def printLinks(page):
    feed = feedparser.parse(page)
    # iterate over entries.
    for entry in feed.entries:
        # print links.
        for link in entry.enclosures:
            print(link.href)


# Run the main program.
feedUrl = ""
if (len(sys.argv) > 1):
    feedUrl = sys.argv[1]
else:
    feedUrl = input("Please enter the feed url: ")
main(feedUrl)
