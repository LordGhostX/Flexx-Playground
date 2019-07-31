"""
The init method

In the above example one can see the use of the init() method, which is a common use in Flexx. It is generally better to use it instead of __init__(), because Flexx calls it at a very approproate time in the initialization process. For example, when init() is called, the corresponding widget is the default parent.

Further, the init() gets the positional instantiation arguments: creating a component Person("john", 32) matches def init(self, name, age)."""

"""Structuring widgets

Flexx comes with it’s own layout system. (Therefore you should generally not use CSS for widget layout, though you can very well use CSS inside a widget).
Any widget class can also be used as a context manager. Within the context, that widget is the default parent; any widget that is created in that context and that does not specify a parent will have that widget as a parent. (This mechanism is thread-safe.) This allows for a style of writing that clearly shows the structure of your app"""

from flexx import flx

class HSplit(flx.Widget):
    def init(self):
        with flx.HSplit():
            flx.Button(text='foo')
            with flx.VBox():
                flx.Widget(style='background:red;', flex=1)
                flx.Widget(style='background:blue;', flex=1)

app = flx.App(HSplit)
app.export('renders/hsplit.html', link=0)
