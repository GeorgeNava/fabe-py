import os,models,visitor
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

url  = '/'
view = 'index.html'

class Main(webapp.RequestHandler):
  def get(self):
    visitor.register(self.request)
    data={ 
      'options' : models.getConfig(),
      'history' : models.getLastEntries(10) 
    }
    path = os.path.join(os.path.dirname(__file__),view)
    self.response.out.write(template.render(path,data))

if __name__ == "__main__":
  run_wsgi_app(webapp.WSGIApplication([(url,Main)],debug=True))