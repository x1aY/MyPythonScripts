from urllib.request import urlopen
from urllib.request import Request
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser, PDFDocument


def OnlinePdf2TextList(_path):
    praser_pdf, doc = PDFParser(urlopen(Request(url=_path))), PDFDocument()
    praser_pdf.set_document(doc), doc.set_parser(praser_pdf), doc.initialize()
    textList = []
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        device = PDFPageAggregator(rsrcmgr, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            if layout != None:
                for out in layout:
                    if isinstance(out, LTTextBoxHorizontal):
                        textList.append(out.get_text())
    return textList
