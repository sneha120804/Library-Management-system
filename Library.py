from datetime import datetime
import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self, List_of_Books):
        self.books = List_of_Books

    def display_available_Books(self):
        print("\n---Books currently available in the library..")
        for index, book in enumerate(self.books, 1):
            print(f"{index}.{book}")

    def lend_book(self, requested_book):
        for book in self.books:
            if book.lower() == requested_book.lower():
                print(
                    f"Congratulations! Your requested book is available "
                    f"'{book}' Please collect your book"
                )
                self.books.remove(book)
                return True

        print(
            f"Sorry!! Your requested book '{requested_book}' "
            f"is not available in the library.."
        )
        return False

    def add_book(self, returned_books):
        self.books.append(returned_books)
        print(
            f"Thanks for returning the book "
            f"'{returned_books}' to the Library.."
        )

    def search_book(self, book_name):
        for book in self.books:
            if book.lower() == book_name.lower():
                print(f"'{book}' is available in the library.")
                return True

        print(f"'{book_name}' is not available.")
        return False

    def total_books(self):
        print(f"\nTotal books available: {len(self.books)}")

My_Library = Library([
    "Python Crash Course",
    "clean code",
    "Introduction to Algorithms",
    "Head First Java",
    "Data Structures and Algorithms",
    "The pragmatic programmer",
    "The Art of Computer programming",
    "Introduction to the Theory of Computation",
    "Computer Networks",
    "Operating System Concepts",
    "Database System Concepts",
    "Artificial Intellgence:a Modern Approach",
    "Machine Learning",
    "Deep Learning",
    "Effectiveness of Python programming",
    "Learning SQL",
    "Hands-on Machine Learning",
    "Django for Beginners",
    "Flask Web Development",
    "Software Engineering",
    "The C programming Language"
])


BG = "#0F172A"
SIDEBAR = "#111827"
CARD = "#1E293B"
CARD2 = "#263449"
TEXT = "#F8FAFC"
MUTED = "#94A3B8"
ACCENT = "#38BDF8"
GREEN = "#22C55E"
RED = "#EF4444"
WHITE = "#FFFFFF"

root = tk.Tk()

root.title("Library Management System")
root.geometry("1200x720")
root.resizable(False, False)
root.configure(bg=BG)

sidebar = tk.Frame(
    root,
    bg=SIDEBAR,
    width=230,
    height=720
)

sidebar.place(x=0, y=0)

logo = tk.Label(
    sidebar,
    text="📚",
    font=("Arial", 35),
    bg=SIDEBAR,
    fg=ACCENT
)

logo.pack(pady=(35, 5))

library_name = tk.Label(
    sidebar,
    text="LIBRARY",
    font=("Arial", 17, "bold"),
    bg=SIDEBAR,
    fg=TEXT
)

library_name.pack()

system_name = tk.Label(
    sidebar,
    text="MANAGEMENT SYSTEM",
    font=("Arial", 8),
    bg=SIDEBAR,
    fg=MUTED
)

system_name.pack(pady=(0, 40))

def sidebar_button(text):
    button = tk.Button(
        sidebar,
        text=text,
        font=("Arial", 11, "bold"),
        bg=SIDEBAR,
        fg=MUTED,
        activebackground=CARD,
        activeforeground=TEXT,
        bd=0,
        anchor="w",
        padx=30,
        width=22,
        height=2
    )
    button.pack(pady=4)
    return button


home_btn = sidebar_button("⌂   Dashboard")
books_btn = sidebar_button("▣   All Books")
borrow_btn = sidebar_button("↗   Borrow Book")
return_btn = sidebar_button("↙   Return Book")
search_btn = sidebar_button("⌕   Search")

exit_btn = tk.Button(
    sidebar,
    text="⏻   Exit",
    font=("Arial", 11, "bold"),
    bg=SIDEBAR,
    fg=RED,
    activebackground=CARD,
    activeforeground=RED,
    bd=0,
    anchor="w",
    padx=30,
    width=22,
    height=2,
    command=root.destroy
)

exit_btn.pack(
    side="bottom",
    pady=30
)

main = tk.Frame(
    root,
    bg=BG,
    width=970,
    height=720
)

main.place(x=230, y=0)

