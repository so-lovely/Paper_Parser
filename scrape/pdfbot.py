import linkbot
import requests

class Pdfbot:
    def __init__(self):
        self.response = None
        
    def response(self, pdf_lnk):
         self.response = requests(pdf_lnk)

    async def get_pdf(self, response, file_name):

        pdf_name = file_name + '.pdf'

        with open(pdf_name, "wb") as f:
            f.write(self.response.content)