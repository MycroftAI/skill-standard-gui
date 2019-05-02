
import QtQuick.Layouts 1.4
import QtQuick 2.4
import QtQuick.Controls 2.0
import org.kde.kirigami 2.4 as Kirigami

import Mycroft 1.0 as Mycroft

Mycroft.ProportionalDelegate {
    id: simpleGuiRoot
    
    Mycroft.AutoFitLabel {
        id: simpleTextType
        Layout.fillWidth: true
        Layout.preferredHeight: proportionalGridUnit * 40
        wrapMode: Text.Wrap
        font.family: "Noto Sans"
        font.weight: Font.Bold
        text: sessionData.message_text
    }
}
