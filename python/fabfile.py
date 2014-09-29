from fabric.api import local

def hello(name="world"):
    print "Hello %s" % (name)

def prepare():
    local("python echo.py")
