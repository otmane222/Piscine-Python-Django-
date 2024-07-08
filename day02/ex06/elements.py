















import elem

class Html(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='html', attr=atr,  content=content)

class Head(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='head', attr=atr, content=content)

class Body(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='body', attr=atr, content=content)

class Title(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='title', attr=atr, content=content)

class Meta(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='meta', attr=atr, content=content, tag_type='simple')

class Img(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='img', attr=atr, content=content, tag_type='simple')

class Table(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='table', attr=atr, content=content)

class Th(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='th', attr=atr, content=content)

class Tr(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='tr', attr=atr, content=content)

class Td(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='td', attr=atr, content=content)

class Ul(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='ul', attr=atr, content=content)

class Ol(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='ol', attr=atr, content=content)

class Li(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='li', attr=atr, content=content)

class H1(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='h1', attr=atr, content=content)

class H2(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='h2', attr=atr, content=content)

class P(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='p', attr=atr, content=content)

class Div(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='div', attr=atr, content=content)

class Span(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='span', attr=atr, content=content)

class Hr(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='hr', attr=atr, content=content)

class Br(elem.Elem):
    def __init__(self, content=None, atr={}):
        elem.Elem.__init__(self, tag='br', attr=atr, content=content , tag_type='simple')


def starto():
    print(Html([Head([Title(elem.Text('"Hello ground!"'))]), Body([H1(elem.Text('"Oh no, not again!"'))])]))

if __name__ == "__main__":
    starto()
