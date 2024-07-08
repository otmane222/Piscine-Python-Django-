#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        if len(self) == 1 and self != '\n':
            return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
        return super().__str__().replace('\n', '\n<br />\n')
        # .replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
# return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        pass

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        
        if type(tag) != str:
            raise Elem.ValidationError
        if type(attr) != dict:
            raise Elem.ValidationError
        if type(tag_type) != str:
            raise Elem.ValidationError
        if tag_type not in ['double', 'simple']:
            raise Elem.ValidationError
 

        if content == '' and type(content) == str:
            raise Elem.ValidationError
        self.tag = tag
        self.attr = attr if attr else {}
        self.content = []
        self.tag_type = tag_type
        self.counter = 0
        if content:
            res = ''
            if type(content) == Elem:
                self.add_content(content)
            elif type(content) == list:
                for elem in content:
                    if type(elem) == Elem:
                        elem.counter += 1
                        self.add_content(elem)
                    elif type(elem) == Text:
                        if elem != Text(''):
                            self.add_content(Text(elem))
                        else:
                            self.add_content(Text(''))
                    else:
                        self.add_content(elem)
            elif type(content) == Text:
                self.add_content(Text(content))
                    

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        result = ''
        if self.tag_type == 'double':
            for elem in self.content:
                if type(elem) == Elem or isinstance(elem, Elem):
                    elem.counter = self.counter + 1
            open_tag = self.counter * '  ' + '<' + self.tag + self.__make_attr() + '>'
            if len(self.content) == 0:
                self.counter = 0
            close_tag =  self.counter * '  ' + '</' + self.tag + '>'
                    
            if len(self.content) == 0:
                result = open_tag + close_tag
            else:
                for elem in self.content:
                    if type(elem) != Elem and not isinstance(elem, Elem):
                        self.counter += 1
                        break
                for elem in self.content:
                    if type(elem) == Elem or isinstance(elem, Elem):
                        self.counter -= 1
                        break
                result = open_tag +  self.__make_content() + close_tag
        elif self.tag_type == 'simple':
            for elem in self.content:
                if type(elem) == Elem:
                    elem.counter = self.counter + 1
                elif type(elem) == Text:
                    elem = Text('  ' + elem)
            open_tag = self.counter * '  ' + '<' + self.tag + self.__make_attr() + ' />' + '\n'
            close_tag = ''
            result = open_tag + close_tag
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            if type(elem) != Elem:
                result += self.counter * '  ' + str(elem) + '\n'
            else:
                result +=  str(elem) + '\n'
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            if type(content) == Text:
                self.content.append(Text(content))
            else:
                self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))
        # this function should return True if the content is a Text instance or an Elem, or a list of both, False otherwise


def starto():
    html_elem = Elem("html")
    head_elem = Elem("head")
    title_elem = Elem("title")
    title_elem.add_content(Text('"Hello ground!"'))
    head_elem.add_content(title_elem)

    body_elem = Elem("body")
    h1_elem = Elem("h1")
    h1_elem.add_content(Text('"Oh no, not again!"'))
    body_elem.add_content(h1_elem)

    img_elem = Elem("img", {"src": "http://i.imgur.com/pfp3T.jpg"}, "simple")
    body_elem.add_content(img_elem)

    html_elem.add_content(head_elem)
    html_elem.add_content(body_elem)

    # Printing the HTML structure
    print(html_elem)

if __name__ == '__main__':
    try:
        starto()
    except Exception as e:
        print("damn")
        pass

    
