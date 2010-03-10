from twisted.application import internet, service
from twisted.web import static, server, script
import os

root = static.File(os.getcwd())
root.ignoreExt(".rpy")
root.processors = {'.rpy': script.ResourceScript}
application = service.Application('web')
sc = service.IServiceCollection(application)
site = server.Site(root)
i = internet.TCPServer(8080, site)
i.setServiceParent(sc)
