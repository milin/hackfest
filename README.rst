hackfest
========

So far, this is a simple prototype of the scoring server/client for
the ``hackfest`` competition.

Check out the website, <http://jonwaltman.github.com/hackfest/>.


Dependencies
------------

`Python <http://www.python.org/>`_

`Twisted <http://twistedmatrix.com/trac/>`_

Build
-----

Installing on Ubuntu::

    sudo apt-get install twisted
    
Then to run the program::
  
    cd /path/to/hackfest
    twistd -ny hackfest.tac

This will start the ``twisted`` web server which will serve the 
program at <http://localhost:8080/>.