heading = tk.Label(
    main,
    text="Good day! 👋",
    font=("Arial", 24, "bold"),
    bg=BG,
    fg=TEXT
)

heading.place(x=35, y=30)

subtitle = tk.Label(
    main,
    text="Manage your library from one place.",
    font=("Arial", 11),
    bg=BG,
    fg=MUTED
)

subtitle.place(x=37, y=70)

def create_card(x, title, value, icon):

    frame = tk.Frame(
        main,
        bg=CARD,
        width=205,
        height=110
    )

    frame.place(x=x, y=115)

    icon_label = tk.Label(
        frame,
        text=icon,
        font=("Arial", 25),
        bg=CARD,
        fg=ACCENT
    )

    icon_label.place(x=18, y=20)

    title_label = tk.Label(
        frame,
        text=title,
        font=("Arial", 9),
        bg=CARD,
        fg=MUTED
    )

    title_label.place(x=70, y=25)

    value_label = tk.Label(
        frame,
        text=value,
        font=("Arial", 22, "bold"),
        bg=CARD,
        fg=TEXT
    )

    value_label.place(x=70, y=48)

    return value_label

total_card = create_card(
    35,
    "TOTAL BOOKS",
    str(len(My_Library.books)),
    "📚"
)

available_card = create_card(
    260,
    "AVAILABLE",
    str(len(My_Library.books)),
    "✓"
)

activity_card = create_card(
    485,
    "STATUS",
    "ONLINE",
    "●"
)

search_frame = tk.Frame(
    main,
    bg=CARD2,
    width=650,
    height=55
)

search_frame.place(
    x=35,
    y=245
)

search_icon = tk.Label(
    search_frame,
    text="⌕",
    font=("Arial", 22),
    bg=CARD2,
    fg=ACCENT
)

search_icon.place(
    x=15,
    y=10
)

search_entry = tk.Entry(
    search_frame,
    font=("Arial", 12),
    bg=CARD2,
    fg=TEXT,
    insertbackground=TEXT,
    bd=0,
    width=55
)

search_entry.place(
    x=55,
    y=17
)

def search_from_dashboard():

    book_name = search_entry.get().strip()

    if book_name == "":
        messagebox.showwarning(
            "Search",
            "Please enter a book name."
        )
        return

    if My_Library.search_book(book_name):

        messagebox.showinfo(
            "Book Found",
            f"📖 '{book_name}' is available."
        )

    else:

        messagebox.showerror(
            "Not Available",
            f"❌ '{book_name}' is not available."
        )


search_button = tk.Button(
    search_frame,
    text="SEARCH",
    font=("Arial", 9, "bold"),
    bg=ACCENT,
    fg=BG,
    bd=0,
    width=10,
    height=2,
    command=search_from_dashboard
)

search_button.place(
    x=550,
    y=8
)

books_title = tk.Label(
    main,
    text="Available Books",
    font=("Arial", 18, "bold"),
    bg=BG,
    fg=TEXT
)

books_title.place(
    x=35,
    y=320
)

books_count = tk.Label(
    main,
    text="Browse the collection",
    font=("Arial", 9),
    bg=BG,
    fg=MUTED
)

books_count.place(
    x=35,
    y=350
)

book_frame = tk.Frame(
    main,
    bg=CARD,
    width=650,
    height=300
)

book_frame.place(
    x=35,
    y=380
)

book_list = tk.Listbox(
    book_frame,
    font=("Arial", 11),
    bg=CARD,
    fg=TEXT,
    selectbackground=ACCENT,
    selectforeground=BG,
    bd=0,
    highlightthickness=0,
    activestyle="none"
)

book_list.place(
    x=15,
    y=15,
    width=620,
    height=265
)

def display_books():

    book_list.delete(
        0,
        tk.END
    )

    for index, book in enumerate(
        My_Library.books,
        1
    ):

        book_list.insert(
            tk.END,
            f"  {index:02d}     📖   {book}"
        )

    total_card.config(
        text=str(len(My_Library.books))
    )

    available_card.config(
        text=str(len(My_Library.books))
    )

action_frame = tk.Frame(
    main,
    bg=CARD,
    width=250,
    height=435
)

action_frame.place(
    x=700,
    y=245
)

action_title = tk.Label(
    action_frame,
    text="Quick Actions",
    font=("Arial", 17, "bold"),
    bg=CARD,
    fg=TEXT
)

