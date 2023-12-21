from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton 
from kivymd.uix.label import MDLabel
from kivymd.theming import ThemeManager

class ChatApp(MDApp):
    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "BlueGrey"
        return self._build_ui()


KV = '''
BoxLayout:
    orientation: 'vertical'

    ScrollView:

        MDList:
            id: chat_container

    BoxLayout:
        padding: dp(10)

        MDTextField:
            id: message_input
            hint_text: 'Type your message...'
            on_text_validate: app.send_message()

        MDRaisedButton:
            text: 'Send'
            on_press: app.send_message()
'''
#createsa class chatApp that will represent the app
#this line also inherits from the MDApp class
# we are using a class to create objects 

class ChatApp(MDApp):
    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "BlueGrey"
        return Builder.load_string(KV)

class ChatAPP(MDApp):
    def build(self):
        return Builder.load_string(KV)
    

    def send_message(self):
        message_input = self.root.ids.message_input  # Fix the typo here
        message_text = message_input.text.strip()

        if message_text:
            chat_container = self.root.ids.chat_container

            message_label = MDLabel(
                text=message_text,
                theme_text_color="Primary",
                size_hint_y=None,
                height=dp(40),
            )
            chat_container.add_widget(message_label)
            message_input.text = ''  # Clears the input field

if __name__ == '__main__':
    ChatAPP().run()
            
            
        
        
 
   
    