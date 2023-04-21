from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class InstagramCard(BoxLayout):
    def __init__(self, image_path, caption, username, **kwargs):
        super(InstagramCard, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10

        # Add image
        image = Image(source=image_path)
        self.add_widget(image)

        # Add caption label
        caption_label = Label(text=caption, size_hint_y=None, height=50)
        self.add_widget(caption_label)

        # Add username label
        username_label = Label(text=username, size_hint_y=None, height=50)
        self.add_widget(username_label)


class InstagramCardApp(App):
    def build(self):
        # Create a container for the cards
        container = BoxLayout(orientation='vertical', spacing=10)

        # Create a scrollview for the container
        scrollview = ScrollView(size_hint=(1,1), size=(1000, 2000))
        scrollview.add_widget(InstagramCard)
        

        # Add 10 Instagram cards to the container
        for i in range(2):
            card = InstagramCard(
                image_path='logo.png',
                caption=f"Example caption {i+1}",
                username=f"Example username {i+1}",
            )
            card.size_hint_y = None  # Set size_hint_y to None
            card.height = 500  # Set a fixed height for the cards
            card.size_hint_x = None  # Set size_hint_y to None
            card.width = 500

            container.add_widget(card)

        return scrollview

if __name__ == '__main__':
    InstagramCardApp().run()
