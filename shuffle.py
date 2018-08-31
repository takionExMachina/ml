import os
import random

emails_list = []
Directory = '<put dir here>'
Dir_list = os.listdir(Directory)

for fi in Dir_list:
    f = open(Directory + fi, 'r')
    emails.append(f.read())
    f.close()

