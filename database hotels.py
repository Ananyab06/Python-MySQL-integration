import tkinter as tk
from tkinter import ttk
import mysql.connector
def search_hotel(CITY=None, ROOM_TYPE=None, STARS=None):
    query = "SELECT * FROM HOTELS1 WHERE 1=1"
    params = []

    if CITY:
        query += " AND CITY = %s"
        params.append(CITY)
    if ROOM_TYPE:
        query += " AND ROOM_TYPE = %s"
        params.append(ROOM_TYPE)
    if STARS:
        query += " AND STARS = %s"
        params.append(STARS )
    
    with mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='HOTEL'
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
# Tkinter application
def search_hotel_gui():
    def search():
        CITY = CITY_entry.get()
        ROOM_TYPE = ROOM_TYPE_entry.get()
        STARS = STARS_entry.get()
        results = search_hotel(CITY,ROOM_TYPE,STARS )
        display_results(results)

    def display_results(results):
        result_tree.delete(*result_tree.get_children())  # Clear existing rows

        if not results:
            result_tree.insert("", "end", values=("No results found", "", "", ""))
        else:
            for result in results:
                result_tree.insert("", "end", values=result)
    
    root = tk.Tk()
    root.title("Python-MySQL integration module")
    root.geometry("1129x700")
    root.resizable(False,False)

    search_frame = tk.Frame(root)
    search_frame.pack(padx=10, pady=10)

    CITY_label = tk.Label(search_frame, text="CITY:",font=("Gadugi",16))
    CITY_label.grid(row=0, column=0)
    CITY_entry = ttk.Combobox(search_frame,font=("Gadugi",16),values=["Kerala","Andaman and Nicobar Islands","Rajasthan","Kashmir","Gujarat","Sikkim","Leh Ladakh"])
    CITY_entry.grid(row=0, column=1)

    ROOM_TYPE_label = tk.Label(search_frame, text="ROOM_TYPE:",font=("Gadugi",16))
    ROOM_TYPE_label.grid(row=1, column=0)
    ROOM_TYPE_entry = tk.Entry(search_frame,font=("Gadugi",16))
    ROOM_TYPE_entry.grid(row=1, column=1)

    STARS_label = tk.Label(search_frame, text="STARS:",font=("Gadugi",16))
    STARS_label.grid(row=2, column=0)
    STARS_entry = tk.Entry(search_frame,font=("Gadugi",16))
    STARS_entry.grid(row=2, column=1)

    search_button = tk.Button(search_frame, text="Search", command=search,height=1,width=7,font=("Gadugi",16))
    search_button.grid(row=3, columnspan=2)
     #Create a custom style for the Treeview widget
    style = ttk.Style()
    style.theme_use("clam")  

    # Configure the style for the Treeview widget
    style.configure("Treeview", font=("Gadugi", 12), rowheight=25, fieldbackground="white")

    # Configure the style for the Treeview headings
    style.configure("Treeview.Heading", font=("Gadugi", 12, "bold"), background="lightblue")
   
   

    result_tree = ttk.Treeview(root, columns=( "CITY","NAME", "STARS ","ROOM_TYPE","PRICE_PER_NIGHT","LOCATION"), show="headings",height=15)
    result_tree.heading("CITY", text="CITY")
    result_tree.heading("ROOM_TYPE", text="ROOM_TYPE")
    result_tree.heading("STARS ", text="STARS ")
    result_tree.heading("NAME", text="NAME")
    result_tree.heading("PRICE_PER_NIGHT", text="PRICE_PER_NIGHT")
    result_tree.heading("LOCATION", text="LOCATION")
    result_tree.pack(padx=10, pady=10)
    result_tree.column("CITY", width=130)
    result_tree.column("ROOM_TYPE", width=120)
    result_tree.column("STARS ", width=50)
    result_tree.column("NAME",width=250 )
    result_tree.column("PRICE_PER_NIGHT",width=150)
    result_tree.column("LOCATION",width=350)

    root.mainloop()

search_hotel_gui()




