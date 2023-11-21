#!/usr/bin/python3
""" module markdown2html
"""
import sys
import os
import re


def markdown2html():
    """ Converts markdown to html
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    elif not os.path.exists(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)
    elif os.path.exists(sys.argv[1]):
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
        with open(sys.argv[2], 'w', encoding="utf-8") as f:
            for line in lines:
                f.write(parse(line))
    else:
        exit(0)


def parse(line):
    """ Reads markdown file line by line,
    and writes html equivalent
    """
    html = ""
    if line.startswith('#'):
        header_level, content = line.split(" ", 1)
        level = len(header_level)
        if level > 6:
            level = 6
        html = "<h{0:}>{1:}</h{0}>".format(level, content)
    elif line.startswith('-'):
        content = line.split(" ", 1)[1]
        html = f"<li>{content}</li>"
    elif line.startswith('*'):
        content = line.split(" ", 1)[1]
        html = f"<li>{content}</li>"
    else:
        if line == "\n":
            html = "<br/>"
        else: 
            html = "<p>{}</p>".format(line)
    return html


if __name__ == "__main__":
    markdown2html()
