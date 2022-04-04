import glob
import os
import re
import json

class Page:
    def __init__(self, path, title, tags, date):
        self.path = path
        self.title = title
        self.tags = tags
        self.date = date

class PageEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Page):
            return {"path": o.path, "title": o.title, "tags": o.tags, "date": o.date}
        return json.JSONEncoder.default(self, o)

os.chdir(os.path.join(os.getcwd(), "output"))

files = glob.glob(os.path.join("content", "*.html"))

# Make index.html
re_title = re.compile(r'<title>(.*)</title>')
re_tag = re.compile(r'<meta name="keywords" content="(.*)" *[/]>')
re_date = re.compile(r'<meta name="date" content="(.*)" *[/]>')

pages = []
for file_path in files:
    path = file_path.replace("\\", "/")
    title = "(No Title)"
    tags = []
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        title = re_title.search(content).group(1)
        date = re_date.search(content).group(1)
        tags = [t.strip() for t in re_tag.search(content).group(1).split(',')]

    pages.append(Page(path, title, tags, date))

js = json.dumps(pages, cls=PageEncoder, ensure_ascii=False)

f = open(os.path.join("data.js"), "w+")
f.write("const CONTENT_META_DATA = " + js)
f.close()

os.chdir("..")
