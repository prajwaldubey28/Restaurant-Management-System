from tkinter import *
import random
import time
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

ro = Tk()
ro.geometry("280x500")
ro.configure(bg='black')

# my_img=ImageTk.PhotoImage(Image.open('abc.png'))
# label_my_img=Label(ro,width=9000,height=400,image=my_img,justify='left',bg='black')
# label_my_img.pack()

ro.title("Welcome")
Top = Frame(ro, width=1600, height=50, relief=SUNKEN, bg="black")
Top.pack(side=TOP)
f3 = Frame(ro, width=900, height=700, relief=SUNKEN, pady=90, bg='black')
f3.pack()
lblinf = Label(Top, font=('aria', 35, 'bold'), text="Welcome", fg="red", bg='black', bd=10, anchor='w', pady=4)
lblinf.grid(row=0, column=0)

conn=sqlite3.connect("customer.db")
c=conn.cursor()
'''
c.execute("""CREATE TABLE customer(
                                       Order_id integer,
                                       Pav_Bhaji integer,
                                       Dosa integer,
                                       Indian_Thali integer,
                                       Kebabs integer,
                                       Chinese_Thali integer,
                                       Jain_Thali integer,
                                       Drinks integer,
                                       Dessert integer)""")
'''
conn.commit()
conn.close()


# To print the data

def query():
    conn=sqlite3.connect("Customer.db")
    c=conn.cursor()
    c.execute("SELECT *,oid FROM Customer")
    result= c.fetchall()
    for i in result:
        print(i)

    conn.commit()
    conn.close()


def branch():

    r = Tk()
    r.geometry("350x200")
    r.title("Branch Details")
    r.configure(bg='black')
    lbl1 = Label(r, font=('aria', 15, 'bold'), text="State", fg="red", bg='black', bd=5)
    lbl1.grid(row=0, column=0)
    lbl2 = Label(r, font=('aria', 15, 'bold'), text="______", fg="black", bg='black', anchor=W)
    lbl2.grid(row=0, column=2)
    lbl3 = Label(r, font=('aria', 15, 'bold'), text="no of branches", fg='red', bg='black', anchor=W)
    lbl3.grid(row=0, column=3)
    lbl4 = Label(r, font=('aria', 15, 'bold'), text="Maharashtra", fg="red", bg='black', anchor=W)
    lbl4.grid(row=1, column=0)
    lbl5 = Label(r, font=('aria', 15, 'bold'), text="3", fg="red", bg='black', anchor=W)
    lbl5.grid(row=1, column=3)
    lbl6 = Label(r, font=('aria', 15, 'bold'), text="Delhi", fg="red", bg='black', anchor=W)
    lbl6.grid(row=2, column=0)
    lbl7 = Label(r, font=('aria', 15, 'bold'), text="2", fg="red", bg='black', anchor=W)
    lbl7.grid(row=2, column=3)
    lbl8 = Label(r, font=('aria', 15, 'bold'), text="Assam", fg="red", bg='black', anchor=W)
    lbl8.grid(row=3, column=0)
    lbl9 = Label(r, font=('aria', 15, 'bold'), text="2", fg="red", bg='black', anchor=W)
    lbl9.grid(row=3, column=3)
    lbl10 = Label(r, font=('aria', 15, 'bold'), text="Goa", fg="red", bg='black', anchor=W)
    lbl10.grid(row=4, column=0)
    lbl11 = Label(r, font=('aria', 15, 'bold'), text="1", fg="red", bg='black', anchor=W)
    lbl11.grid(row=4, column=3)
    lbl12 = Label(r, font=('aria', 15, 'bold'), text="West Bengal", fg="red", bg='black', anchor=W)
    lbl12.grid(row=5, column=0)
    lbl3 = Label(r, font=('aria', 15, 'bold'), text="1", fg="red", bg='black', anchor=W)
    lbl3.grid(row=5, column=3)
    r.mainloop()

def about():

    p = Tk()
    p.geometry("900x200")
    p.title("Details")
    p.configure(bg='black')

    lbla = Label(p, font=('aria', 15, 'bold'),
                 text="This is our project that shows real life application of GUI and Database using python.\nThis is a Restaurant Management System,with the following functions:\n1. To view the Menu card\n2. To Take a particular order\n3.To Calculate Total no of bills\n4.To resert the order if needed\n5. To fetch the details of orders in past ",
                 fg="red", bg='black', bd=5)
    lbla.grid(row=0, column=0)

    p.mainloop()

