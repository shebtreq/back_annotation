#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive

import os
import sys

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

    dir_home = os.path.abspath(__file__).replace("source/exts/youtube.py", "")
    dir_sup_html = dir_home + "build/html/_supporting_html/"

    create_supporting_html(dir_sup_html, node["id"])

    sup_html_url = dir_sup_html + node["id"] + ".html"

    link_url = "<div> <a href=\"%s\">Analytics for video %s</a></div>" % (sup_html_url, node["id"])

    self.body.append(link_url)

    self.body.append(self.starttag(node, "iframe", **attrs))
    self.body.append("</iframe>")



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

        if "width" not in self.options:
            width = None
        else:
            width = self.options["width"]

        if "height" not in self.options:
            height = None
        else:
            height = self.options["height"]

        dir_home = os.path.abspath(__file__).replace("source/exts/youtube.py", "")
        dir_Rrst = dir_home + "build/html/_supporting_html/%s.Rrst" % self.arguments[0]

        createRrst(dir_Rrst, self.arguments[0])

        return [youtube(id=self.arguments[0], width=width, height=height)]




def setup(app):
    app.add_node(youtube, html=(visit_youtube_node, depart_youtube_node))
    app.add_directive("youtube", YouTube)
    app.connect('builder-inited', create_dir_for_supporting_html)



def create_dir_for_supporting_html(app):

    dir_home = os.path.abspath(__file__).replace("source/exts/youtube.py", "")

    dir_home_build = dir_home + "build/"
    if not os.path.exists(dir_home_build):
        os.makedirs(dir_home_build)

    dir_home_build_html = dir_home_build + "html/"
    if not os.path.exists(dir_home_build_html):
        os.makedirs(dir_home_build_html)

    dir_home_build_html_sup = dir_home_build_html + "_supporting_html/"
    if not os.path.exists(dir_home_build_html_sup):
        os.makedirs(dir_home_build_html_sup)

    print(dir_home_build_html_sup)

    #print(dir_home_build_html_sup)
    #print('\n\n\n')



def createRrst(dir_Rrst, name):
    print dir_Rrst
    fp = open(dir_Rrst,'w')
    data = '.. {r %s, echo=FALSE, fig.cap=\"\"} \n rm(list=ls()) \n dump <- read.csv(\"~/Desktop/Classified/classroom_dataset.csv\", header = TRUE, sep =\'\t\') \n dump.height <- dim(dump)[1] \n dump.width <- dim(dump)[2] \n rownames(dump) <- NULL \n dump.width <- dim(dump)[2] \n dump.video.played <- dump[ with(dump, grepl(\"%s\", payload)), ] \n dump.video.played <- dump.video.played[ with(dump.video.played, grepl(\"PLAY\", payload)), ] \n dump.video.played <- subset(dump.video.played, selec = c(\"week\")) \n dump.video.played.height <- dim(dump.video.played)[1] \n hist.data <- c(NULL) \n for(i in 1:dump.video.played.height) \n { \n   value <- as.numeric(dump.video.played[i,1]) \n   hist.data <- c(hist.data, value) \n } \n hist(hist.data, breaks=16, xlim=c(0,16), main="Distribution of video watched over the semester\", col=\"skyblue\", xlab=\"Time Of Day\", ylab=\"Frequency\", border=\"white\") \n .. .. \n' % (name, name)
    fp.write(data)
    fp.close()



def create_supporting_html(file_dir, file_name):
    file_url = file_dir + file_name + ".html"
    #print(file_url)
    fp = open(file_url,'w')
    image_html = "<img alt=\"\" src=\"%s\">" % (file_dir + "figure/" + file_name + "-1.png")
    data = '<!DOCTYPE html>\n<html>\n<head>\n  <title>Distribution of video watched over the semester</title>\n</head>\n\n<body>\n  %s\n</body>\n\n</html>' % image_html
    fp.write(data)
    fp.close()
