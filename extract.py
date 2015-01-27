#!/usr/bin/env python
import sqlite3
import os

conn = sqlite3.connect('resources.meta')
dirs = 'res_ext'

cur = conn.cursor()
cur.execute('SELECT * FROM file_information')

if not os.path.exists(dirs):
    os.makedirs(dirs)

old_index = -1

for row in cur:
    resource_id = row[0]
    file_index = row[1]
    file_size = row[2]
    file_begin = row[3]

    if old_index < file_index:
        old_index = file_index
        if 'f' in locals():
            f.close()
        if os.path.isfile('resources.d00' + str(old_index)):
            f = open('resources.d00'+ str(old_index), 'rb')

    f.seek(file_begin)
    mem = f.read(file_size)

    p = dirs + '/' + resource_id

    if not os.path.exists(os.path.dirname(p)):
        os.makedirs(os.path.dirname(p))

    o = open(p, 'w')
    o.write(mem)
    o.close()

conn.close()

