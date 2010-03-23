import os,re,models,visitor
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

url  = '/admin/publish'

class Main(webapp.RequestHandler):
  def post(self):
    visitor.register(self.request)
    models.newPost({
      'url'    :cleanUrl(self.request.get('xtitle')),
      'title'  :self.request.get('xtitle'),
      'content':cleanContent(self.request.get('xcontent')),
      'summary':cleanSummary(self.request.get('xcontent'))
    })
    self.redirect("/")

def unescape(s):        return s.replace("&lt;","<").replace("&gt;",">").replace("&amp;","&")
def cleanUrl(url):      return re.sub('[^a-z^A-Z^0-9]','',url).lower()
def cleanContent(html): return unescape(html).replace("'","\'")
def cleanSummary(html): return unescape(re.sub('<[a-zA-Z\/][^>]*>','',html)).replace("'","\'")[0:200]+'...'


if __name__ == "__main__": 
  run_wsgi_app(webapp.WSGIApplication([(url,Main)],debug=True))
