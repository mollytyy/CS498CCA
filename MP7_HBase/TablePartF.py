import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection()
connection.open()

table = connection.table('powers')

for key, data in table.scan():
    for key1, data1 in table.scan():
        if data[b'custom:color'] == data1[b'custom:color'] and data[b'professional:name'] != data1[b'professional:name']:
            name = data[b'professional:name']
            power = data[b'personal:power']
            name1 = data1[b'professional:name']
            power1 = data1[b'personal:power']
            color = data[b'custom:color']
            print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))
