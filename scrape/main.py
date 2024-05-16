# %%
from linkbot import linkbot
import pdfbot
from dotenv import load_dotenv
import os

# %%
if __name__ == '__main__':
    load_dotenv()
    start_url = os.environ.get('SERVER')
    print(start_url)
    lnkbot = Linkbot(start_url) 
    pdfbot = pdfbot()
    lnkbot.startpoint_load()
    lnkbot.find_elements_by_tag_a()
    lnkbot.filter_href()  #Save ids and texts
    ids = lnkbot.get_ids() #get_ids fun -> arg:elements or element
    for id in lnkbot.current_element.values(id):
        lnkbot.find_element_by_id(id)
        lnkbot.get_text_from_element()
        lnkbot.click_element() #page_url is changed,add code in the class
        pdf_function_hash = lnkbot.find_elements_by_link_text('pdf')
        pdf_lnks = lnkbot.filter_href(hash=pdf_function_hash)
        for pdf_lnk in pdf_lnks:
            response = pdfbot.response(pdf_lnk)
            await pdfbot.get_pdf(response=response, file_name=lnkbot.current_element.values(text))
        lnkbot.back()
    lnkbot.quit()


