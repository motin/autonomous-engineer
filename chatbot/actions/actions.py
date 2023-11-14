# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from abilities.hello_world.hello_world import get_hello_world_text
from abilities.tmux.interact import (
    send_echo_hello_world,
    split_pane_horizontally,
    split_pane_vertically,
)


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        text = get_hello_world_text()
        dispatcher.utter_message(text=text)

        text = send_echo_hello_world()
        dispatcher.utter_message(text=text)

        return []


class ActionSplitPane(Action):
    def name(self) -> Text:
        return "action_split_pane"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        if pane_split_direction := tracker.get_slot("pane_split_direction"):
            if pane_split_direction == "horizontally":
                text = split_pane_horizontally()
                dispatcher.utter_message(text=text)
                return []
            elif pane_split_direction == "vertically":
                text = split_pane_vertically()
                dispatcher.utter_message(text=text)
                return []

        # If the direction is not known, ask the question
        dispatcher.utter_message(template="utter_ask_split_direction")

        return []
