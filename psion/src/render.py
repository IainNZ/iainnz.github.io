#!/usr/bin/python3

from textwrap import dedent
import markdown

raw_md = open("index.md", "r").read()
raw_html = markdown.markdown(raw_md)

header = (
"""
<html>
<body>
"""
).strip() + "\n\n\n"

footer = "\n\n\n" + (
"""
</body>
</html>
"""
).strip()

with open("../index.html", "w") as fp:
    fp.write(header)
    fp.write(raw_html)
    fp.write(footer)
