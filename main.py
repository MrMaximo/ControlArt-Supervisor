# Importing libraries
import sqlite3
from Module import module

# Configuration File
config_File = 'Alexandre.ca'

# Connecting to the configuration file
conn = sqlite3.connect(config_File)
cursor = conn.cursor()

#List of Modules
modules = []

#Reading Module's data from DB
row = cursor.execute("""SELECT id, hdw_addr, serial_number FROM module;""")

# For each row readed at the database, create the object and append to the module
for row in cursor:
    m = module(row[0], row[1], row[2])
    modules.append(m)

# Printing list of modules
#for x in range(len(modules)):
#    print(str(modules[x].getID()) + " " + modules[x].getMAC() + " " +modules[x].getSerialNumber())
    
conn.close()