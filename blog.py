#!/usr/bin/env python3
import os
import sys
import shutil
import glob
import subprocess
from pathlib import Path
import update_data

def copy_assets(src_dir: Path, dst_dir: Path, file_names: list, dir_names: list):
    for file_name in file_names:
        src = src_dir / file_name
        dst = dst_dir / file_name
        if not os.path.exists(dst):
            shutil.copyfile(src, dst)
    for dir_name in dir_names:
        src = src_dir / dir_name
        dst = dst_dir / dir_name
        if not os.path.exists(dst):
            shutil.copytree(src, dst)

def call_pandoc(proj_dir, in_path, out_path):
    template = proj_dir / "template.html"
    filter = proj_dir / "filter.py"
    args = [
        "pandoc",
        "-s",
        "-f", "commonmark_x+emoji-fancy_lists",
        "-M", "base=" + str(os.path.relpath("docs", out_path.parent)),
        "--no-highlight",
        "--template", str(template),
        "--filter", str(filter),
        "--katex=https://cdn.jsdelivr.net/npm/katex@0.13.16/dist/",
        in_path,
        "-o", out_path,
    ]
    subprocess.run(args)

def convert_md_to_html_all(proj_dir, root):
    work_list = []
    for (dirpath, _child_dir, child_file_list) in os.walk(root):
        for child_file in child_file_list:
            if child_file[-3:] == ".md":
                dirpath = Path(dirpath)
                in_file_name = Path(child_file)
                out_file_name = Path(child_file[:-3] + ".html")
                work_list.append((dirpath/in_file_name, dirpath/out_file_name))
    for (md, html) in work_list:
        call_pandoc(proj_dir, md, html)
        os.remove(md)

def main():
    # Directory where this script exists.
    proj_dir = Path(__file__).parent

    output_dir = Path("./docs")
    content_dir = Path("./docs/content")
    os.makedirs(content_dir, exist_ok=True)

    copy_assets(
        proj_dir,
        output_dir,
        ["index.html", "tag.html", "style.css", "script.js"],
        ["font"]
    )

    shutil.copytree(Path("./src"), content_dir, dirs_exist_ok=True)
    convert_md_to_html_all(proj_dir, content_dir)

    update_data.run()

if __name__ == "__main__":
    main()
