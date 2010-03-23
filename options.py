import os,models,visitor
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

url  = '/admin/options'
view = 'options.html'

class Main(webapp.RequestHandler):
  def get(self):
    visitor.register(self.request)
    data={ 'options':models.getConfig() }
    path=os.path.join(os.path.dirname(__file__),view)
    self.response.out.write(template.render(path,data))

  def post(self):
    visitor.register(self.request)
    options={
      'url'           : self.request.get('xurl'),
      'title'         : self.request.get('xtitle'),
      'subtitle'      : self.request.get('xsubtitle'),
      'author'        : self.request.get('xauthor'),
      'email'         : self.request.get('xemail'),
      'theme'         : self.request.get('xtheme'),
      'themecss'      : self.request.get('xthemecss'),
      'footer'        : self.request.get('xfooter'),
      'about'         : self.request.get('xabout'),
      'avatar'        : self.request.get('xavatar'),
      'useanalytics'  : self.request.get('xuseanalytics')=='True',
      'analyticscode' : self.request.get('xanalyticscode'),
      'usedisqus'     : self.request.get('xusedisqus')=='True',
      'disquscode'    : self.request.get('xdisquscode')
    }
    models.setConfig(options)
    self.redirect("/admin")

if __name__ == "__main__": 
  run_wsgi_app(webapp.WSGIApplication([(url,Main)],debug=True))
