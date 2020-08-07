import mysql.connector

print("******Welcome!😀 here you can have access to ((picto)) gallery database! \nwe will connect the picto database for"
      " you!******\n")
# print("******if you are willing to use this program, \nyou need to first create the database \"picto\" \nand add the tables using "
#       "the create.sql file in the project folder.******")
print("*****please enter the username and password for your mysql database:******")
user = input("username:")
password = input("password:")

print("******if you are willing to use this program, \nplease create a database beforehand and enter the name below:******")
print("******You can add the tables to your database using the \"create.sql\".\nyou can find it in the project folder.******")

db = input("database:")
mydb = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password,
    database=db
)


def primary_key(table, cursor):
    cursor.execute("describe " + table)
    for y in cursor:
        if y[3] == 'PRI':
            return y[0], y[1]


def func2(table, cursor):
    cursor.execute("describe " + table)
    u = []
    for y in cursor:
        if y[1].isnumeric():
           u.append("%d")
        else:
           u.append("%s")
    s = str(tuple(u))
    st = s.replace("'", "")
    return st


def func(table, cursor):
    cursor.execute("describe " + table)
    l = []
    for y in cursor:
        l.append(y[0] + " - " + y[1])
    return l


def func1(table, cursor):
    cursor.execute("describe " + table)
    l = []
    for y in cursor:
        l.append(y[0])
    return l


mycursor = mydb.cursor(buffered=True)
tables = ['art_piece', 'artist', 'auction', 'customer', 'exhibition', 'receipt']
choices = [1, 2, 3, 4, 5]
tables_dict = []
for t in tables:
    temp = func(t, mycursor)
    tables_dict.append({t: temp})
# print(tables_dict)
while True:
    print("please enter the 1 to 6 to choose the table you want to change")
    for i in range(6):
        print(i + 1, "-", tables[i])
    print("7 - Quit")
    choice1 = input()
    while not choice1.isnumeric():
        print("invalid input! try again!")
        choice1 = input()
    choice1 = int(choice1)
    while choice1 > 7 or choice1 < 1:
        print("invalid input, please try again!")
        choice1 = int(input())
    if choice1 == 7:
        print("See you soon!")
        break
    print("you have chosen the", tables[choice1 - 1], "table")
    print("please enter 1 to 4 to choose the action you want to do")
    print("1-Add a record\n2-Delete a record\n3-Update a record\n4-Show the records\n5-Quit")
    choice2 = input()
    while not choice2.isnumeric():
        print("invalid input! try again!")
        choice2 = input()
    choice2 = int(choice2)
    while choice2 > 4 or choice2 < 1:
        print("invalid input. please try again!")
        choice2 = int(input())
    if choice2 == 1:
        print("please enter the record info in the order below:")
        t = list(tables_dict[choice1 - 1].values())
        print(*t[0])
        li = []
        for i in range(len(t[0])):
            print(t[0][i] + "?")
            attr = input()
            if attr.isnumeric():
                attr = int(attr)
            li.append(attr)
        val = tuple(li)
        vals = func2(tables[choice1-1], mycursor)
        # print(vals)
        sql = "INSERT INTO " + tables[choice1-1] + " VALUES " + str(vals)
        # print(sql)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except mysql.connector.errors.IntegrityError:
            print("unable to add the record! please try again!")
    if choice2 == 2:
        primkey, typekey = primary_key(tables[choice1-1], mycursor)
        print("the primary key is", primkey)
        print("please enter the value of the record's primary key you wish to delete:")
        key = input()
        try:
            if not typekey == 'int(11)':
                key = "'"+key+"'"
            delete = "DELETE FROM " + tables[choice1-1] + " WHERE " + primkey + " = " + key
            print(delete)
            mycursor.execute(delete)
            mydb.commit()
            print(mycursor.rowcount, "record(s) deleted")
        except mysql.connector.errors.InternalError:
            print("\n###the record does not exist!###\n")
    if choice2 == 3:
        primkey, typekey = primary_key(tables[choice1 - 1], mycursor)
        print("the primary key is", primkey)
        print("please enter the value of the record's primary key you wish to update:")
        key = input()
        print("please choose the key you want to change its value for the specified record:")
        tmp = func1(tables[choice1 - 1], mycursor)
        tmp1 = func(tables[choice1 - 1], mycursor)
        print(tmp)
        counter = 1
        for x in tmp:
            print(counter, "-", x)
            counter += 1
        choice3 = int(input())
        while choice3 > len(tmp) or choice3 < 1:
            print("invalid input! please try again!")
            choice3 = int(input())
        try:
            if not typekey == 'int(11)':
                key = "'" + key + "'"
            print("please enter the new value:")
            new_val = input()
            if tmp1[choice3-1].count('int(11)') == 0:
                new_val = "'" + new_val + "'"
            update = "UPDATE " + tables[choice1-1] + " SET " + tmp[choice3-1] + " = " + new_val +" WHERE " + primkey + " = " + key
            print(update)
            mycursor.execute(update)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
        except mysql.connector.errors.InternalError:
            print("###the action did not complete! please try again!###")
    if choice2 == 4:
        select = "SELECT * FROM " + tables[choice1-1]
        print(select)
        mycursor.execute(select)
        my_result = mycursor.fetchall()
        for x in my_result:
            print(x)
    if choice2 == 5:
        print("See you soon!")
        break






