import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection()
connection.open()

table = connection.table('powers')

# Id: "row1", Values for (hero, power, name, xp, color)
q1 = table.row(b'row1')

hero = q1[b'personal:hero']
power = q1[b'personal:power']
name = q1[b'professional:name']
xp = q1[b'professional:xp']
color = q1[b'custom:color']

print('hero: {}, power: {}, name: {}, xp: {}, color: {}'.format(hero, power, name, xp, color))

# Id: "row19", Values for (hero, color)
q19 = table.row(b'row19')

hero = q19[b'personal:hero']
color = q19[b'custom:color']

print('hero: {}, color: {}'.format(hero, color))

# Id: "row1", Values for (hero, name, color)

hero = q1[b'personal:hero']
name = q1[b'professional:name']
color = q1[b'custom:color']
print('hero: {}, name: {}, color: {}'.format(hero, name, color))