from services.message_bus import MessageBus
from services.scanner_config import ScannerConfig

class ScannerController:
    def __init__(self, message_bus: MessageBus, scanner_config: ScannerConfig):
        self._message_bus = message_bus
        self._scanner_config = scanner_config

    def list(self):
        return self._scanner_config.get_scanners()

    def scan(self, scanner_id, tuner_id):
        self._message_bus.send({
            "scanner_id": scanner_id,
            "action": "scan",
            "tuner_id": tuner_id
        })

    def next(self, scanner_id, tuner_id):
        self._message_bus.send({
            "scanner_id": scanner_id,
            "action": "next",
            "tuner_id": tuner_id
        })

    def prev(self, scanner_id, tuner_id):
        self._message_bus.send({
            "scanner_id": scanner_id,
            "action": "prev",
            "tuner_id": tuner_id
        })

    def stop(self, scanner_id, tuner_id):
        self._message_bus.send({
            "scanner_id": scanner_id,
            "action": "stop",
            "tuner_id": tuner_id
        })

    def skip(self, scanner_id, tuner_id):
        self._message_bus.send({
            "scanner_id": scanner_id,
            "action": "skip",
            "tuner_id": tuner_id
        })

    def clear_skip(self, scanner_id, tuner_id, value, all_values):
        self._message_bus.send({
            "scanner_id": scanner_id,
            "action": "clear_skip",
            "tuner_id": tuner_id,
            "value": value,
            "all": all_values
        })

    def tune(self, scanner_id, tuner_id, value):
        rssi_threshold = 1000 - value
        self._message_bus.send({
            "scanner_id": scanner_id,
            "action": "tune",
            "tuner_id": tuner_id,
            "value": rssi_threshold
        })