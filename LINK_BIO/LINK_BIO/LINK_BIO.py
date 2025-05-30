import reflex as rx

class State(rx.State):
    # Define any state variables here
    pass

def index() -> rx.Component:
    return rx.text("Hola", font_size="2em", font_weight="bold")

app = rx.App()
app.add_page(index, title="LINK_BIO")