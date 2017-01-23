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
import os
import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT=jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+"/templates"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_vars={'title':'Shu Zhou'}	
    	template = JINJA_ENVIRONMENT.get_template('index.html')
    	self.response.out.write(template.render(template_vars))

class LiftHandler(webapp2.RequestHandler):
    def get(self):
        template_vars={'title':'Lift | Shu Zhou'}	
    	template = JINJA_ENVIRONMENT.get_template('work/lift.html')
    	self.response.out.write(template.render(template_vars))

class CeremonyHandler(webapp2.RequestHandler):
    def get(self):
        template_vars={'title':'Ceremony | Shu Zhou'}	
    	template = JINJA_ENVIRONMENT.get_template('work/ceremony.html')
    	self.response.out.write(template.render(template_vars))   	

class DominoHandler(webapp2.RequestHandler):
    def get(self):
        template_vars={'title':'Domino | Shu Zhou'}	
    	template = JINJA_ENVIRONMENT.get_template('work/domino.html')
    	self.response.out.write(template.render(template_vars))  

class GraphicHandler(webapp2.RequestHandler):
    def get(self):
        template_vars={'title':'Graphic | Shu Zhou'} 
        template = JINJA_ENVIRONMENT.get_template('work/graphic.html')
        self.response.out.write(template.render(template_vars)) 

class TimberHandler(webapp2.RequestHandler):
    def get(self):
        template_vars={'title':'Timber | Shu Zhou'} 
        template = JINJA_ENVIRONMENT.get_template('work/timber.html')
        self.response.out.write(template.render(template_vars))

class PavilionHandler(webapp2.RequestHandler):
    def get(self):
        template_vars={'title':'Pavilion | Shu Zhou'} 
        template = JINJA_ENVIRONMENT.get_template('work/pavilion.html')
        self.response.out.write(template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index', MainHandler),
    ('/work/lift', LiftHandler),
    ('/work/ceremony', CeremonyHandler),
    ('/work/domino', DominoHandler),
    ('/work/graphic', GraphicHandler),
    ('/work/timber', TimberHandler),
    ('/work/pavilion', PavilionHandler),
    ('/.*', MainHandler)
], debug=True)