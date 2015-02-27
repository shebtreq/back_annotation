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

class question(nodes.General, nodes.Element): pass

def visit_question_node(self, node):
    self.body.append("<div style=\" border-radius: 7px 7px 7px 7px; border-width: 3px; border-style: solid; border-color: inherit; max-width: 640px; padding: 5px 10px; \"  > ")
    self.body.append("<div style=\"font-weight: bold; margin: 5px 0px 2px; \">"+node["ques"]+"</div>")
    if node["a"]:
        self.body.append("<div>\n"+"<input type=\"radio\" name=\""+ node["id"] +"\" value=\"a\" checked>    " + node["a"]+"</div>")
    if node["b"]:
        self.body.append("<div>\n"+"<input type=\"radio\" name=\""+ node["id"] +"\" value=\"b\">    " + node["b"]+"</div>")
    if node["c"]:
        self.body.append("<div>\n"+"<input type=\"radio\" name=\""+ node["id"] +"\" value=\"c\">    " + node["c"]+"</div>")
    if node["d"]:
        self.body.append("<div>\n"+"<input type=\"radio\" name=\""+ node["id"] +"\" value=\"d\">    " + node["d"]+"</div>")
    if node["e"]:
        self.body.append("<div>\n"+"<input type=\"radio\" name=\""+ node["id"] +"\" value=\"e\">    " + node["e"]+"</div>")
    if node["f"]:
        self.body.append("<div>\n"+"<input type=\"radio\" name=\""+ node["id"] +"\" value=\"f\">    " + node["f"]+"</div>")
    self.body.append("<div style=\"height:40px; margin: 10px 0px;\" ><button type=\"button\"" +
                     "style=\"background:#dd4814;color:#000000;padding:5px 10px;text-decoration:none;border-style:none;margin: 10px 0px; float:left;\" "+
                     " onclick=\"ansFunc"+node["id"]+"()\">"+
                     "Submit Answer</button>")
    self.body.append("<div id=\"ansBox"+node["id"]+"\" style=\"height:100%; min-width:0px; float:left; padding: 5px 10px 5px 20px; margin: 10px 0px;\">  </div></div>")
    self.body.append("</div>")

    self.body.append("<script>")
    self.body.append("function ansFuncWhatsthecolourofthesky()")
    self.body.append("{")
    self.body.append("var elements = document.getElementsByName(\""+ node["id"] +"\");")
    self.body.append("for (i=0;i<elements.length;i++)")
    self.body.append("{")
    self.body.append("if(elements[i].checked == true)")
    self.body.append("{")
    self.body.append("if(elements[i].value.toLowerCase() == \""+ node["ra"] +"\".toLowerCase())")
    self.body.append("{")
    self.body.append("document.getElementById(\"ansBox"+node["id"]+"\").innerHTML = \"Correct Answer!!\";")
    self.body.append("break;")
    self.body.append("}")
    self.body.append("}")
    self.body.append("document.getElementById(\"ansBox"+node["id"]+"\").innerHTML = \"That is incorrect. Try again\";")
 #   self.body.append("document.getElementById(\"ansBox"+node["id"]+"\").innerHTML = \"Incorrect. The correct answer is "+ node["ra"] +"\";")
    self.body.append("}")
    self.body.append("}")
    self.body.append("</script>")


def depart_question_node(self, node):
    pass

class Question(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 7
    final_argument_whitespace = False
    option_spec = {
        "ra": directives.unchanged,
        "a": directives.unchanged,
        "b": directives.unchanged,
        "c": directives.unchanged,
        "d": directives.unchanged,
        "e": directives.unchanged,
        "f": directives.unchanged,
    }

    def run(self):
        id = "".join(self.arguments)
        id = id.replace("'", "")
        id = id.replace("?", "")
        ques = " ".join(self.arguments)

        ra = None
        a = None
        b = None
        c = None
        d = None
        e = None
        f = None

        if "ra" in self.options:
            ra = self.options["ra"]
        if "a" in self.options:
            a = self.options["a"]
        if "b" in self.options:
            b = self.options["b"]
        if "c" in self.options:
            c = self.options["c"]
        if "d" in self.options:
            d = self.options["d"]
        if "e" in self.options:
            e = self.options["e"]
        if "f" in self.options:
            f = self.options["f"]

        return [question(id=id, ques=ques, ra=ra, a=a, b=b, c=c, d=d, e=e, f=f)]


def setup(app):
    app.add_node(question, html=(visit_question_node, depart_question_node))
    app.add_directive("question", Question)