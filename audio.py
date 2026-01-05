import logging

from PySide6.QtCore import QThread
from pedalboard import Pedalboard, Reverb, Delay, Gain, Chorus, Phaser
from pedalboard.io import AudioStream

SAMPLE_RATE = 44100 # Set to 44100, or 48000 for higher quality (but higher latency)
INPUT_DEVICE_NAME = "Axe IO One"
OUTPUT_DEVICE_NAME = "LS27A800U"

class AudioWorker(QThread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._delay = Delay(delay_seconds=1.0, feedback=0.25, mix=0.4)
        self._reverb = Reverb(room_size=0.25)
        self._gain = Gain(gain_db=15)
        self._chorus = Chorus()
        self._phaser = Phaser()
        self._board = Pedalboard([
              self._gain,
              self._delay,
              self._reverb
          ])

    def run(self):
        try:
            # Available devices
            logging.info(f"Input devices: {AudioStream.input_device_names}")
            logging.info(f"Output devices: {AudioStream.output_device_names}")

            with AudioStream(
                    input_device_name="AXE IO One",  # Guitar interface
                    output_device_name="LS27A800U"
            ) as stream:
                logging.info("Audio stream is running...")

                # Audio is now streaming through this pedalboard and out of your speakers!
                stream.plugins = self._board

                # Loop here until thread termination is requested
                while not self.isInterruptionRequested():
                    pass

                logging.info("Audio stream has been closed.")

        except Exception as e:
            logging.error(f"Unexpected error when starting audio stream. Reason {e}")

    @property
    def gain(self):
        return self._gain.gain_db

    @gain.setter
    def gain(self, gain):
        self._gain.gain_db = gain

    @property
    def delay(self):
        return self._delay.delay_seconds

    @delay.setter
    def delay(self, delay):
        self._delay.delay_seconds = delay

    @property
    def reverb(self):
        return self._reverb.room_size

    @reverb.setter
    def reverb(self, reverb):
        self._reverb.room_size = reverb

    @property
    def chorus(self):
        return self._chorus in self._board

    @chorus.setter
    def chorus(self, enable):
        if enable:
            self._board.insert(1, self._chorus)
        else:
            self._board.remove(self._chorus)

    @property
    def phaser(self):
        return self._phaser in self._board

    @phaser.setter
    def phaser(self, enable):
        if enable:
            self._board.insert(1, self._phaser)
        else:
            self._board.remove(self._phaser)

    @property
    def input_device(self):
        return INPUT_DEVICE_NAME

    @property
    def output_device(self):
        return OUTPUT_DEVICE_NAME
