#!/usr/bin/env python
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
import cgi
import datetime
import wsgiref.handlers
from BeautifulSoup import BeautifulSoup
import urllib2
from google.appengine.ext import webapp

class MainPage(webapp.RequestHandler):
  def get(self):

    url = 'http://en.wikipedia.org/wiki/Main_Page'
    request = urllib2.Request(url)
    request.add_header('User-Agent','Srikanth Logic 1.0')
    opener = urllib2.build_opener()

    soup = BeautifulSoup(opener.open(request).read())
    t = soup.find(id='mp-dyk')

    y = t.__str__().replace('href="/wiki/','href="http://en.wikipedia.org/wiki/')

    self.response.out.write('<html><body>')
    self.response.out.write(y)
    self.response.out.write('</body></html>')

application = webapp.WSGIApplication([
  ('/', MainPage)
], debug=True)

def main():
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
