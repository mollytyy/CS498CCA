import happybase as hb


connection = hb.Connection()
connection.open()

print(connection.tables())