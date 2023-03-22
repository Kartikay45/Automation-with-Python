
import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate



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




