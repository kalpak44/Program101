import sqlite3

db = sqlite3.connect("mydatabase.db")
cursor = db.cursor()

name1 = 'Petyr Ivanov'
monthly_salary1 = 5000
yearly_bonus1 = 10000
position1 = 'Software Developer'

name2 = 'Rado Rado'
monthly_salary2 = 500
yearly_bonus2 = 0
position2 = 'Technical Support Intern'

name3 = 'Ivo Ivo'
monthly_salary3 = -500
yearly_bonus3 = 0
position3 = 'Student'

name4 = 'Marketing Manager'
monthly_salary4 = 800
yearly_bonus4 = 200
position4 = 'Software Developer'





# Insert user 1
cursor.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', (name1,monthly_salary1, yearly_bonus1, position1))
print('user inserted')
 # Insert user 2
cursor.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', (name2,monthly_salary2, yearly_bonus2, position2))
print('user inserted')
 # Insert user 3
cursor.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', (name3,monthly_salary3, yearly_bonus3, position3))
print('user inserted')
 # Insert user 4
cursor.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', (name4,monthly_salary4, yearly_bonus4, position4))
print('user inserted')
db.commit()