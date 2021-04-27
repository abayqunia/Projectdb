import psycopg2

#Connect to db
con = psycopg2.connect (
    host = "localhost",
    port = 5432,
    database= "test",
    user = "postgres",
    password = "meja1234")
#connect cur
cur = con.cursor()

print(" Program Demo Operasi CRUD SQLite Database ")
print("       Achmad Bayquni Alfarisi           ")
print("       (19/447309/SV/17003) ARM 1           ")
print("===========================================\n")
print("Menu Operasi Database :")
print("1. Create Database dan Tabel")
print("2. Insert Data")
print("3. Select/Search Data")
print("4. Update Data")
print("5. Delete Data\n")
menu=input("Silahkan pilih Operasi ( 1 / 2 / 3 / 4 / 5 ) = ")
print("Operasi Yang Dipilih : " + menu)

#pilihan
if menu=='1':
    print("Create Database dan Tabel")
    con = psycopg2.connect (
    host = "localhost",
    port = 5432,
    database= "test",
    user = "postgres",
    password = "meja1234")
    cur = con.cursor()
    #create table
    cur.execute("CREATE TABLE tambahan (nama VARCHAR(60), nilai INTEGER NOT NULL)")
    con.commit()
elif menu=='2':
    print("Insert Data")
    con = psycopg2.connect (
    host = "localhost",
    port = 5432,
    database= "test",
    user = "postgres",
    password = "meja1234")
    cur = con.cursor()
    cur.execute('''INSERT INTO spare (nama, harga, stok) VALUES ('tromol', '75000', '4');''')
    con.commit()
elif menu=='3':
    print("Select/Search Data")
    con = psycopg2.connect (
    host = "localhost",
    port = 5432,
    database= "test",
    user = "postgres",
    password = "meja1234")
    cur = con.cursor()
    cur.execute("""SELECT * FROM spare""")
    query_res = cur.fetchall()
    print(query_res)
elif menu=='4':
    print("Update Data")
    con = psycopg2.connect (
    host = "localhost",
    port = 5432,
    database= "test",
    user = "postgres",
    password = "meja1234")
    cur = con.cursor()
    sql1="UPDATE spare SET nama = 'lampu' WHERE id = 4"
    cur.execute(sql1)
    con.commit()
    print(sql1)
elif menu=='5':
    print("Delete Data")
    con = psycopg2.connect (
    host = "localhost",
    port = 5432,
    database= "test",
    user = "postgres",
    password = "meja1234")
    cur = con.cursor()
    sql2 = "DELETE FROM spare WHERE id = 4"
    cur.execute(sql2)
    con.commit()
    print(sql2)
else :
    print("Perintah Yang Dimasukkan Salah")


#close cur connection
cur.close()
#close the connection
con.close()