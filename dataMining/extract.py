import PyPDF2
with open("user_score.csv.pdf", "rb") as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    print(page.extractText())
