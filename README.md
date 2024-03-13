# mylibrary

## Access to MyLibrary (Library Management System) Version 2.0: https://mylibrary-85a6syqubi3dwkusrmktf8.streamlit.app/

## What's New in Version 2.0

I am excited to release version 2.0 of my Library Management System built with Streamlit! 🎉

### New Features & Improvements
- **Redesigned User Interface**: We've overhauled the UI to make it cleaner, more organized, and user-friendly.
  - New books are now added through a sidebar, making the main page focused on your library's catalog.
  - Book deletion has been moved to an expandable section that you can open as needed.
  - Visual enhancements like headers, emojis, and styled tables make the app more pleasant to use.

- **Enhanced Feedback**: Clear and immediate feedback is provided after adding or deleting books, so you always know what's happening.

- **Optimized Performance**: Deleting a book now refreshes only the relevant parts of the app, making your interactions faster and smoother.


### Changes in Version 2.0:
  
  **Design Overhaul:**

 - Implemented st.sidebar for adding new books, which helped de-clutter the main page and provided a dedicated space for book entry.
 - Used st.expander to neatly hide the delete functionality until the user chooses to use it, reducing initial information overload.
 - Added a header and emojis to sections for a friendlier and more engaging user interface.
 - Introduced a styled st.dataframe to display the list of books with improved readability.
  
  **Usability Improvements:**

 - Included form submission within the sidebar to ensure that the UI is more intuitive and the form inputs are grouped logically.
 - Provided clear success messages with icons for better user feedback when actions (add/delete) are performed.
  
  **Code Enhancements:**

 - Organized the code into more logical sections using Python comments, making it easier for future developers to understand and maintain.
 - Applied better variable naming conventions to enhance code readability and maintainability.

  **Performance Optimization:**

 - Added st.experimental_rerun() to refresh the page and the displayed list of books after a book is deleted without having to manually refresh the entire page.


### MyLibrary Version 1.0 > https://mylibrary-jt9eyw33czxc3itdyru8zz.streamlit.app/

**Version 1.0 Functions:**
  
 - init_db(conn): Initialize the database and create the books table if it doesn't exist.
 - add_book(conn, book_name, book_no, student_name, matrikel_number): Add a new book record to the database.
 - delete_book(conn, book_id): Delete a book record from the database based on its ID.
 - get_all_books(conn): Retrieve all book records from the database and return them.
 - Streamlit UI to add a new book, delete a book, and display the list of books.
