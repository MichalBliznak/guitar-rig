import logging

from audio import AudioWorker
from PySide6.QtCore import QObject, Property, Signal, Slot, QThread
from PySide6.QtQml import QmlElement, QmlSingleton

QML_IMPORT_NAME = "GuitarRig"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0 # Optional

@QmlElement
@QmlSingleton
class Backend(QObject):
    # Qt signals
    inputDeviceChanged = Signal()
    outputDeviceChanged = Signal()
    gainChanged = Signal()
    delayChanged = Signal()
    reverbChanged = Signal()
    chorusChanged = Signal()
    phaserChanged = Signal()

    def __init__(self, /, parent=None):
        super().__init__(parent)

        try:
            # Start worker thread processing the audio stream on the application background
            self._audio = AudioWorker()
            self._audio.start()

        except Exception as e:
            logging.error(f"Unable to start audio thread. Reason: {e}")

    # Getters and Setters
    def get_input_device(self):
        return self._audio.input_device

    def get_output_device(self):
        return self._audio.output_device

    def get_gain(self):
        return self._audio.gain

    def set_gain(self, value):
        if self._audio.gain != value:
            logging.debug(f"Setting gain to {value}")
            self._audio.gain = value
            self.gainChanged.emit()

    def set_delay(self, value):
        if self._audio.delay != value:
            logging.debug(f"Setting delay to {value}")
            self._audio.delay = value

    def get_delay(self):
        return self._audio.delay

    def set_reverb(self, value):
        if self._audio.reverb != value:
            logging.debug(f"Setting reverb to {value}")
            self._audio.reverb = value

    def get_reverb(self):
        return self._audio.reverb

    def set_chorus(self, value):
        if self._audio.chorus != value:
            logging.debug(f"Setting chorus to {value}")
            self._audio.chorus = value

    def get_chorus(self):
        return self._audio.chorus

    def set_phaser(self, value):
        if self._audio.phaser != value:
            logging.debug(f"Setting phaser to {value}")
            self._audio.phaser = value

    def get_phaser(self):
        return self._audio.phaser

    # Qt slots callable from QML code
    @Slot()
    def stop_audio(self):
        self._audio.requestInterruption()
        self._audio.wait()

    # Properties accessible from QML
    inputDevice = Property(str, get_input_device, notify=inputDeviceChanged)
    outputDevice = Property(str, get_output_device, notify=outputDeviceChanged)
    gain = Property(float, get_gain, set_gain, notify=gainChanged)
    delay = Property(float, get_delay, set_delay, notify=delayChanged)
    reverb = Property(float, get_reverb, set_reverb, notify=reverbChanged)
    chorus = Property(bool, get_chorus, set_chorus, notify=chorusChanged)
    phaser = Property(bool, get_phaser, set_phaser, notify=phaserChanged)