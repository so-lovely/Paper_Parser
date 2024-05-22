from pdf_splitter import pdf_splitter
if __name__ == '__main__':
    print('hi')
    dir = '/Users/user/Documents/paper_parser/pdf/pdf_data/Computational Finance'
    returns = pdf_splitter(dir,40, 0)
    print(len(returns))