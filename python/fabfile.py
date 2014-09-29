from __future__ import with_statement
from fabric.api import local,settings, abort
from fabric.contrib.console import confirm

def hello(name="world"):
    print "Hello %s" % (name)

def startCry():
    print "STARTING"

def endCry():
    print "WooHoo !! finished"

def prepare():
    local("python echo.py")
    exit(1)

def do_task():
    startCry()
    with settings(warn_only=True):
        result = local("python echo.py")
    if result.failed and not confirm("Test failed. Do you want to continue ?"):
        abort("Quitting")
    endCry()
    

