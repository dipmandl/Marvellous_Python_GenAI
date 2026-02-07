#Duck Typing: It is a concept where the type of an object
#determined by its behaviour, not by its class

class InkjetPrinter():
    def printdocument(self,document):
        print("Inject printer printing : ",document)

class LaserPrinter():
    def printdocument(self, document):
        print("Laser printer printing : ", document)

class PDFWriter():
    def printdocument(self, document):
        print(f"Saving {document} As PDF")

def start_printing(Device):
    Device.printdocument("Marvellous Notes")

def main():
    start_printing(InkjetPrinter())
    start_printing(LaserPrinter())
    start_printing(PDFWriter())

main()

