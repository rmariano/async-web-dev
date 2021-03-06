from twisted.internet import protocol, reactor


class GreetProtocol(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(b"Hello world\n")
        self.transport.loseConnection()


class GreetFactory(protocol.ServerFactory):
    protocol = GreetProtocol

reactor.listenTCP(1079, GreetFactory())
reactor.run()
