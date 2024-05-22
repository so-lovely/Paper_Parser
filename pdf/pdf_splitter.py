# %%
import pymupdf4llm
from langchain.text_splitter import MarkdownTextSplitter
import threading
import os

# %%
Data = []

# %%
lock = threading.Lock()

# %%
def split(path:str, chunk_size, chunk_overlap) -> list:
 # get markdown for all pages
    splitter = MarkdownTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    lock.acquire()
    Document = splitter.create_documents([pymupdf4llm.to_markdown(path)])
    lock.release()
    lock.acquire()
    Data.append(Document)
    lock.release()

def threads_process(folder_path:str, chunk_size, chunk_overlap):
    files = os.listdir(folder_path)
    length = len(files)
    i = 0
    threads = []
    while (not i == length):
        path = folder_path + '/' + files[i]
        thread = threading.Thread(target=split, args=(path, chunk_size, chunk_overlap)) 
        threads.append(thread)
        thread.start()
        i = i + 1
    return threads

# %%
def pdf_splitter(dir_path:str | list[str], chunk_size, chunk_overlap):
    threads = threads_process(dir_path, chunk_size, chunk_overlap)
    for thread in threads:
        thread.join()
    print('finish')
    return Data


