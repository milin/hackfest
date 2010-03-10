hackfest
========

So far, this is a simple prototype of the scoring server/client for the ``hackfest`` 
competition.

More information can be found at our website, <http://jonwaltman.github.com/hackfest/>.


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
