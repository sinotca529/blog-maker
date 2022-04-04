#!/usr/bin/env python3
import os
import sys
import shutil
import glob
import subprocess

def copy_assets(pwd, proj_dir):
    dir_output = os.path.join(pwd, "output")
    os.makedirs(dir_output, exist_ok=True)
    file_names = ["index.html", "tag.html", "style.css"]
    for file_name in file_names:
        src = os.path.join(proj_dir, file_name)
        dst = os.path.join(dir_output, file_name)
        if not os.path.exists(dst):
            shutil.copyfile(src, dst)

def make_html(pwd, proj_dir):
    dir_out_content = os.path.join(pwd, "output", "content")
    os.makedirs(dir_out_content, exist_ok=True)
    markdowns = glob.glob("*.md")
    for markdown in markdowns:
        output_file = os.path.join(dir_out_content, os.path.basename(markdown).split(".")[0] + ".html")
        template = os.path.join(proj_dir, "template.html")
        filter = os.path.join(proj_dir, "filter.py")
        args = [
            "pandoc",
            "-s",
            "-f", "commonmark_x+emoji-fancy_lists",
            "--no-highlight",
            "--template", template,
            "--filter", filter,
            "--katex=https://cdn.jsdelivr.net/npm/katex@0.13.16/dist/",
            markdown,
            "-o", output_file,
        ]
        subprocess.run(args)

def update_page_data(proj_dir):
    args = [
        "python3",
        os.path.join(proj_dir, "update-data.py")
    ]
    subprocess.run(args)

def main():
    # Directory where this script exists.
    proj_dir = os.path.dirname(os.path.realpath(__file__))
    pwd = os.getcwd()

    copy_assets(pwd, proj_dir)
    make_html(pwd, proj_dir)
    update_page_data(proj_dir)

if __name__ == "__main__":
    main()

