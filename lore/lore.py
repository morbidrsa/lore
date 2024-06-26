#!/usr/bin/env python3
import sys
import re
import argparse
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

BASE_URL = 'https://lore.kernel.org/all/?q='


def get_links(title):
    url = BASE_URL + urllib.parse.quote(title)
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all("a", href=True, string=re.compile(title))


def main():
    parser = argparse.ArgumentParser(
        prog='lore.py',
        description='Get Message-IDs for patches on lore.kernel.org'
        )
    parser.add_argument("title")
    args = parser.parse_args()

    links = get_links(args.title)
    for link in links:
        text = link.get_text()
        href = link.attrs['href']
        msgid = href.split('/')[0]
        print(f"{text} - {msgid}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