action_title.pack(
    pady=(25, 5)
)

action_subtitle = tk.Label(
    action_frame,
    text="Library operations",
    font=("Arial", 9),
    bg=CARD,
    fg=MUTED
)

action_subtitle.pack(
    pady=(0, 20)
)

def borrow_book():

    window = tk.Toplevel(root)

    window.title("Borrow Book")
    window.geometry("400x300")
    window.configure(bg=BG)
    window.resizable(False, False)

    tk.Label(
        window,
        text="📤 Borrow a Book",
        font=("Arial", 20, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(pady=25)

    tk.Label(
        window,
        text="Your Name",
        bg=BG,
        fg=MUTED
    ).pack()

    name = tk.Entry(
        window,
        font=("Arial", 11),
        width=35
    )

    name.pack(pady=7)

    tk.Label(
        window,
        text="Book Name",
        bg=BG,
        fg=MUTED
    ).pack()

    book = tk.Entry(
        window,
        font=("Arial", 11),
        width=35
    )

    book.pack(pady=7)

    def confirm():

        user_name = name.get().strip()
        requested_book = book.get().strip()

        if user_name == "" or requested_book == "":
            messagebox.showwarning(
                "Missing Details",
                "Please enter all details."
            )
            return

        if My_Library.lend_book(requested_book):

            current_time = datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )

            messagebox.showinfo(
                "Success",
                f"Welcome {user_name}!\n\n"
                f"📖 {requested_book}\n"
                f"🕒 {current_time}"
            )

            display_books()
            window.destroy()

        else:

            messagebox.showerror(
                "Unavailable",
                f"'{requested_book}' is not available."
            )

    tk.Button(
        window,
        text="BORROW BOOK",
        font=("Arial", 10, "bold"),
        bg=ACCENT,
        fg=BG,
        bd=0,
        width=25,
        height=2,
        command=confirm
    ).pack(pady=20)

def return_book():

    window = tk.Toplevel(root)

    window.title("Return Book")
    window.geometry("400x250")
    window.configure(bg=BG)
    window.resizable(False, False)

    tk.Label(
        window,
        text="📥 Return a Book",
        font=("Arial", 20, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(pady=30)

    book = tk.Entry(
        window,
        font=("Arial", 11),
        width=35
    )

    book.pack(pady=10)

    def confirm_return():

        returned_book = book.get().strip()

        if returned_book == "":
            messagebox.showwarning(
                "Missing Book",
                "Enter the book name."
            )
            return

        My_Library.add_book(
            returned_book
        )

        messagebox.showinfo(
            "Returned",
            f"📚 '{returned_book}' returned successfully."
        )

        display_books()
        window.destroy()

    tk.Button(
        window,
        text="RETURN BOOK",
        font=("Arial", 10, "bold"),
        bg=GREEN,
        fg=BG,
        bd=0,
        width=25,
        height=2,
        command=confirm_return
    ).pack(pady=20)

tk.Button(
    action_frame,
    text="↗   BORROW BOOK",
    font=("Arial", 10, "bold"),
    bg=ACCENT,
    fg=BG,
    bd=0,
    width=25,
    height=2,
    command=borrow_book
).pack(pady=8)

tk.Button(
    action_frame,
    text="↙   RETURN BOOK",
    font=("Arial", 10, "bold"),
    bg=GREEN,
    fg=BG,
    bd=0,
    width=25,
    height=2,
    command=return_book
).pack(pady=8)

tk.Button(
    action_frame,
    text="⌕   SEARCH BOOK",
    font=("Arial", 10, "bold"),
    bg=CARD2,
    fg=TEXT,
    bd=0,
    width=25,
    height=2,
    command=search_from_dashboard
).pack(pady=8)

tk.Button(
    action_frame,
    text="⟳   REFRESH",
    font=("Arial", 10, "bold"),
    bg=CARD2,
    fg=TEXT,
    bd=0,
    width=25,
    height=2,
    command=display_books
).pack(pady=8)

footer = tk.Label(
    main,
    text="Library Management System  •  Python + Tkinter",
    font=("Arial", 8),
    bg=BG,
    fg=MUTED
)

footer.place(
    x=35,
    y=690
)

display_books()

root.mainloop()