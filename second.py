from twisted.internet import reactor
from twisted.web.server import Site, NOT_DONE_YET
from twisted.web.resource import Resource


class Greeting(Resource):
    isLeaf = True

    def delayed(self, request):
        query = request.args.get(b'q', [""])[0]

        reply_txt = "Hello {0!s}\n".format(str(query)).encode('utf-8')
        request.write(reply_txt)
        request.finish()

    def render_GET(self, request):
        reactor.callLater(1, self.delayed, request)
        return NOT_DONE_YET


resource = Greeting()
factory = Site(resource)
reactor.listenTCP(2001, factory)
reactor.run()


"""
Calling like:
    curl localhost:2001?q=Mariano

Should reply:
    Hello Mariano
"""
