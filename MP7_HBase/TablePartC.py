import happybase as hb
import csv


connection = hb.Connection()
connection.open()

table = connection.table('powers')

with open('input.csv', newline='') as f:
    for row in csv.reader(f, delimiter=','):
        table.put(b'%s' % row[0].encode(), {
            b'personal:hero': b'%s' % row[1].encode(),
            b'personal:power': b'%s' % row[2].encode(),
            b'professional:name': b'%s' % row[3].encode(),
            b'professional:xp': b'%s' % row[4].encode(),
            b'custom:color': b'%s' % row[5].encode()
        })

connection.close()