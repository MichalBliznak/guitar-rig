Pre-requisites
--------------

These Python packages need to be installed:
- numpy
- pedalboard
- PySide6

One could do that as follows:

```bash
pip3 install numpy pedalboard PySide6
```

Other information
-----------------

Adjust the input/output device names and sample rate in the `audio.py` accordingly to your HW setup:

```python
SAMPLE_RATE = 44100 # Set to 44100, or 48000 for higher quality (but higher latency)
INPUT_DEVICE_NAME = "Axe IO One"
OUTPUT_DEVICE_NAME = "LS27A800U"
```

Start the application as follows:

```bash
python3 main.py
```

Resources
---------

Spotify Pedalboard library: https://spotify.github.io/pedalboard/index.html

Qt PySide6 library: https://doc.qt.io, https://doc.qt.io/qtforpython-6/index.html