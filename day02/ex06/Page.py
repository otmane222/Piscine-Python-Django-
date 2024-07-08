import elements
import elem



def remove_tag(tags, elem2):
    if elem2.tag in tags:
        tags.remove(elem2.tag)
    for e in elem2.content:
        if isinstance(e, elem.Elem):
            remove_tag(tags, e)
        else:
            tags.remove("Text")


class Page:
    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        str1 =  "<!DOCTYPE html>\n"
        str1 += str(self.elements)
        return str(str1)
    def write_to_file(self, filename):
        if not filename.endswith(".html"):
            filename += ".html"
        if self.elements.tag != "html":
            print("Error: Page has no html tag")
            return
        f = open(filename, "w")
        f.write(str(self.elements))
        f.close()
    def is_valid(self, elem2):
        tags = []
        if isinstance(elem2, elem.Elem):
            if elem2.tag == "html":
                tags = ["html", "head", "body","title", "meta", "img", "table", "th", "tr", "td ", "ul", "ol", "li", "h1", "h2", "p", "div", "span", "hr", "br", "Text"]
                remove_tag(tags, elem2)
            if tags != [] : return False
            if elem2.tag == "html":
                if len(elem2.content) != 2: return False
                if not isinstance(elem2.content[0], elements.Head): return False
                if not isinstance(elem2.content[1], elements.Body): return False
            if elem2.tag == "head":
                if len(elem2.content) == 0: return False
                for e in elem2.content:
                    if not isinstance(e, elements.Title) and not isinstance(e, elements.Meta): return False
            if elem2.tag == "body":
                for e in elem2.content:
                    if not isinstance(e, elements.H1) \
                        and not isinstance(e, elements.H2) and not isinstance(e, elements.Table) \
                          and not isinstance(e, elements.Ul) and not isinstance(e, elements.Ol) \
                            and not isinstance(e, elements.Div) \
                              and not isinstance(e, elements.Span) and type(e) != elem.Text : return False
            if elem2.tag == "title":
                if len(elem2.content) != 1: return False
                if type(elem2.content[0]) != elem.Text: return False
            if elem2.tag == "h1":
                if len(elem2.content) != 1: return False
                if type(elem2.content[0]) != elem.Text: return False
            if elem2.tag == "h2":
                if len(elem2.content) != 1: return False
                if type(elem2.content[0]) != elem.Text: return False
            if elem2.tag == "Li":
                if len(elem2.content) != 1: return False
                if type(elem2.content[0]) != elem.Text: return False
            if elem2.tag == "Th":
                if len(elem2.content) != 1: return False
                if type(elem2.content[0]) != elem.Text: return False
            if elem2.tag == "Td":
                if len(elem2.content) != 1: return False
                if type(elem2.content[0]) != elem.Text: return False
            if elem2.tag == "P":
                if len(elem2.content) != 1: return False
                if type(elem2.content[0]) != elem.Text: return False
            if elem2.tag == "Span":
                if len(elem2.content) != 1: return False
                if type(elem2.content[0]) != elem.Text: return False
            if elem2.tag == "UL" or elem2.tag == "OL":
                for e in elem2.content:
                    if not isinstance(e, elements.Li): return False
            if elem2.tag == "Tr":
                for e in elem2.content:
                    if not isinstance(e, elements.Td) and not isinstance(e, elements.Th): return False
            if elem2.tag == "Table":
                for e in elem2.content:
                    if not isinstance(e, elements.Tr): return False
        return True
        







def starto():
    html = elements.Html([elements.Head([elements.Title([elem.Text('"hello ground!"')])]), elements.Body()])
    # print(html)
    pa = Page(html)
    print(pa)
    pa.write_to_file("test.html")
    

if __name__ == "__main__":
    starto()