def main():

    def qexit():

        messagebox.showinfo("Greeting","Thank You for Visiting")
        root.destroy()
        ro.destroy()


    def reset():

        txtorder.delete(0, END)
        txtpb.delete(0, END)
        txtdosa.delete(0, END)
        txtindt.delete(0, END)
        txtFilet.delete(0, END)
        txtchet.delete(0, END)
        txtsdr.delete(0, END)
        txtjt.delete(0, END)
        txtic.delete(0, END)
        txtTax.delete(0, END)
        txtSubtotal.delete(0, END)
        txtTotal.delete(0, END)

    def total():

        txtTax.delete(0, END)
        txtSubtotal.delete(0, END)
        txtTotal.delete(0, END)

        copb = int(txtpb.get())
        codosa = int(txtdosa.get())
        coindt = int(txtindt.get())
        cofi = int(txtFilet.get())
        cochet = int(txtchet.get())
        cosdr = int(txtsdr.get())
        cojt = int(txtjt.get())
        coic = int(txtic.get())

        costofpb = copb * 70
        costofdosa = codosa * 60
        costofindt = coindt * 100
        costoffilet = cofi * 150
        costofchet = cochet * 120
        costofsdr = cosdr * 50
        costofjt = cojt * 70
        costofic = coic * 40

        tt = int(costofpb + costofdosa + costofindt + costoffilet + costofchet + costofsdr + costofjt + costofic)

        cost = tt

        PayTax = tt * 0.12
        Totalcost = tt
        Ser_Charge = tt / 99
        OverAllCost = (PayTax + Totalcost + Ser_Charge)
        PaidTax = PayTax

        txtTotal.insert(0, OverAllCost)
        txtTax.insert(0, PaidTax)
        txtSubtotal.insert(0, cost)

        conn = sqlite3.connect("customer.db")
        c = conn.cursor()

        c.execute(
            "INSERT INTO customer(Order_id, Pav_Bhaji, Dosa, Indian_Thali, Kebabs, Chinese_Thali, Jain_Thali, Drinks, Dessert) VALUES(:Order_id, :Pav_Bhaji, :Dosa, :Indian_Thali, :Kebabs, :Chinese_Thali, :Jain_Thali, :Drinks, :Dessert)",

            {
                'Order_id': txtorder.get(),
                'Pav_Bhaji': txtpb.get(),
                'Dosa': txtdosa.get(),
                'Indian_Thali': txtindt.get(),
                'Kebabs': txtFilet.get(),
                'Chinese_Thali': txtchet.get(),
                'Jain_Thali': txtjt.get(),
                'Drinks': txtsdr.get(),
                'Dessert': txtic.get()
            })

        conn.commit()
        conn.close()



    root = Tk()
    root.configure(bg='black')
    root.title("Restaurant Management System")


    lblorder = Label(root, font=('aria', 16, 'bold'), text="Order No.", fg="red", bg='black', bd=10, anchor='w', pady=5)
    lblorder.grid(row=3, column=0)
    txtorder = Entry(root, font=('ariel', 16, 'bold'), bd=6, insertwidth=4, bg="white",
                     justify='right')
    txtorder.grid(row=3, column=1)

    lblpb = Label(root, font=('aria', 16, 'bold'), text="Pav Bhaji", fg="red", bg='black', bd=10, anchor='w', pady=5)
    lblpb.grid(row=4, column=0)
    txtpb = Entry(root, font=('ariel', 16, 'bold'),  bd=6, insertwidth=4, bg="white",
                  justify='right')
    txtpb.grid(row=4, column=1)

    lbldosa = Label(root, font=('aria', 16, 'bold'), text="Dosa", fg="red", bg='black', bd=10, anchor='w', pady=5)
    lbldosa.grid(row=5, column=0)
    txtdosa = Entry(root, font=('ariel', 16, 'bold'),  bd=6, insertwidth=4, bg="white", justify='right')
    txtdosa.grid(row=5, column=1)

    lblindt = Label(root, font=('aria', 16, 'bold'), text="Indian Thali", fg="red", bg='black', bd=10, anchor='w', pady=5)
    lblindt.grid(row=6, column=0)
    txtindt = Entry(root, font=('ariel', 16, 'bold'),  bd=6, insertwidth=4, bg="white",
                    justify='right')
    txtindt.grid(row=6, column=1)

    lblFilet = Label(root, font=('aria', 16, 'bold'), text="Kebabs", fg="red", bg='black', bd=10, anchor='w', pady=5)
    lblFilet.grid(row=7, column=0)
    txtFilet = Entry(root, font=('ariel', 16, 'bold'),  bd=6, insertwidth=4, bg="white",
                     justify='right')
    txtFilet.grid(row=7, column=1)

    lblchet = Label(root, font=('aria', 16, 'bold'), text="Chinese Thali", fg="red", bg='black', bd=10, anchor='w',
                    pady=10)
    lblchet.grid(row=8, column=0)
    txtchet = Entry(root, font=('ariel', 16, 'bold'),  bd=6, insertwidth=4, bg="white",
                    justify='right')
    txtchet.grid(row=8, column=1)

    # --------------------------------------------------------------------------------------
    lblsdr = Label(root, font=('aria', 16, 'bold'), text="Soft Drinks", fg='red', bg='black', bd=10, anchor='w', pady=5)
    lblsdr.grid(row=4, column=2)
    txtsdr = Entry(root, font=('ariel', 16, 'bold'),  bd=6, insertwidth=4, bg="white",
                   justify='right')
    txtsdr.grid(row=4, column=3)

    lbljt = Label(root, font=('aria', 16, 'bold'), text="Jain Thali", fg="red", bg='black', bd=10, anchor='w', pady=5)
    lbljt.grid(row=3, column=2)
    txtjt = Entry(root, font=('ariel', 16, 'bold'),  bd=6, insertwidth=4, bg="white",
                  justify='right')
    txtjt.grid(row=3, column=3)

    lblic = Label(root, font=('aria', 16, 'bold'), text="Dessert", fg="red", bg='black', bd=10, anchor='w', pady=5)
    lblic.grid(row=5, column=2)
    txtic = Entry(root, font=('ariel', 16, 'bold'), bd=6, insertwidth=4, bg="white",
                  justify='right')
    txtic.grid(row=5, column=3, padx = 30)

    lblTax = Label(root, font=('aria', 16, 'bold'), text="Tax", fg="red", bg='black', bd=10, anchor='w', pady=5)
    lblTax.grid(row=7, column=2)
    txtTax = Entry(root, font=('ariel', 16, 'bold'), bd=6, insertwidth=4, bg="white", justify='right')
    txtTax.grid(row=7, column=3)

    lblSubtotal = Label(root, font=('aria', 16, 'bold'), text="Subtotal", fg="red", bg='black', bd=10, anchor='w', pady=5)
    lblSubtotal.grid(row=6, column=2)
    txtSubtotal = Entry(root, font=('ariel', 16, 'bold'), bd=6, insertwidth=4, bg="white",
                        justify='right')
    txtSubtotal.grid(row=6, column=3)

    lblTotal = Label(root, font=('aria', 16, 'bold'), text="Total", fg="red", bg='black', bd=10, anchor='w', pady=10)
    lblTotal.grid(row=8, column=2)
    txtTotal = Entry(root, font=('ariel', 16, 'bold'), bd=6, insertwidth=4, bg="white",
                     justify='right')
    txtTotal.grid(row=8, column=3)

    def price():
        roo = Tk()
        roo.geometry("600x300+0+0")
        roo.title("Menu Card")
        roo.configure(bg='black')

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="red",bg='black', bd=5)
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="black",bg='black', anchor=W)
        lblinfo.grid(row=0, column=2)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg='red',bg='black', anchor=W)
        lblinfo.grid(row=0, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pav Bhaji", fg="red",bg='black', anchor=W)
        lblinfo.grid(row=1, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="70", fg="red",bg='black', anchor=W)
        lblinfo.grid(row=1, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Dosa", fg="red", bg='black',anchor=W)
        lblinfo.grid(row=2, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="60", fg="red",bg='black', anchor=W)
        lblinfo.grid(row=2, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Indian Thali", fg="red", bg='black',anchor=W)
        lblinfo.grid(row=3, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="100", fg="red", bg='black',anchor=W)
        lblinfo.grid(row=3, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Kebabs", fg="red", bg='black',anchor=W)
        lblinfo.grid(row=4, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="150", fg="red", bg='black',anchor=W)
        lblinfo.grid(row=4, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chinese Thali", fg="red",bg='black', anchor=W)
        lblinfo.grid(row=5, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="120", fg="red",bg='black', anchor=W)


        lblinfo.grid(row=5, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Jain thali", fg="red",bg='black', anchor=W)
        lblinfo.grid(row=6, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="70", fg="red", bg='black',anchor=W)
        lblinfo.grid(row=6, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Soft Drinks", fg="red",bg='black', anchor=W)
        lblinfo.grid(row=7, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="red",bg='black', anchor=W)
        lblinfo.grid(row=7, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Dessert", fg="red",bg='black', anchor=W)
        lblinfo.grid(row=8, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="red",bg='black', anchor=W)
        lblinfo.grid(row=8, column=3)




        roo.mainloop()

    btnprice=Button(root,padx=16,pady=8, bd=10 ,fg="red",font=('ariel' ,16,'bold'),width=10, text="Menu Card", bg="black",command=price)
    btnprice.grid(row=9, column=0, padx = 20)

    # -----------------------------------------buttons------------------------------------------

    btnTotal = Button(root, padx=16, pady=8, bd=10, fg="red", font=('ariel', 16, 'bold'), width=10, text="TOTAL",
                      bg="black", command=total)
    btnTotal.grid(row=9, column=1)

    btnreset = Button(root, padx=16, pady=8, bd=10, font=('ariel', 16, 'bold'), width=10, text="RESET", bg='black',
                      fg='red', command=reset)
    btnreset.grid(row=9, column=2)

    btnexit = Button(root, padx=16, pady=8, bd=10, font=('ariel', 16, 'bold'), width=10, text="EXIT", bg="black",
                     fg='red', command=qexit)
    btnexit.grid(row=9, column=3)

    localtime = time.asctime(time.localtime(time.time()))
    # -----------------INFO TOP------------
    lblinfo = Label(root, font=('aria', 35, 'bold'), text="Restaurant Management System", fg="red", bg='black', bd=10,
                    anchor='w', pady=20)
    lblinfo.grid(row=0, column=0,columnspan = 5)
    lblinfo = Label(root, font=('aria', 20,), text=localtime, fg="red", bg='black', anchor=W, pady=10)
    lblinfo.grid(row=1, column=0,columnspan = 5)


    def price():
        roo = Tk()
        roo.geometry("600x300+0+0")
        roo.title("Menu Card")
        roo.configure(bg='black')
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="red", bg='black', bd=5)
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="black", bg='black', anchor=W)
        lblinfo.grid(row=0, column=2)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg='red', bg='black', anchor=W)
        lblinfo.grid(row=0, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pav Bhaji", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=1, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="70", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=1, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Dosa", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=2, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="60", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=2, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Indian Thali", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=3, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="100", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=3, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Kebabs", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=4, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="150", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=4, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chinese Thali", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=5, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="120", fg="red", bg='black', anchor=W)

        lblinfo.grid(row=5, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Jain thali", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=6, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="70", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=6, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Soft Drinks", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=7, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=7, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Dessert", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=8, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="red", bg='black', anchor=W)
        lblinfo.grid(row=8, column=3)


    root.mainloop()


btn2=Button(f3,padx=20,pady=8, bd=10 ,fg="red",font=('ariel' ,16,'bold'),width=10, text="Go to Restaurant",bg="black",command=main)
btn2.grid(row=2, column=3,columnspan=2, pady =20)

btn3=Button(f3,padx=20,pady=8, bd=10 ,fg="red",font=('ariel' ,16,'bold'),width=10, text="Branch Details",bg='black',command=branch)
btn3.grid(row=3, column=3,columnspan=2, pady =20)

btn4=Button(f3,padx=20,pady=8, bd=10 ,fg="red",font=('ariel' ,16,'bold'),width=10, text="About",bg='black',command=about)
btn4.grid(row=4, column=3,columnspan=2, pady = 20)


ro.mainloop()
