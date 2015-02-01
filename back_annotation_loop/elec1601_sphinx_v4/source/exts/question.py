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

    self.body.append("<div id=\"question_post\">"+node["id"]+"</div>")
    self.body.append("<input type=\"radio\" name=\"Answer\" value=\"ra\" checked>" + node["ra"])
    if node["a"]:
        self.body.append("\n<br>\n"+"<input type=\"radio\" name=\"Answer\" value=\"a\" checked>" + node["a"])
    if node["b"]:
        self.body.append("\n<br>\n"+"<input type=\"radio\" name=\"Answer\" value=\"b\">" + node["b"])
    if node["c"]:
        self.body.append("\n<br>\n"+"<input type=\"radio\" name=\"Answer\" value=\"c\">" + node["c"])
    if node["d"]:
        self.body.append("\n<br>\n"+"<input type=\"radio\" name=\"Answer\" value=\"d\">" + node["d"])
    if node["e"]:
        self.body.append("\n<br>\n"+"<input type=\"radio\" name=\"Answer\" value=\"e\">" + node["e"])
    if node["f"]:
        self.body.append("\n<br>\n"+"<input type=\"radio\" name=\"Answer\" value=\"f\">" + node["f"])

    self.body.append("<button type=\"button\" onclick=\"document.getElementById('answerbox').innerHTML = 'Correct Answer:'"+node["ra"]+"'>Submit</button>")
    self.body.append("<div id=\"answerbox\"></div>")

def depart_question_node(self, node):
    pass

class Question(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 6
    final_argument_whitespace = False
    option_spec = {
        "RA": directives.unchanged,
        "A": directives.unchanged,
        "B": directives.unchanged,
        "C": directives.unchanged,
        "D": directives.unchanged,
        "E": directives.unchanged,
        "F": directives.unchanged,
    }

    def run(self):
        ra = None
        a = None
        b = None
        c = None
        d = None
        e = None
        f = None

        if "RA" in self.options:
            ra = self.options["RA"]
        if "A" in self.options:
            a = self.options["A"]
        if "B" in self.options:
            b = self.options["B"]
        if "C" in self.options:
            c = self.options["C"]
        if "D" in self.options:
            d = self.options["D"]
        if "E" in self.options:
            e = self.options["E"]
        if "F" in self.options:
            f = self.options["F"]
        
        return [question(id=self.arguments[0], ra=ra, a=a, b=b, c=c, d=d, e=e, f=f)]


def setup(app):
    app.add_node(question, html=(visit_question_node, depart_question_node))
    app.add_directive("question", Question)