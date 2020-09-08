from html.parser import HTMLParser
import sys

class MyHTMLParser(HTMLParser):
    def __init__(self, convert_charrefs=True):
        super(MyHTMLParser, self).__init__(convert_charrefs=True)
        self.result = []

    def handle_comment(self, comment):
        parts = comment.split(sep = "\n")
        if len(parts) > 1:
            self.result.append(">>> Multi-line Comment")
            for l in parts:
                self.result.append(l)
        else:
            self.result.append(">>> Single-line Comment")
            self.result.append(parts[0])

    def handle_data(self, data):
        if data.strip():
            self.result.append(">>> Data")
            self.result.append(data)
    
    def get_result(self):
        return self.result

if __name__ == "__main__":
    parser = MyHTMLParser()
    with open(sys.path[0] + "/html_sample_2.txt") as f:
        parser.feed("".join(f.readlines()))
        print(*parser.get_result(), sep = '\n')