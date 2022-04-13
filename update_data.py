import glob
import os
import re
import json
from pathlib import Path

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

def collect_meta_data():
    re_title = re.compile(r'<title>(.*)</title>')
    re_tag = re.compile(r'<meta name="keywords" content="(.*)" *[/]>')
    re_date = re.compile(r'<meta name="date" content="(.*)" *[/]>')

    pages = []
    for (dirpath, _child_dir, child_file_list) in os.walk(Path("./output/content")):
        for child_file in child_file_list:
            if child_file[-5:] == ".html":
                path = Path(dirpath) / child_file
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    title = re_title.search(content).group(1)
                    date = re_date.search(content).group(1)
                    tags = [t.strip() for t in re_tag.search(content).group(1).split(',')]
                    pages.append(Page(str(path.relative_to("./output")), title, tags, date))
    return pages

def run():
    pages = collect_meta_data()
    js = json.dumps(pages, cls=PageEncoder, ensure_ascii=False)
    f = open(Path("./output/data.js"), "w+")
    f.write("const CONTENT_META_DATA = " + js)
    f.close()
