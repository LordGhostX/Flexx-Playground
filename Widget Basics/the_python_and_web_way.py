"""Using widgets the Python way

In the above examples, we’ve used the “classic” way to build applications from basic components. Flexx provides a variety of layout widgets as well as leaf widgets (i.e. controls), see the list of widget classes.

Further, we’ve created high-level widgets by subclassing the flx.Widget class. These classes operate in JavaScript, because they are what we call JsComponent’s, more on that later. Effectively, we are able to show the widgets live inside the guide itself. However, if you are developing a desktop app, consider subclassing from PyWidget instead: this will make that your widgets operatate in Python instead of JavaScript. We talk more about this in the next page of the guide."""

"""Using widgets the web way

An approach that might be more familiar for web developers, and which is inspired by frameworks such as React is to build custom widgets using html elements. If you’re used to Python and the below looks odd to you, don’t worry, you don’t need it"""

from flexx import flx

class Web(flx.Widget):
    name = flx.StringProp('John Doe', settable=True)
    age =  flx.IntProp(22, settable=True)

    @flx.action
    def increase_age(self):
        self._mutate_age(self.age + 1)

    def _create_dom(self):
        # Use this method to create a root element for this widget.
        # If you just want a <div> you don't have to implement this.
        return flx.create_element('div')  # the default is <div>

    def _render_dom(self):
        # Use this to determine the content. This method may return a
        # string, a list of virtual nodes, or a single virtual node
        # (which must match the type produced in _create_dom()).
        return [flx.create_element('span', {},
                    'Hello', flx.create_element('b', {}, self.name), '! '),
                flx.create_element('span', {},
                    'I happen to know that your age is %i.' % self.age),
                flx.create_element('br'),
                flx.create_element('button', {'onclick': self.increase_age},
                    'Next year ...')
                ]
app = flx.App(Web)
app.launch('browser')  # show it now in a browser
flx.run()  # enter the mainloop

"""The _render_dom() method is called from an implicit reaction. This means that when any properties that are accessed during this function change, the function is automatically called again. This thus provides a declerative way to define the appearance of a widget using HTML elements.

Above, the third argument in create_element() is a string, but this may also be a list of dicts (create_element() returns a dict)."""
