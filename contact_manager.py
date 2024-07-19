import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import messagebox

# Initialize the database connection
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('contacts.db')
    except Error as e:
        print(e)
    return conn

# Create the contacts table
def create_table(conn):
    try:
        sql_create_contacts_table = """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        );
        """
        conn.execute(sql_create_contacts_table)
    except Error as e:
        print(e)

# Add a new contact
def add_contact(conn, contact):
    sql = '''INSERT INTO contacts(name, phone, email) VALUES(?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()
    return cur.lastrowid

# View all contacts
def view_contacts(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    return rows

# Search contacts by name or phone
def search_contacts(conn, query):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", ('%' + query + '%', '%' + query + '%'))
    rows = cur.fetchall()
    return rows

# Update a contact
def update_contact(conn, contact):
    sql = '''UPDATE contacts
             SET name = ?,
                 phone = ?,
                 email = ?
             WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()

# Delete a contact
def delete_contact(conn, id):
    sql = 'DELETE FROM contacts WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

# Main Application
class ContactManagerApp:
    def __init__(self, root):
        self.conn = create_connection()
        if self.conn is not None:
            create_table(self.conn)
        else:
            print("Error! Cannot create the database connection.")
            return

        self.root = root
        self.root.title("Contact Manager")

        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(root, text="Email")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=4, column=0, columnspan=2)

        self.search_label = tk.Label(root, text="Search")
        self.search_label.grid(row=5, column=0)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=5, column=1)

        self.search_button = tk.Button(root, text="Search", command=self.search_contacts)
        self.search_button.grid(row=6, column=0, columnspan=2)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2)

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.grid(row=9, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone:
            contact = (name, phone, email)
            add_contact(self.conn, contact)
            messagebox.showinfo("Success", "Contact added successfully")
        else:
            messagebox.showerror("Error", "Name and Phone are required")

    def view_contacts(self):
        rows = view_contacts(self.conn)
        self.result_text.delete(1.0, tk.END)
        for row in rows:
            self.result_text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}\n")

    def search_contacts(self):
        query = self.search_entry.get()
        rows = search_contacts(self.conn, query)
        self.result_text.delete(1.0, tk.END)
        for row in rows:
            self.result_text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}\n")

    def update_contact(self):
        id = self.search_entry.get()
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if id and name and phone:
            contact = (name, phone, email, id)
            update_contact(self.conn, contact)
            messagebox.showinfo("Success", "Contact updated successfully")
        else:
            messagebox.showerror("Error", "ID, Name, and Phone are required")

    def delete_contact(self):
        id = self.search_entry.get()
        if id:
            delete_contact(self.conn, id)
            messagebox.showinfo("Success", "Contact deleted successfully")
        else:
            messagebox.showerror("Error", "ID is required")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
