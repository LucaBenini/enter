from typing import Optional
import os
import os.path
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import NumericProperty

class Root(BoxLayout):
    # Track number of clicks
    counter = NumericProperty(0)

    def on_button_click(self,number):
        """Increase counter and update label."""
        self.counter += 1
        # Access label via id
        self.ids.second_row_label.text = f"Button pressed {self.counter} times"


class KivyEnterApp(App):
    title = "Enter System"

    def build(self) -> Root:
        # Load KV before building to register classes and ids
        Builder.load_file(os.path.join(os.path.dirname(__file__) ,"app.kv"))
        return Root()

    def show_message(self, text: str, title: str = "Info") -> None:
        """Show a simple, reusable message popup."""
        content = BoxLayout(orientation="vertical", spacing="12dp", padding="16dp")

        message = Label(
            text=text,
            halign="center",
            valign="middle",
        )
        # Ensure label wraps nicely
        message.bind(size=lambda *_: setattr(message, "text_size", message.size)) # type: ignore

        ok_btn = Button(text="OK", size_hint=(1, None), height="40dp")

        popup = Popup(
            title=title,
            content=content,
            size_hint=(None, None),
            size=("380dp", "220dp"),
            auto_dismiss=False,  # explicit close via OK
        )

        ok_btn.bind(on_release=lambda *_: popup.dismiss()) # type: ignore
        content.add_widget(message)
        content.add_widget(ok_btn)

        popup.open()
