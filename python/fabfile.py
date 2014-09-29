from fabric.api import local

def hello(name="world"):
    print "Hello %s" % (name)

def startCry():
    print "STARTING"

def endCry():
    print "WooHoo !! finished"

def prepare():
    local("python echo.py")
    raise Exception("yo")

def do_task():
    startCry()
    prepare()
    endCry()
