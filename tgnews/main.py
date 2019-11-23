import argparse
import os
import re
import json


def find_htmls(path):
    html_files = []
    for dirpath, subdirs, files in os.walk(path):
        for x in files:
            if x.endswith(".html"):
                html_files.append(os.path.join(dirpath, x))
    return html_files


body_re = re.compile(".*<body>(.*)</body>")
tag_re = re.compile("<.*?>")

def only_words(txt):
    txt = txt.replace("\n", " ")
    body = body_re.match(txt).group(1)
    notag = re.sub(tag_re, " ", body)
    nosp = re.sub(" +", " ", notag).strip()

    return nosp


def prepare(path, out):
    files = find_htmls(path)
    with open(out, 'w') as o:
        for f in files:
            name = f.split("/")[-1]
            body = only_words(open(f).read())
            o.write(json.dumps({"fname": name, "body": body}))


methods = {
    "languages":  None,
    "news":       None,
    "categories": None,
    "threads":    None,
    "top":        None,

    "prepare": prepare,
}


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('method')
    parser.add_argument('dir')

    args = parser.parse_args()
    methods[args.method](args.dir)


def prepare_main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path')
    parser.add_argument('out')

    args = parser.parse_args()
    prepare(args.path, args.out)

