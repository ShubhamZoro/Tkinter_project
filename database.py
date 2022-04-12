from tkinter import *


import sqlite3

window=Tk()
window.title("Opening a new window")


conn=sqlite3.connect("address_book.db")

#create cursor
c=conn.cursor()
# c.execute("""CREATE TABLE ADDRESSES(first_name text,
# last_name text,
# address text,
# city text)""")

#create function to delete

#add data in database
def add_data():
    conn = sqlite3.connect("address_book.db")

    # create cursor
    c = conn.cursor()

    #Inset into Table
    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:state)",
            {
            'f_name':f_name.get(),
            'l_name':l_name.get(),
            'address':address.get(),
            'state':state.get()
            })


    # commit changes
    conn.commit()

    # connect connection
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    state.delete(0, END)

#edit the data
def edit_data():
    conn = sqlite3.connect("address_book.db")

    # create cursor
    c = conn.cursor()
    record_id=delete_box.get()
    c.execute(""" UPDATE addresses SET 
        first_name=:first,
        last_name=:last,
        address=:address,
        city=:state
        
        WHERE oid=:oid""",

              {
        'first':f_name_editor.get(),
        'last':l_name_editor.get(),
        'address':address_editor.get(),
        'state':state_editor.get(),
        'oid':record_id
    })
    # commit changes
    conn.commit()

    # connect connection
    conn.close()

    editor.destroy()

#Create an Update function
def update():
    global editor
    editor=Tk()
    editor.title()
    editor.geometry("400x600")
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # create cursor
    c = conn.cursor()
    record_id=delete_box.get()
    # Inset into Table
    c.execute("SELECT * FROM addresses WHERE oid="+record_id
              )
    records = c.fetchall()
    #Loop through results

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[3]) + '\n'
    global f_name_editor, l_name_editor, address_editor, state_editor
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=10)

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20, pady=10)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20, pady=10)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=3, column=1, padx=20, pady=10)




    # Create Text Box
    f_name_label = Label(editor, text="Fname")
    f_name_label.grid(row=0, column=0, pady=10)

    l_name_label = Label(editor, text="Lname")
    l_name_label.grid(row=1, column=0, pady=10)

    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0, pady=10)

    state_label = Label(editor, text="State")
    state_label.grid(row=3, column=0, pady=10)
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        state_editor.insert(0, record[3])
    conn.commit()

    # connect connection
    conn.close()
    # save updated record
    save_btn = Button(editor, text="save Update record", command=edit_data)
    save_btn.grid(row=4, column=1, columnspan=2, pady=10, ipadx=105)
    # commit changes



def query():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # create cursor
    c = conn.cursor()

    # Inset into Table
    c.execute("SELECT *, oid FROM addresses",

              )
    records=c.fetchall()
    print_records=''
    for record in records:
        print_records +=str(record[0])+" " +str(record[1]) + " "+"\t" + str(record[4])+'\n'

    query_label=Label(window,text=print_records)
    query_label.grid(row=9,column=0,columnspan=2,pady=20)

    # commit changes
    conn.commit()

    # connect connection
    conn.close()

def delete():
    conn = sqlite3.connect("address_book.db")

    # create cursor
    c = conn.cursor()

    #Delete a record
    c.execute("DELETE from addresses WHERE oid=" + delete_box.get())
    # commit changes
    conn.commit()
    delete_box.delete(0,END)

    # connect connection
    conn.close()

    query()
f_name=Entry(window,width=30)
f_name.grid(row=0,column=1,padx=20,pady=10)

l_name=Entry(window,width=30)
l_name.grid(row=1,column=1,padx=20,pady=10)

address=Entry(window,width=30)
address.grid(row=2,column=1,padx=20,pady=10)

state=Entry(window,width=30)
state.grid(row=3,column=1,padx=20,pady=10)

delete_box=Entry(window,width=30)
delete_box.grid(row=7,column=1)

#Create Text Box
f_name_label=Label(window,text="Fname")
f_name_label.grid(row=0,column=0,pady=10)

l_name_label=Label(window,text="Lname")
l_name_label.grid(row=1,column=0,pady=10)

address_label=Label(window,text="Address")
address_label.grid(row=2,column=0,pady=10)

state_label=Label(window,text="State")
state_label.grid(row=3,column=0,pady=10)

delete_l=Label(window,text="Select ID")
delete_l.grid(row=7,column=0)


submit=Button(window,text="Add data to database",command=add_data)
submit.grid(row=4,column=0,columnspan=2,ipadx=90)

#Create a query button
query_btn=Button(window,text="Show records",command=query)
query_btn.grid(row=5,column=0,columnspan=2,pady=10,ipadx=107)
#create delete button
del_btn=Button(window,text="Delete record",command=delete)
del_btn.grid(row=8,column=0,columnspan=2,pady=10,ipadx=105)
#update_button
update_btn=Button(window,text="Update record",command=update)
update_btn.grid(row=10,column=0,columnspan=2,pady=10,ipadx=105)

mainloop()