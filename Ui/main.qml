import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material
import GuitarRig

Window {
    width: 600
    height: 400
    visible: true
    title: "Guitar Rig"

    onClosing: Backend.stop_audio()

    ColumnLayout {
        anchors.fill:  parent

        Label {
            text: "Guitar Rig"
            color: "grey"
            font {
                pixelSize: 50
                bold: true
            }
            Layout.alignment: Qt.AlignHCenter
        }

        GridLayout {
            columns: 2
            Layout.leftMargin: 20

            Label {
                text: "Input device: "
                font.bold: true
            }
            Text {
                text: Backend.inputDevice
            }

            Label {
                text: "Output device: "
                font.bold: true
            }
            Text {
                text: Backend.outputDevice
            }
        }

        GridLayout {
            columns: 2
            Layout.leftMargin: 20
            Layout.rightMargin: 10

            Label {
                text: "Gain: "
                font.bold: true
            }

            Slider {
                Layout.fillWidth: true
                to: 30
                stepSize: 1
                value: Backend.gain

                onMoved: Backend.gain = value
            }

            Label {
                text: "Delay: "
                font.bold: true
            }

            Slider {
                Layout.fillWidth: true
                to: 2.0
                stepSize: 0.1
                value: Backend.delay

                onMoved: Backend.delay = value
            }

            Label {
                text: "Reverb: "
                font.bold: true
            }

            Slider {
                Layout.fillWidth: true
                to: 1.0
                stepSize: 0.1
                value: Backend.reverb

                onMoved: Backend.reverb = value
            }
        }

        GridLayout {
            columns: 2
            Layout.leftMargin: 20
            Layout.bottomMargin: 20

            Label {
                text: "Chorus: "
                font.bold: true
            }

            Switch {
                checked: Backend.chorus

                onClicked: Backend.chorus = checked
            }

            Label {
                text: "Phaser: "
                font.bold: true
            }

            Switch {
                checked: Backend.phaser

                onClicked: Backend.phaser = checked
            }
        }
    }
}