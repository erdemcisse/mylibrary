import streamlit as st
import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('library.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_name TEXT,
        book_no TEXT,
        student_name TEXT,
        matrikel_number TEXT
    )
''')
conn.commit()

# Function to add a new book
def add_book(book_name, book_no, student_name, matrikel_number):
    c.execute('INSERT INTO books (book_name, book_no, student_name, matrikel_number) VALUES (?, ?, ?, ?)',
              (book_name, book_no, student_name, matrikel_number))
    conn.commit()

# Function to delete a book
def delete_book(book_id):
    c.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()

# Function to get books
def get_books():
    c.execute('SELECT * FROM books')
    return c.fetchall()

# Layout and design improvements
st.title("📚 Library Management System")

# Sidebar for adding books
with st.sidebar:
    st.header("Add a New Book")
    with st.form(key='add_book_form'):
        book_name = st.text_input("Book Name")
        book_no = st.text_input("Book No")
        student_name = st.text_input("Student Name")
        matrikel_number = st.text_input("Matrikel Number")
        submit_button = st.form_submit_button(label="Add Book")
        if submit_button:
            add_book(book_name, book_no, student_name, matrikel_number)
            st.success("✅ Book added successfully!")

# Main page for book listing and deletion
st.header("📖 Book List")
books = get_books()
books_df = pd.DataFrame(books, columns=['ID', 'Book Name', 'Book No', 'Student Name', 'Matrikel Number'])
st.dataframe(books_df.style.format({'Matrikel Number': lambda x: f'{x}'}), height=300)

# Deletion section
with st.expander("Delete a Book"):
    if books:
        book_id_to_delete = st.selectbox("Select a Book ID to delete", [book[0] for book in books])
        if st.button("Delete Book"):
            delete_book(book_id_to_delete)
            st.success(f"🗑️ Book with ID {book_id_to_delete} deleted successfully!")
            st.experimental_rerun()
