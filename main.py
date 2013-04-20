#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render(template_values))

class IntroHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('intro.html')
    self.response.out.write(template.render(template_values))

class TutorialHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('tutorial.html')
    self.response.out.write(template.render(template_values))

class MeetingHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('meeting.html')
    self.response.out.write(template.render(template_values))

class PeopleHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('people.html')
    self.response.out.write(template.render(template_values))

class ColumnHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('column.html')
    self.response.out.write(template.render(template_values))

class WhatHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('what.html')
    self.response.out.write(template.render(template_values))

class PartsHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('parts.html')
    self.response.out.write(template.render(template_values))

class KnowledgeHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('knowledge.html')
    self.response.out.write(template.render(template_values))

class ChooseHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('choose.html')
    self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', MainHandler),
                               # ('/intro', IntroHandler),
                               ('/meeting', MeetingHandler),
                               # ('/parts', PartsHandler),
                               ('/knowledge', KnowledgeHandler),
                               ('/choose', ChooseHandler),
                               ('/people', PeopleHandler),
                               ('/column', ColumnHandler),
                               # ('/tutorial', TutorialHandler),
                               ('/what', WhatHandler)],
                              debug=True)
