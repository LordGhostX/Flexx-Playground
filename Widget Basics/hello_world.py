from flexx import flx

class WebPage(flx.Widget):
    def init(self):
        flx.Button(text='hello')
        flx.Button(text='world')

app = flx.App(WebPage)
app.export('hello_world.html', link=0)
