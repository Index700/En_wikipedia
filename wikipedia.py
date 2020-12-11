#! /usr/bin/python3
# Copyright (c) 2020, Keita Kitaura
# All rights reserved.
#
# $Id: $
#
# ref: wikipedia-api
# https://github.com/martin-majlis/Wikipedia-API/

import wikipediaapi
import sys
from perlcompat import getopts

def print_sections(sections, level=0):
        for s in sections:
                print("%s %s - %s" % ("*" * (level + 1), s.title, s.text))
                print_sections(s.sections, level + 1)


def main():
    opt = getopts('asw:') or usage()
    all_page = opt.a
    section_page = opt.s
    word = opt.w if opt.w else "python3"
    # word = sys.argv[1]
    
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    p_wiki = wiki_wiki.page(word)

    if not p_wiki.exists():
        print(f"'{word}' does not exists in the Wikipedia.")
        return 0

    if all_page:
        print(p_wiki.text)
        print("a")
    elif section_page:
        print_sections(p_wiki.sections)
        print("s")
    else:
        print(p_wiki.summary)
        pass
        

if __name__ == "__main__":
    main()
