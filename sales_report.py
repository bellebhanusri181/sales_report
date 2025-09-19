import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    date TEXT,
    amount REAL
)
""")
conn.commit()

def add_sale():
    product = input("Enter product name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    amount = float(input("Enter amount: "))
    cursor.execute("INSERT INTO sales (product, date, amount) VALUES (?, ?, ?)", (product, date, amount))
    conn.commit()
    print("Sale added!\n")

def view_sales():
    cursor.execute("SELECT * FROM sales")
    for row in cursor.fetchall():
        print(row)
    print()

def product_summary():
    cursor.execute("SELECT product, SUM(amount) FROM sales GROUP BY product")
    print("\nTotal Sales by Product:")
    for row in cursor.fetchall():
        print(f"{row[0]} - {row[1]}")
    print()

while True:
    print("1. Add Sale")
    print("2. View All Sales")
    print("3. Show Product Summary")
    print("0. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_sale()
    elif choice == "2":
        view_sales()
    elif choice == "3":
        product_summary()
    elif choice == "0":
        break
    else:
        print("Invalid choice!\n")

conn.close()
