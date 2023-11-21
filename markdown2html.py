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
                f.write(parse(lines))
    else:
        exit(0)


def parse(lines):
    """ Reads markdown file line by line,
    and writes html equivalent
    """
    html = ""
    in_list = False
    list_type = None

    for line in lines:
        if line.startswith('#'):
            header_level, content = line.split(" ", 1)
            level = min(len(header_level), 6)
            html += f"<h{level}>{content.strip()}</h{level}>" + "\n"
        if line.startswith('-'):
            if not in_list:
                html += "<ul>\n"
                in_list = True
                list_type = "ul"
            content = line.split(" ", 1)[1]
            html += f"  <li>{content.strip()}</li>\n"
        elif line.startswith('*'):
            if not in_list:
                html += "<ol>\n"
                in_list = True
                list_type = "ol"
            content = line.split(" ", 1)[1]
            html += f"  <li>{content.strip()}</li>\n"
        elif in_list:
            if list_type == "ul":
                html += "</ul>\n"
            elif list_type == "ol":
                html += "</ol>\n"
            else:
                html += f"{line.strip()}\n</p>\n"
            in_list = False
            list_type = None
        elif not line.startswith('#') and not line.startswith('-') \
                and not line.startswith('*') and line != '\n':
            if not in_list:
                html += "<p>\n"
            if line.endswith(' \n'):
                html += f"{line.strip()}\n<br />\n"
                in_list = True
            else:
                html += f"{line.strip()}\n"

    if in_list:
        if list_type == "ul":
            html += "</ul>\n"
        elif list_type == "ol":
            html += "</ol>\n"
        else:
            html += "</p>\n"
            in_list = False

    return html


if __name__ == "__main__":
    markdown2html()
