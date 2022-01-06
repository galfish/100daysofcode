from prettytable import PrettyTable
table = PrettyTable()

table.add_column ("pokemon name", ["Pichu", "Simipour", "Bidoof"])
table.add_column ("Type", ["Electric", "Water", "Normal"])

table.align = "l"

print (table)


