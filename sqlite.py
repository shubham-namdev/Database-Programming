"""
-> SQLite3
"""
import sqlite3

conn = sqlite3.connect("database.db") # returns a connection object

c = conn.cursor()

#c.execute(""" CREATE TABLE persons (
#first_name TEXT, 
#last_name TEXT,
#age INTEGER
#)
#""")

#c.execute(""" INSERT INTO persons VALUES
#('Jerry', 'Nelson', 78),
#('Zach', 'Nelson', 35),
#('Cambrey', 'Nelson', 30)
#""")

c.execute(""" SELECT * from persons
""")

print(c.fetchall())

"""
>> fetchall()  - fetches all records
>> fetchone()  - fetches one record
>> fetchmany(x) - fetches many records
"""
conn.commit()
conn.close()


"""
-> Creating Database Class and Objects
"""

import sqlite3


class Person():
    def __init__(self, f_name: int = None, l_name: int = None,
                  age: int = None) -> None:
        self.first = f_name
        self.last = l_name
        self.age = age
    
    def clone(self, sequence :tuple) -> None:
        self.first = sequence[0]
        self.last = sequence[1]
        self.age = sequence[2]

conn = sqlite3.connect("database.db")
c = conn.cursor()

# ~ Table to Object

c.execute(""" SELECT * FROM persons
""")

person1 = Person()
person1.clone(c.fetchone())

print(person1.first)
print(person1.last)
print(person1.age)

# ~ Object to Table

person2 = Person("Cyrus", "Nelson", 2)

c.execute("""INSERT INTO persons VALUES
('{}', '{}', '{}')
""".format(person2.first, person2.last, person2.age))

conn.commit()

c.execute(""" SELECT * from persons
""")

print(c.fetchall())


# -> Prepared Statements
#>> a much more secure and elegant way to put the values of our
#>> attributes into the SQL statements.

person = Person("Carter", "Horse", 15)

c.execute("INSERT INTO persons VALUES (?, ?, ?)", (person.first, person.last, person.age))

conn.commit()
c.execute(""" SELECT * from persons
""")

print(c.fetchall())
conn.close()