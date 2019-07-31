from flexx import flx

#The Widget class is the base class of all other ui classes. On itself it does not do or show much. What you’ll typically do, is subclass it to create a new widget that contains ui elements

class WebPage(flx.Widget):
    def init(self):
        flx.Button(text='hello')
        flx.Button(text='world')

app = flx.App(WebPage)
app.export('renders/hello_world.html', link=0)

#The above is usually not the layout that you want. Therefore there are layout widgets which distribute the space among its children in a more sensible manner

class HBox(flx.Widget):
    def init(self):
        with flx.HBox():
            flx.Button(text='hello', flex=1)
            flx.Button(text='world', flex=2)

app = flx.App(HBox)
app.export('renders/hbox.html', link=0)

#The HBox and Button are all widgets too. The example widgets that we created above are also refered to as “compound widgets”; widgets that contain other widgets. This is the most used way to create new UI elements
