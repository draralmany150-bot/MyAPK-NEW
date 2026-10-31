from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MyApp(App):

    def build(self):
        self.layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        self.layout.add_widget(Label(
            text="MyAPK",
            font_size=32
        ))

        self.status = Label(
            text="التطبيق جاهز للعمل",
            font_size=20
        )
        self.layout.add_widget(self.status)

        self.input = TextInput(
            hint_text="اكتب رسالة للاختبار",
            multiline=False,
            size_hint_y=None,
            height=55
        )
        self.layout.add_widget(self.input)

        button = Button(
            text="اختبار التطبيق",
            font_size=20,
            size_hint_y=None,
            height=60
        )
        button.bind(on_press=self.test_app)
        self.layout.add_widget(button)

        return self.layout

    def test_app(self, instance):
        self.status.text = "نجح الاختبار: " + self.input.text

MyApp().run()
