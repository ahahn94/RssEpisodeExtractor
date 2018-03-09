# Part of RssEpisodeExtractor.
# This program is published under the terms of the GNU GPL Version 2.
# Copyright ahahn94 2018
import urllib.request
import feedparser
import requests


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


def get_pages(feed_url):
    """
    Get list of pages.
    :param feed_url: URL to the feed.
    :return: List of the feeds pages.
    """
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
    return pages


def get_links(page):
    """
    Get links to episodes.
    :param page: Page to extract the links from.
    :return: List of links.
    """
    feed = feedparser.parse(page)
    links = []
    # iterate over entries.
    for entry in feed.entries:
        # print links.
        for link in entry.enclosures:
            links.append(link.href)
    return links


def get_redirect(link):
    """
    Get the url of the redirected link.
    :param link: Link to follow.
    :return: Redirected url.
    """
    response = requests.get(link)
    return response.url
