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
from google.appengine.api import mail

import urllib

import urllib2
from jinja2 import Template
import random


template_path = os.path.join(os.path.dirname(__file__))

jinja2_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_path))

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class MainHandler(webapp2.RequestHandler):
    def get(self):


        template_values = {

        }
        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('main/index.html')
        self.response.out.write(template.render(template_values))

class Signup(webapp2.RequestHandler):
	def get(self):

            global signup
            template_values = {

            }
            notification = self.request.get('notification')
            if notification:
                template_values['notification'] = notification
            self.response.set_status(200)
            template = jinja2_env.get_template('main/signup.html')
            self.response.out.write(template.render(template_values))

	def post(self):
            global signup
            name = self.request.get('name')
            org = self.request.get('organization')
            ces = self.request.get('ces')
            email = self.request.get('email')
            employees = self.request.get('employees')

            message = mail.EmailMessage(sender="Contact Us form <ispwebsite@intellisoftpluswebsite.appspotmail.com>",
                                        subject="NEW Contact")

            message.to = 'reshiwani@intellisoftplus.com'
            message.body = """
                    Hi,

                    The below client has filled the online (isp website) contact form .

                    Name: %s
                    Organization: %s
                    Email: %s
                    Current Email System: %s
                    No of Employees: %s

                    Please follow up.
                    """ % (name,org,email,ces,employees)

            message.send()

            self.redirect('/signup?notification=Successfu!')

class Services(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja2_env.get_template('main/services.html')
        self.response.out.write(template.render(template_values))

class ContactUs(webapp2.RequestHandler):
	def post(self):
            global contactus
            name = self.request.get('name')
            email = self.request.get('email')
            msg = self.request.get('message')

            message = mail.EmailMessage(sender="Contact Us form <ispwebsite@intellisoftpluswebsite.appspotmail.com>",
                                        subject="NEW Contact")

            message.to = 'reshiwani@intellisoftplus.com'
            message.body = """
                    Hi,

                    The below client has field the online (isp website) contact form .

                    Name: %s
                    Email: %s
                    Message.: %s

                    Please follow up.
                    """ % (name,email,msg)

            message.send()

            self.redirect('/?notification=Successfu!#Contacts')

class Team(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja2_env.get_template('main/team.html')
        self.response.out.write(template.render(template_values))

class Crm(webapp2.RequestHandler):

    def get(self):
        module_name = 'Leads'

        authtoken_d = '0f6d5b3e2cb345f1780860a34c154fc9'
        authtoken_r = 'b72f0f5ed3d2afa9b8a314649d3cf66f'
        authtoken_i = '28c0030acc0560e35c24edf7917d9228'

        authtoken = random.choice(['0f6d5b3e2cb345f1780860a34c154fc9', 'b72f0f5ed3d2afa9b8a314649d3cf66f', '28c0030acc0560e35c24edf7917d9228' ])




        params = {'authtoken':authtoken,'scope':'crmapi'}
        final_URL = "https://crm.zoho.com/crm/private/xml/"+module_name+"/getRecords"
        data = urllib.urlencode(params)
        request = urllib2.Request(final_URL,data)
        response = urllib2.urlopen(request)
        xml_response = response.read()
        #print xml_response

        template_values = {
            'xml_response':xml_response,
        }
        template = jinja2_env.get_template('main/xml_response.html')
        self.response.out.write(template.render(template_values))

class Crm3(webapp2.RequestHandler):

    def get(self):

        #authtoken = '0f6d5b3e2cb345f1780860a34c154fc9'
        authtoken = random.choice(['0f6d5b3e2cb345f1780860a34c154fc9', 'b72f0f5ed3d2afa9b8a314649d3cf66f', '28c0030acc0560e35c24edf7917d9228' ])

        params = {'authtoken':authtoken,'scope':'crmapi','xmlData':'<Leads>'
                                                                       '<row no="1">'
                                                                           '<FL val="Lead Source">internal (dev test)</FL>'                                                                           '<FL val="Closing Date">2014-06-28</FL>'
                                                                           '<FL val="Company">Intellisoftplus Solutions</FL>'
                                                                           '<FL val="First Name">Phares</FL>'
                                                                            '<FL val="Last Name">Machira</FL>'
                                                                            '<FL val="Email">pmachira@intellisoftplus.com.com</FL>'
                                                                            '<FL val="Phone">0719301140</FL>'
                                                                            '<FL val="City">Nairobi</FL>'
                                                                            '<FL val="State">Upperhill</FL>'
                                                                            '<FL val="Country">Kenya</FL>'
                                                                            '<FL val="Zip Code">20100</FL>'
                                                                       '</row>'
                                                                   '</Leads>'
                  }

        final_URL = "https://crm.zoho.com/crm/private/xml/Leads/insertRecords"

        data = urllib.urlencode(params)

        print data

        request = urllib2.Request(final_URL,data)

        response = urllib2.urlopen(request)

        xml_response = response.read()

        print xml_response

        template_values = {
            'xml_response':xml_response,
        }
        template = jinja2_env.get_template('main/xml_response3.html')
        self.response.out.write(template.render(template_values))

class Crm2(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja2_env.get_template('main/xml.xml')
        self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', Signup),
    ('/services', Services),
    ('/contactus', ContactUs),
    ('/team', Team),
    ('/crm', Crm),
    ('/crm2', Crm2),
    ('/crm3', Crm3)
], debug=True)
