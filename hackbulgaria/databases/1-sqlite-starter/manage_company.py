import sys
import sqlite3

db = sqlite3.connect("mydatabase.db")
cursor = db.cursor()

def main():
    exit_status = True
    while exit_status == True:
        command = input("command>")
        if command == 'exit':
            exit_status = False
            print('Buy')
        elif command == 'help':
            print_help()
        elif command == 'list_employees':
            list_employees()
        elif command == 'monthly_spending':
            print('The company is spending ${} every month!'.format(monthly_spending()))
        elif command == 'yearly_spending':
            print('The company is spending ${} every year!'.format(yearly_spending()))
        elif command == 'add_employee':
            name = input("name>")
            monthly_salary = input("monthly_salary>")
            yearly_bonus = input("yearly_bonus>")
            position = input("position>")
            add_employee(name,monthly_salary, yearly_bonus, position)
        elif command == 'delete_employee':
            ident = input("id>")
            delete_employee(ident)
        elif command == 'update_employee':
            employee_id = input("id>")
            update_employee(employee_id)
        else:
            print("lol")


def list_employees():
    for row in cursor.execute('''SELECT name, position FROM users'''):
        print('{0} : {1}'.format(row[0], row[1]))

def monthly_spending():
    salaries = 0
    for row in cursor.execute('''SELECT monthly_salary FROM users'''):
        salaries += row[0]
    return salaries

def yearly_spending():
    return monthly_spending()*12

def add_employee(name,monthly_salary, yearly_bonus, position):
    cursor.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', (name,monthly_salary, yearly_bonus, position))
    print('user inserted')
    db.commit()

def delete_employee(delete_userid):
    cursor.execute('''DELETE FROM users WHERE id = ? ''', (delete_userid,))
    db.commit()

#none
def update_employee(id):
    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")
    cursor.execute('''UPDATE name, monthly_salary, yearly_bonus, position 
        SET ?, ?, ?, ? WHERE id = ? ''',
     (name, monthly_salary, yearly_bonus, position, userid))
    db.commit()

def print_help():
    print('list_employees - Prints out all employees, in the following format - "name - position"')
    print('monthly_spending - Prints out the total sum for monthly spending that the company is doing for salaries')
    print('yearly_spending - Prints out the total sum for one year of operation (Again, salaries)')
    print('add_employee, the program starts to promt for data, to create a new employee.')
    print('delete_employee <employee_id>, the program should delete the given employee from thje database')
    print('update_employee <employee_id>, the program should prompt the user to change each of the fields ')
    print('exit - exit program')

if __name__ == '__main__':
    main()