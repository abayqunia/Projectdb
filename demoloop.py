import psycopg2

print(" Program Demo Operasi CRUD SQLite Database ")
print("       Achmad Bayquni Alfarisi            ")
print("       (19/447309/SV/17003) ARM 1         ")
print("===========================================")
def main() :
    print("\nMenu operasi database")
    print("1. Create database dan tabel")
    print("2. Insert data")
    print("3. Select/search data")
    print("4. Update data")
    print("5. Delete data")
    menu=input("Silahkan pilih operasi ( 1 / 2 / 3 / 4 /5 ) = ")
    print("Pilihan Yang Dipilih = " + menu)
    if menu=='1' :
        print("Create database dan tabel")
        con = psycopg2.connect (
        host = "localhost",
        port = 5432,
        database= "test",
        user = "postgres",
        password = "meja1234")
        cur = con.cursor()
        #create table
        cur.execute("CREATE TABLE tambahan1 (nama VARCHAR(60), nilai INTEGER NOT NULL)")
        con.commit()
    elif menu=='2' :
        print("Insert data")
        con = psycopg2.connect (
        host = "localhost",
        port = 5432,
        database= "test",
        user = "postgres",
        password = "meja1234")
        cur = con.cursor()
        cur.execute('''INSERT INTO spare (nama, harga, stok) VALUES ('busi', '75000', '5');''')
        con.commit()
    elif menu=='3' :
        print("Select/search data")
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
    elif menu=='4' :
        print("Update data")
        con = psycopg2.connect (
        host = "localhost",
        port = 5432,
        database= "test",
        user = "postgres",
        password = "meja1234")
        cur = con.cursor()
        sql1="UPDATE spare SET nama = 'karbo' WHERE id = 5"
        cur.execute(sql1)
        con.commit()
        print(sql1)
    elif menu=='5' :
        print("Delete data")
        con = psycopg2.connect (
        host = "localhost",
        port = 5432,
        database= "test",
        user = "postgres",
        password = "meja1234")
        cur = con.cursor()
        sql2 = "DELETE FROM spare WHERE id = 5"
        cur.execute(sql2)
        con.commit()
        print(sql2)

    lagi=input("\nApakah Anda Ingin Melanjutkan Program (Y/T) = ")
    if lagi.lower() == "y" :
        main ()
    else :
        print("Program Selesai")
    
main()