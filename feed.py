import os,cgi,datetime,models,visitor
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

url  = '/feed'
view = 'feed.xml'

class Main(webapp.RequestHandler):
  def get(self):
    visitor.register(self.request)
    options=models.getConfig()
    entries=models.getLastEntries(10)
    updated=entries[0].date
    data={
      'blog'   :options,
      'updated':updated,
      'entries':entries
    }
    path=os.path.join(os.path.dirname(__file__),view)
    self.response.out.write(template.render(path,data))

if __name__ == "__main__": 
  run_wsgi_app(webapp.WSGIApplication([(url,Main)],debug=True))
