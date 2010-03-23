from google.appengine.ext import db

class Stats(db.Model):
  time  = db.DateTimeProperty(auto_now_add=True)
  url   = db.StringProperty()
  ip    = db.StringProperty()
  host  = db.StringProperty()
  ref   = db.StringProperty(multiline=True)
  agent = db.StringProperty(multiline=True)

def register(request):
  stat = Stats()
  stat.host    = request.host
  stat.url     = request.path
  stat.ip      = request.remote_addr
  stat.ref     = request.headers.get("referer")
  stat.agent   = request.headers.get("user-agent")
  stat.put()
