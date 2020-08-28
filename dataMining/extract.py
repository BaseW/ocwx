import PyPDF2
with open("course_list.csv.pdf", "rb") as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    print(page.extractText())
