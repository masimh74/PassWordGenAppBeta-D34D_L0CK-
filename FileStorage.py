import sqlite3


class file_handler():
    def __init__(self, filename="database.db"):
        self.database = sqlite3.connect("database.db")
        self.cursor = self.database.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Users_Accounts(name, username, password, password_list)")

    def __enter__(self):
        return self

    def add_user(self, name: str, account: str, password: str):
        self.cursor.execute('SELECT name FROM Users_Accounts WHERE username = (?)', (account,))
        objects = self.cursor.fetchall()
        if objects:
            # print("user already exists on the database")
            return False
        else:
            self.cursor.execute('INSERT INTO Users_Accounts VALUES (?,?,?,?)', (name, account, password, ""))
            self.database.commit()
            # print("congrats")
            return True
    def add_password(self, account, site, username, password):
        prev = self.cursor.execute('''SELECT password_list FROM Users_Accounts WHERE username= (?)''', (account,))
        objects = self.cursor.fetchall()
        self.cursor.execute('UPDATE Users_Accounts SET password_list = (?) WHERE username = (?)',("{}{},{},{}/".format(objects[0][0], site, username,password) ,account))
        self.database.commit()
        # print(account,site,username,password)

    def user_exists(self, username:str, password: str):
        self.cursor.execute('SELECT name FROM Users_Accounts WHERE username = (?) and password = (?)', (username,password))
        objects = self.cursor.fetchall()
        return True if objects else False

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.database.close()

    def close(self):
        self.database.commit()
        self.database.close()
    def get_password(self, account):
        self.cursor.execute('''SELECT password_list FROM Users_Accounts WHERE username= (?)''', (account,))
        objects = self.cursor.fetchall()
        # print(objects[0][0])
        return objects[0][0].split("/")[:-1]


def main():
    with file_handler() as database:
        print(database.add_user("ssss11111", "11b", "1v"))
        print(database.user_exists('1b','1v'), database.user_exists("11b","1v"))
        database.add_password("11b",23,23,23)
        # database.add_password("11b",1,2,3)


        database.cursor.execute('''SELECT * FROM Users_Accounts''')
        objects = database.cursor.fetchall()
        print(objects,database.get_password("11b"))

    # print("Success")


if __name__ == "__main__":
    main()
