import asyncio
import logging
import time

_LOGGER = logging.getLogger(__name__)


class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        _LOGGER.info("Start connection")
        self.transport = transport

    def data_received(self, data):
        _LOGGER.info("Receive")
        time.sleep(5)
        message = (b'HTTP/1.1 200 OK\n'
                   b'Content-Type: text/plain; charset=utf-8\n\n'
                   b'OK')
        _LOGGER.info("Write")
        self.transport.write(message)
        _LOGGER.info("Close")
        self.transport.close()
        _LOGGER.info("After Close")


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s [%(name)s] %(message)s")

loop = asyncio.get_event_loop()
coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 5000)
server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
