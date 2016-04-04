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
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import parse
import requests
import urllib, json

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
            phone = self.request.get('phone')
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
                    Phone: %s
                    Organization: %s
                    Email: %s
                    Current Email System: %s
                    No of Employees: %s

                    Please follow up.
                    """ % (name,phone,org,email,ces,employees)

            message.send()

            self.redirect('/signup?notification=Successfu!')

class Careers(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja2_env.get_template('main/careers.html')
        self.response.out.write(template.render(template_values))

class SalesLogin(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja2_env.get_template('main/saleslogin.html')
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
        
        template_values = {

        }
        template = jinja2_env.get_template('main/xml_response3.html')
        self.response.out.write(template.render(template_values))

    def post(self):

        fname = self.request.get('fname')
        lname = self.request.get('lname')
        status = 'Not Contacted'
        phone = self.request.get('phone')
        email = self.request.get('email')
        industry = self.request.get('industry')
        Lead_Source = 'isp website'
        Company = self.request.get('company')
        Website = self.request.get('website')
        No_of_Employees = self.request.get('no_of_employees')
        Secondary_Email = self.request.get('secondary_email')
        Number_of_Email_users = self.request.get('Number_of_Email_users')


        authtoken = random.choice(['0f6d5b3e2cb345f1780860a34c154fc9', 'b72f0f5ed3d2afa9b8a314649d3cf66f', '28c0030acc0560e35c24edf7917d9228' ])
        insert_lead(authtoken,fname,lname,status,phone,email,industry,Lead_Source,Company,Website,No_of_Employees,Secondary_Email,Number_of_Email_users)
        self.redirect('/crm3')


def insert_lead(authtoken,fname,lname,status,phone,email,industry,Lead_Source,Company,Website,No_of_Employees,Secondary_Email,Number_of_Email_users):




        params = {'authtoken':authtoken,'scope':'crmapi','xmlData':'<Leads>'
                                                                       '<row no="1">'
                                                                            '<FL val="First Name">%s</FL>'
                                                                            '<FL val="Last Name">%s</FL>'
                                                                            '<FL val="Lead Status">%s</FL>'
                                                                            '<FL val="Phone">%s</FL>'
                                                                            '<FL val="Email">%s</FL>'
                                                                            '<FL val="Industry">%s</FL>'
                                                                            '<FL val="Lead Source">%s</FL>'
                                                                            '<FL val="Company">%s</FL>'
                                                                            '<FL val="Website">%s</FL>'
                                                                            '<FL val="No of Employees">%s</FL>'
                                                                            '<FL val="Secondary Email">%s</FL>'
                                                                            '<FL val="Number of Email users">%s</FL>'
                                                                       '</row>'
                                                                   '</Leads>'% (fname,lname,status,phone,email,industry,Lead_Source,Company,Website,No_of_Employees,Secondary_Email,Number_of_Email_users)
                  }

        final_URL = "https://crm.zoho.com/crm/private/xml/Leads/insertRecords"

        data = urllib.urlencode(params)

        #print data

        request = urllib2.Request(final_URL,data)

        response = urllib2.urlopen(request)

        xml_response = response.read()


        print xml_response

class Records(webapp2.RequestHandler):

    def get(self):

        module_name = 'Leads'
        authtoken = '0f6d5b3e2cb345f1780860a34c154fc9'
        params = {'authtoken':authtoken,'scope':'crmapi'}
        final_URL = "https://crm.zoho.com/crm/private/xml/"+module_name+"/getRecords"
        data = urllib.urlencode(params)
        request = urllib2.Request(final_URL,data)
        response = urllib2.urlopen(request)
        xml_response = response.read()
        self.response.out.write(xml_response)

        #template_values = {
        #    'xml_response':xml_response,
        #}
        #template = jinja2_env.get_template('main/records.html')
        #self.response.out.write(template.render(template_values))



class Crm2(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja2_env.get_template('main/xml.xml')
        self.response.out.write(template.render(template_values))

class Zbooks(webapp2.RequestHandler):
    def get(self):

        url = "https://books.zoho.com/api/v3/customerpayments?authtoken=640df7b6237bec6ccc0101aec2a1605d&organization_id=8470645"
        response = urllib.urlopen(url)
        data = json.loads(response.read())

        url_invoice = "https://books.zoho.com/api/v3/invoices?authtoken=640df7b6237bec6ccc0101aec2a1605d&organization_id=8470645"
        response_invoice = urllib.urlopen(url_invoice)
        data_invoice = json.loads(response_invoice.read())


        template_values = {
            'data':data,
            'data_invoice':data_invoice
        }
        template = jinja2_env.get_template('main/zbooks.html')
        self.response.out.write(template.render(template_values))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', Signup),
    ('/careers', Careers),
    ('/contactus', ContactUs),
    ('/team', Team),
    ('/crm', Crm),
    ('/crm2', Crm2),
    ('/crm3', Crm3),
<<<<<<< HEAD
    ('/records', Records),
    ('/zbooks', Zbooks)
=======
<<<<<<< HEAD
    ('/saleslogin', SalesLogin)
=======
    ('/records', Records)
>>>>>>> 815ac92d0272539ff7325b9b0410f7a1f3bef4fa
    #('/signup', Crm3)
>>>>>>> 301d01f7b8f8e409d94f6cfc7caff65d31614a34
], debug=True)
