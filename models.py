from google.appengine.ext import db

#---------- Classes ----------#
class Post(db.Model):
  title         = db.StringProperty()
  date          = db.DateTimeProperty(auto_now_add=True)
  url           = db.StringProperty()
  summary       = db.TextProperty()
  content       = db.TextProperty()

class Config(db.Model):
  url           = db.StringProperty()
  title         = db.StringProperty()
  subtitle      = db.StringProperty()
  author        = db.StringProperty()
  email         = db.StringProperty()
  theme         = db.StringProperty()
  themecss      = db.TextProperty()
  footer        = db.StringProperty()
  about         = db.TextProperty()
  avatar        = db.StringProperty()
  useanalytics  = db.BooleanProperty()
  analyticscode = db.StringProperty()
  usedisqus     = db.BooleanProperty()
  disquscode    = db.StringProperty()

#---------- Methods ----------#
def getLastEntries(n):
  sql  = "SELECT * FROM Post ORDER BY date DESC LIMIT %s" %(n)
  data = db.GqlQuery(sql)
  return data

def newPost(data):
  post = Post()
  post.title   = data['title']
  post.url     = data['url']
  post.summary = data['summary']
  post.content = data['content']
  post.put()

def getPost(url):
  sql  = "SELECT * FROM Post WHERE url=:1 LIMIT 1"
  post = db.GqlQuery(sql,url)
  return post[0]

def updatePost(data):
  post = getPost(data['url'])
  post.summary = data['summary']
  post.content = data['content']
  post.put()

def deletePost(url):
  post = getPost(url)
  post.delete()

def newConfig(data):
  config = Config()
  config.url           = data['url']
  config.title         = data['title']
  config.subtitle      = data['subtitle']
  config.footer        = data['footer']
  config.author        = data['author']
  config.email         = data['email']
  config.avatar        = data['avatar']
  config.useanalytics  = data['useanalytics']
  config.analyticscode = data['analyticscode']
  config.usedisqus     = data['usedisqus']
  config.disquscode    = data['disquscode']
  config.about         = data['about']
  config.theme         = data['theme']
  config.themecss      = data['themecss']
  config.put()

def getConfig():
  sql  = "SELECT * FROM Config LIMIT 1"
  data = db.GqlQuery(sql)
  return data[0]

def setConfig(data):
  config = getConfig()
  config.url           = data['url']
  config.title         = data['title']
  config.subtitle      = data['subtitle']
  config.footer        = data['footer']
  config.author        = data['author']
  config.email         = data['email']
  config.avatar        = data['avatar']
  config.useanalytics  = data['useanalytics']
  config.analyticscode = data['analyticscode']
  config.usedisqus     = data['usedisqus']
  config.disquscode    = data['disquscode']
  #config.about        = data['about']
  #config.theme        = data['theme']
  #config.themecss     = data['themecss']
  config.put()

