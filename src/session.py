from signalrcore.hub_connection_builder import HubConnectionBuilder
from .utils import logger


class Client:
    def __init__(self, token):
        self.access_token = token
        self.hub_connection = None
        self.setup_connection()
        self.logger = logger.AsyncLogCollector()

    def setup_connection(self):  # TODO: fix crash <class 'websocket._exceptions.WebSocketBadStatusException'>
                                 # Likely caused by an invalid SignalR config, need to examine the use-case more
        options = {
            "access_token_factory": lambda: self.access_token,
            "skip_negotiation": True
        }
        self.hub_connection = HubConnectionBuilder()\
            .with_url("wss://app.valour.gg/", options=options)\
            .with_automatic_reconnect({
                "type": "raw",
                "keep_alive_interval": 10,
                "reconnect_interval": 5,
                "max_attempts": 5
            }).build()

        self.hub_connection.on_open(lambda: logger.sync_logging(self.logger, "info", "Session opened"))
        self.hub_connection.on_close(lambda: logger.sync_logging(self.logger, "warn", "Session closed"))
        self.hub_connection.on_error(lambda error: logger.sync_logging(self.logger, "error", "Connection error: {error}"))

    async def start(self):
        """Start the session"""
        self.hub_connection.start()
        await self.logger.info("Session started")

    async def stop(self):
        """End the session"""
        self.hub_connection.stop()
        await self.logger.info("Session stopped")
