import os,models
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

url  = '/install'
view = 'index.html'

class Main(webapp.RequestHandler):
  def get(self):
    installed=True
    check=models.getConfig();
    if not check: 
      conf=newconfig()
      post=newpost()
      installed=False
    self.redirect("/")

def newconfig():
  data={
    'url'          :'http://myapplication.appspot.com',
    'title'        :'My own blog',
    'subtitle'     :'The awesomest blog on earth',
    'author'       :'Myself',
    'email'        :'myname at gmail com',
    'theme'        :'default',
    'themecss'     :'body{background:white; color:black;}',
    'footer'       :'Copyright, copyleft or who cares.',
    'about'        :'I am a blogger extraordinaire',
    'avatar'       :'myavatar.jpg',
    'useanalytics' : False,
    'analyticscode':'UA-??????-??',
    'usedisqus'    : False,
    'disquscode'   :'mydisqusid'
  }
  models.newConfig(data)
  return data

def newpost():
  data={
    'title'  :'Hello World!',
    'url'    :'helloworld',
    'summary':"""Welcome to my blog!""",
    'content':"""
<p><b>FABE - Fricking Awesome Blog Engine</b> has been installed!</p>
<p>To change the blog settings go to the <a href="/admin">admin console</a>. You will be asked to login to your GAE account, the admin console is restricted and only you have privileged access to it.</p>
<p>Please login clicking here: <a href="/admin/options">Admin Console</a></p>
<p>You can also click on the avatar to the right to access the admin console.</p>
<p>Delete or modify this post at will, you already have <b>FABE</b> installed, enjoy!.</p>
"""
  }
  models.newPost(data)
  return data

if __name__ == "__main__": 
  run_wsgi_app(webapp.WSGIApplication([(url,Main)],debug=True))
