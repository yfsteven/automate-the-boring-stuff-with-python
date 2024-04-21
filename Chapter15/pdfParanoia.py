#! python3
# pdfParanoia.py - Encrypt every pdf file and decrypt every pdf file

import os, sys, PyPDF2
def encryptPdf(name, passwd):
    pdf_file = open(name, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_writer = PyPDF2.PdfWriter()
    for pageNum in range(len(pdf_reader.pages)):
        pageObj = pdf_reader.pages[pageNum]
        pdf_writer.add_page(pageObj)
    pdf_writer.encrypt(passwd)
    encrypted_pdf = open('encrypted'+name,'wb')
    pdf_writer.write(encrypted_pdf)
    encrypted_pdf.close()
if len(sys.argv) == 2:
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name.endswith('.pdf') and 'encrypted' not in name:
                encryptPdf(name, sys.argv[1])
        for name in dirs:
            if name.endswith('.pdf') and 'encrypted' not in name:
                encryptPdf(name, sys.argv[1])

def decrypter(passwd):
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name.endswith('.pdf') and name.startswith('encrypted'):
                pdf_file = open(name, 'rb')
                pdf_writer = PyPDF2.PdfWriter()
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                try:
                    pdf_reader.decrypt(passwd)
                    for pageNum in range(len(pdf_reader.pages)):
                        pageObj = pdf_reader.pages[pageNum]
                        pdf_writer.add_page(pageObj)
                    decrypted_pdf = open('decrypted'+name,'wb')
                    pdf_writer.write(decrypted_pdf)
                    decrypted_pdf.close()
                except Exception as err:
                    print('Wrong password for ' + name + ' ' + str(err))
        for name in dirs:
            if name.endswith('.pdf') and name.startswith('encrypted'):
                pdf_file = open(name, 'rb')
                pdf_writer = PyPDF2.PdfWriter()
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                try:
                    pdf_reader.decrypt(passwd)
                    for pageNum in range(len(pdf_reader.pages)):
                        pageObj = pdf_reader.pages[pageNum]
                        pdf_writer.add_page(pageObj)
                    decrypted_pdf = open('decrypted'+name,'wb')
                    pdf_writer.write(decrypted_pdf)
                    decrypted_pdf.close()
                except Exception as err:
                    print('Wrong password for ' + name + ' ' + str(err))
