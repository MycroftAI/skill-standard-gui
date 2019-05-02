# Copyright 2019 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mycroft.skills.core import MycroftSkill


class StandardGUI(MycroftSkill):

    def __init__(self):
        super().__init__("StandardGUI")

    def initialize(self):
        # Initialize...
        # Handle generic "face" events
        self.add_event('enclosure.mouth.text', self.on_mouth_text)

    ###################################################################
    ## Compatability with Mark 1 standard face messages

    def on_mouth_text(self, message):
        text = message.data.get('text')
        self.gui.clear()
        self.gui['message_text'] = text
        self.gui.show_page('mouth_text.qml')


def create_skill():
    return StandardGUI()


