import os,models,visitor
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

url  = '/anyurl'
view = 'anyurl.html'

class Main(webapp.RequestHandler):
  def get(self):
    visitor.register(self.request)
    data = {'anyvar':'anyvalue'}
    path = os.path.join(os.path.dirname(__file__), view)
    self.response.out.write(template.render(path,data))

if __name__ == "__main__":
  run_wsgi_app(webapp.WSGIApplication([(requested_url, MainPage)],debug=True))