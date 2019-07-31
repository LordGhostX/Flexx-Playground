"""Turning a widget into an app

To create an actual app from a widget, simply wrap it into an App. You can then launch() it as a desktop app, serve() it as a web app, dump() the assets, export() it as a standalone HTML document, or even publish() it online (experimental). Later in this guide we dive deeper into the different ways that you can run your app."""

from flexx import flx

class AppRender(flx.Widget):
    def init(self):
        flx.Label(text='hello world')

app = flx.App(AppRender)

app.export('renders/app.html', link=0)  # Export to single file

app.launch('browser')  # show it now in a browser
flx.run()  # enter the mainloop
