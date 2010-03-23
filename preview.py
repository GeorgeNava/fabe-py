import os,models,visitor
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

url  = '/admin/preview'
view = 'preview.html'

class Main(webapp.RequestHandler):
  def post(self):
    visitor.register(self.request)
    data={ 
      'options':models.getConfig(),
      'post':{
        'title':self.request.get('xtitle'),
        'content':self.request.get('xcontent')
      }
    }
    path=os.path.join(os.path.dirname(__file__),view)
    self.response.out.write(template.render(path,data))

if __name__ == "__main__": 
  run_wsgi_app(webapp.WSGIApplication([(url,Main)],debug=True))
