import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection()
connection.open()

table = connection.table('powers')

for key, data in table.scan(include_timestamp=True):
    print('Found: {}, {}'.format(key, data))

