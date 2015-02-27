#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive

import io
import os
import sys
import re

class youtube(nodes.General, nodes.Element): pass

def visit_youtube_node(self, node):
    width = node["width"]
    height = node["height"]
    px = "px"
    aspect = (4, 3)
    if width is None:
        if height is None:
            width = 640
        else:
            width = height * aspect[0] / aspect[1]
    if height is None:
        height = width * aspect[1] / aspect[0]
    style = {
        "width": "%d%s" % (width, px),
        "height": "%d%s" % (height, px),
        "border": "0",
    }
    attrs = {
        "src": "http://www.youtube.com/embed/%s" % node["id"],
        "style": "; ".join("%s: %s" % keyvalue for keyvalue in style.iteritems())
    }

    bsupp = os.path.abspath(__file__).replace("source/exts/youtube.py", "") + "build/html/_images/time_spent_watching_video_" + node["id"] 
    bsupp = remove_c(bsupp)
    link_url = "<br> <a id=\"" + "video_analytics_" + node["id"] + "\" href=\""+  bsupp  +"\">Video Analytics</a><br>"
    self.body.append(link_url)
    self.body.append(self.starttag(node, "iframe", **attrs))
    self.body.append("</iframe>")

    self.body.append('<script>\n')
    self.body.append('function get_cookie(cookie_name)\n')
    self.body.append('{\n')
    self.body.append('var cookie_string = document.cookie;\n')
    self.body.append('if (cookie_string.length != 0)\n')
    self.body.append('{\n')
    self.body.append("var cookie_value = cookie_string.match( '(^|;)[\s]*' + cookie_name + '=([^;]*)');\n")
    self.body.append('return cookie_value[2];\n')
    self.body.append('}\n')
    self.body.append("return '' ;\n")
    self.body.append('}\n')
    self.body.append('var name = get_cookie("username");\n')
    self.body.append('console.log(name);\n')
    self.body.append('var node = document.getElementById("'+'video_analytics_' + node['id']+'");\n')
    self.body.append('var href = node.href;\n')
    self.body.append('href = href + "-" + name + ".png";\n')

    self.body.append('document.getElementById("'+'video_analytics_' + node['id']+'").href = href;\n')
    self.body.append('console.log(document.getElementById("'+'video_analytics_' + node['id']+'").href);\n')
    self.body.append('</script>')


def depart_youtube_node(self, node):
    pass

class YouTube(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 2
    final_argument_whitespace = False
    option_spec = {
        "width": directives.nonnegative_int,
        "height": directives.nonnegative_int,
    }

    def run(self):
        width = None
        height = None
        if "width" in self.options:
            width = self.options["width"]
        if "height" in self.options:
            height = self.options["height"]

        Rrst = remove_c(os.path.abspath(__file__).replace("source/exts/youtube.py", "") + "source/_supporting_html/%s.Rrst" % self.arguments[0])
        createRrst(Rrst, self.arguments[0])
        return [youtube(id=self.arguments[0], width=width, height=height)]


def setup(app):
    app.add_node(youtube, html=(visit_youtube_node, depart_youtube_node))
    app.add_directive("youtube", YouTube)
    app.connect('builder-inited', create_dir_for_supporting_html)

def create_dir_for_supporting_html(app):
    home = os.path.abspath(__file__).replace("source/exts/youtube.py", "")
    build = remove_c(home + "build/")
    if not os.path.exists(build):
        os.makedirs(build)
    bhtml = remove_c(build + "html/")
    if not os.path.exists(bhtml):
        os.makedirs(bhtml)
    bsupp = remove_c(bhtml + "_supporting_html/")
    if not os.path.exists(bsupp):
        os.makedirs(bsupp)
    ssupp = remove_c(home + "source/_supporting_html/")
    if not os.path.exists(ssupp):
        os.makedirs(ssupp)

def createRrst(dir_Rrst, name):
    url_Rrst = remove_c(os.path.abspath(__file__).replace("youtube.py", "") + "time_spent_watching_video.Rrs")
    title = ""

    fp = open(url_Rrst, "r")
    content = fp.read()
    fp.close()


    import urllib
    try:
        url = urllib.urlopen("https://www.youtube.com/watch?v=" + name)
        html = url.read()
        url.close()
        html = html.decode("utf-8")
        for line in html.splitlines():
            matchObj = re.match(r'.*<title>(.*) - YouTube</title>.*', line)
            if matchObj:
                title = matchObj.group(1)
    except IOError:
        pass

    fp = open(dir_Rrst, "w")
    new = ""
    for line in content.splitlines():
        line = line.replace("%s2", name)
        if title:
            line = line.replace("%s1", title)
        else:
            line = line.replace("%s1", name)
        new += line + "\n"

    fp.write(new)
    fp.close()

def remove_c(source):
    source = source.replace("/ctime_spent_watching_video", "/time_spent_watching_video")
    source = source.replace("/cbuild/", "/build/")
    source = source.replace("/chtml/", "/html/")
    source = source.replace("/csource/", "/source/")
    source = source.replace("/cexts/", "/exts/")
    source = source.replace("/c_supporting_html/", "/supporting_html/")
    source = source.replace("/chourofdaystudy", "/hourofdaystudy")
    return source
