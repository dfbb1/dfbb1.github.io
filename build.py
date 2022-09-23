#! coding=utf8
"""
python3

build static page from markdown file.
1. convert md to html
2. replace css class
3. rebuild index by sitemap.json and dir structure

website map:
-   index.html: page of all/nav/refer
--  page: embed homepage/refer/nav
--  nav: homepage/archives/tags/refer/short_intro

"""
import json
import os
from datetime import datetime

import markdown2

default_tag = 'default'
sitemap = './sitemap.json'


def pre_create_dir(parent: str):
    if not os.path.exists(parent) or not os.path.isdir(parent):
        os.mkdir(parent)


def parse_tags(meta_line: str):
    if not meta_line:
        return ['', default_tag]
    m = meta_line.strip().split('|')
    if len(m) == 1:
        m.append(default_tag)
    elif len(m) == 2:
        # todo ascii
        pass
    return m


def write2html(filename: str, html_content: str):
    with open(filename, mode='w', encoding='utf-8') as w:
        w.writelines(
            '<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8"><title>一念blog</title><link rel="stylesheet" href="../../css/nav.css"><link rel="stylesheet" href="../../css/common.css"><link rel="stylesheet" href="../../css/page.css"><link rel="stylesheet" href="../../css/code.css"><script src="../../js/common.js"></script><script> window.onload = function () {document.getElementById("nav-head").addEventListener("click", function () {goHome();});initFolder();}</script></head><body><div id="nav" class="nav"><div class="nav-head" id="nav-head">一念</div><div class="nav-short">心能转物，即同如来</div><div class="nav-btn">refer</div><div class="nav-btn">分类</div><div class="nav-btn">归档</div><div id="hide-btn-left">《</div></div><div id="content" class="content"><div id="hide-btn-right">》</div>')
        w.writelines(html_content)
        w.writelines('</div></body></html>')


if __name__ == '__main__':
    engine = markdown2.Markdown(extras=['fenced-code-blocks'])
    parent_dir = 'resources'
    mds = os.listdir(parent_dir)
    page_map = json.load(open(sitemap))
    old_keys = [i for i in page_map.keys()]
    # check empty html
    for k in old_keys:
        if not os.path.exists(k):
            del page_map[k]

    for md in mds:
        f = open(parent_dir + os.sep + md, mode='r', encoding='utf-8')
        tags = parse_tags(f.readline())
        html = engine.convert(f.read().lstrip())
        # print(html)
        html_dir = 'pages/' + tags[1]
        # TODO 文件名校验，ascii
        short_name = md[:md.rindex('.')] + '.html' if '.' in md else md + '.html'
        # 写入文件
        full_filename = html_dir + '/' + short_name
        if not os.path.exists(full_filename):
            pre_create_dir(html_dir)
        # TODO
        write2html(full_filename, html)
        # 整理元数据
        if full_filename not in page_map:
            page_map[full_filename] = {
                "title": tags[0],
                "tags": tags[1:],
                "date": datetime.fromtimestamp(os.stat(parent_dir + os.sep + md).st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            }
        f.close()

    with open('./js/data.js', 'w', encoding='utf-8') as wd:
        wd.write('const pageMap = ' + json.dumps(page_map))
        wd.close()
    with open(sitemap, 'w', encoding='utf-8') as ws:
        json.dump(page_map, ws)
        ws.close()

