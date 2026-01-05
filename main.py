import sys
# Import the Backend class to register it as a singleton used in the QML code
from backend import *

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

logging.basicConfig(
    level=logging.INFO,  # Minimum level to log
    format="%(asctime)s [%(levelname)s] %(message)s"
)

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.addImportPath(sys.path[0])
    engine.loadFromModule("Ui", "Main")
    if not engine.rootObjects():
        exit(-1)
    exit_code = app.exec()
    del engine
    exit(exit_code)
