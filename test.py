# %%
import pymupdf4llm
from langchain.text_splitter import MarkdownTextSplitter
import asyncio
from typing import List

# %%
async def split(path: str) -> list:
    path = path + '.pdf'
    md_text = pymupdf4llm.to_markdown(path)  # get markdown for all pages
    print("type: ", type(md_text))
    splitter = MarkdownTextSplitter(chunk_size=40, chunk_overlap=0)
    documents = splitter.create_documents([md_text])
    return documents

async def cooru_obj(dir_path: str, i: int) -> List:
    tasks = []
    for j in range(i):
        path = dir_path + str(j + 1)
        tasks.append(split(path))
    return await asyncio.gather(*tasks)

# %%
if __name__ == '__main__':
    dir_path = 'pdf/pdf_data/Computational Finance/'
    i = 3
    result = asyncio.run(cooru_obj(dir_path, i))
    print(result)
