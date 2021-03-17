import PyPDF2


def pdfwork():
    print()
    pdffile = open('Data\\meetingminutes1.pdf', 'rb') # pdfs are in binary
    reader = PyPDF2.PdfFileReader(pdffile)
    print(reader.numPages)
    page = reader.getPage(0)
    text = page.extractText()
    pages = {}
    for pagenum in range(reader.numPages):
        pages[pagenum] = reader.getPage(pagenum).extractText()
    pdffile.close()


def combinepdfs():
    pdffile1 = open('Data\\meetingminutes1.pdf', 'rb')
    pdffile2 = open('Data\\meetingminutes2.pdf', 'rb')
    reader1 = PyPDF2.PdfFileReader(pdffile1)
    reader2 = PyPDF2.PdfFileReader(pdffile2)
    # writer doesn't have a PDF file yet anywhere, no pages
    writer = PyPDF2.PdfFileWriter()
    for reader in (reader1, reader2):
        for pagenum in range(reader.numPages):
            page = reader.getPage(pagenum)
            writer.addPage(page)
    outputFile = open('Data\\newfile.pdf', 'wb')
    writer.write(outputFile)
    pdffile1.close()
    pdffile2.close()


def main():
    pdfwork()
    combinepdfs()


if __name__ == '__main__':
    main()
