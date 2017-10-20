#!/usr/bin/env python3

"""Retrieve and print words from a URL.

Usage:

    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
"""
Returns:
    A list of strings containing the words from
    the document.
"""
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    print(locals())
    return story_words

def print_items(items):
    """
    Print items one per line.

    Args:
        An iterable series of printalbe items.
    """
    for item in items:
        print(item)

def main(url):
    """
    Print each word from a text document from a URL.abs
    Args:
        url: The URL of a utf-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
