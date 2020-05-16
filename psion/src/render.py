#!/usr/bin/python3

from textwrap import dedent
import markdown

raw_md = open("index.md", "r").read()
raw_html = markdown.markdown(raw_md, extensions=['attr_list'])

header = (
"""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

    <!-- Header numbering -->
    <style>
        body {counter-reset: h2}
        h2 {counter-reset: h3}
        h2:before {counter-increment: h2; content: counter(h2) ". "}
        h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
    </style>

    <title>Iain's Psion Series3a Page</title>
  </head>
  <body>
  <div class="container">
"""
).strip() + "\n\n\n"

footer = "\n\n\n" + (
"""
  </div>  <!-- container -->
  </body>
</html>
"""
).strip()

with open("../index.html", "w") as fp:
    fp.write(header)
    fp.write(raw_html)
    fp.write(footer)
