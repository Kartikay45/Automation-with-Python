import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate
from docx2pdf import convert


doc = DocxTemplate("Offer letter.docx")
#mi_name = "..........."
#mi_number = "........."
#mi_adress = "........."
today_date = datetime.today().strftime("%d %b, %Y")

my_context = {#'mi_name': mi_name, 'mi_number': mi_number, 'mi_adress': mi_adress,
              'today_date': today_date}

df = pd.read_csv('Example.csv')

for index, row in df.iterrows():
    context = {'name': row['names'],
               'job_title': row['internship']}
               

    context.update(my_context)

    doc.render(context)
    doc.save(f"doc_generated_{index}.docx")

a=input()
b=input()
c=input()
d=input()
e=input()


convert(r"C:\Users\hp\Desktop\CODUTION\doc_generated_"+a+".docx",r"C:\Users\hp\Desktop\CODUTION\doc_generated_"+a+"_pdf_converted_file.pdf")
convert(r"C:\Users\hp\Desktop\CODUTION\doc_generated_"+b+".docx",r"C:\Users\hp\Desktop\CODUTION\doc_generated_"+b+"_pdf_converted_file.pdf")
convert(r"C:\Users\hp\Desktop\CODUTION\doc_generated_"+c+".docx",r"C:\Users\hp\Desktop\CODUTION\doc_generated_"+c+"_pdf_converted_file.pdf")
convert(r"C:\Users\hp\Desktop\CODUTION\doc_generated_"+d+".docx",r"C:\Users\hp\Desktop\CODUTION\doc_generated_"+d+"_pdf_converted_file.pdf")
convert(r"C:\Users\hp\Desktop\CODUTION\doc_generated_"+e+".docx",r"C:\Users\hp\Desktop\CODUTION\doc_generated_"+e+"_pdf_converted_file.pdf")



