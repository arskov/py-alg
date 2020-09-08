from html.parser import HTMLParser
import sys

class MyHTMLParser(HTMLParser):
    def __init__(self, convert_charrefs=True):
        super(MyHTMLParser, self).__init__(convert_charrefs=True)
        self.result = []

    def handle_starttag(self, tag, attrs):
        self.result.append("Start : {}".format(tag))
        for t in attrs:
            self.result.append("-> {} > {}".format(t[0], t[1]))
    
    def handle_endtag(self, tag):
        self.result.append("End   : {}".format(tag))
    
    def handle_startendtag(self, tag, attrs):
        self.result.append("Empty : {}".format(tag))
        for t in attrs:
            self.result.append("-> {} > {}".format(t[0], t[1]))
    
    def get_result(self):
        return self.result

if __name__ == "__main__":
    parser = MyHTMLParser()
    with open(sys.path[0] + "/html_sample_1.txt") as f, \
        open(sys.path[0] + "/html_parse_1.expected") as fe:
        parser.feed("".join(f.readlines()))
        print(*parser.get_result(), sep = '\n')