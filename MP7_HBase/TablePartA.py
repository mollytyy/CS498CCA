import happybase as hb

connection = hb.Connection()
connection.open()

# Table 1
connection.create_table(
    "powers",
    {'personal' : dict(),
     'professional' : dict(),
     'custom' : dict(),
    }
)

# Table 2
connection.create_table(
    "food",
    {'nutrition' : dict(),
     'taste' : dict()
     }
)

