import psycopg2

#Connect to the db
con = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database= "test",
    user = "postgres",
    password = "meja1234")

#Cursor
cur = con.cursor()

print(" Program Demo Operasi CRUD SQLite Database ")
print("       Achmad Bayquni Alfarisi           ")
print("         19/447309/SV/17003           ")
print("                ARM 1           ")
print("===========================================\n")
print("Menu Operasi Database :")
print("1. Create Database dan Tabel")
print("2. Insert Data")
print("3. Select/Search Data")
print("4. Update Data")
print("5. Delete Data\n")
menu=input("Silahkan pilih Operasi ( 1 / 2 / 3 / 4 / 5 ) = ")
print("Operasi Yang Dipilih : " + menu)


#Menu Pilihan
if menu=='2' :
print("Insert Data")
con = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database= "test",
    user = "postgres",
    password = "meja1234")
cur = con.cursor()
cur.execute('''INSERT INTO person (name, password, status) VALUES ('biba', 'alulila', 'active');''')
con.commit()

#Cur Close
cur.close()
#close the connection
con.close()
