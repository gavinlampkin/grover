#!/usr/bin/env python3
import csv
import argparse
import string
import pandas as pd
from string import Template

template = Template("""\
{"article": "${article}","domain": "${domain}","title": "${title}","date": "${publish_date}","authors": "${authors}",\
"ind30k": "${ind30k}","url": "${url}","label": "${label}","orig_split": "${orig_split}","split": "${split}","random_score": ${random_score}}
""")

def sanitize(obj):
    # Do we need to sanitize anything else for JSON?
    # https://www.tutorialspoint.com/json_simple/json_simple_escape_characters.htm
    return str(obj).replace("\\","\\\\").replace("\n","\\n").replace("\"","").replace("\r","").replace("\t","")

if __name__ == '__main__':
  # Handle input arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', "--input",help="specify input path")
  parser.add_argument("output",help="specify output path")
  args = parser.parse_args()
  
  # Read dataframe using Pandas
  dataframe = pd.read_excel(args.input)
  print(dataframe)
  
  jsonOut = ""
  
  # Break into rows
  for index, row in dataframe.iterrows():
    _article = sanitize(row["article"])
    _domain = row["domain"]
    _title = sanitize(row["title"])
    _publish_date = "9/27/16" #row["publish_date"]
    _authors = sanitize(row["authors"])
    _ind30k = row["ind30k"]
    _url = row["url"]
    _label = row["label"]
    _orig_split = row["orig_split"]
    _split = row["split"]
    _random_score = row["random_score"]
    
    jsonOut += template.substitute(article = _article, domain=_domain, title=_title, publish_date=_publish_date, authors=_authors, ind30k=_ind30k, url=_url, label=_label, orig_split=_orig_split, split=_split, random_score=_random_score)
  
  jsonOut += ""
  
  # Exclude non-ascii chars from data
  jsonOut = ''.join(i for i in jsonOut if ord(i)<128)
  
  # Print to file
  print("Writeing formated content to {}".format(args.output))
  with open(args.output, "w") as text_file:
    text_file.write(jsonOut)
  
