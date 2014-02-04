# -*- coding: utf-8 -*-

from twisted.internet import reactor
from twisted.internet.protocol import ProcessProtocol

class StressTestProtocol(ProcessProtocol):
    def  outReceived(self, data):
        pass
    def errReceived(self, data):
        pass
    def processExited(self, reason):
        pass
    def processEnded(self, reason):
        pass

proto = StressTestProtocol()

reactor.spawnProcess(proto, "/usr/bin/env", ('python', 'send_metrics.py', 'pickled'))
reactor.spawnProcess(proto, "/usr/bin/env", ('python', 'send_metrics.py',))

reactor.run()
