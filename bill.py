from tkinter import *
from tkinter import messagebox
import datetime as d
import os


mw = Tk()
mw.title('Billing Software For Retail Shops')
mw.geometry('1280x720')
bg_color="darkblue"

title = Label(mw,text="Billing Software",bd=12,bg=bg_color,fg='white',relief=GROOVE,font=("Poppins", 25, "bold"))
title.pack(pady=2, fill=X)


# =================Variables

customer_name = StringVar()
customer_phone = StringVar()
bill_number = StringVar()
product = StringVar()
product_cost = IntVar()
product_qty = IntVar()

global l
l = []

# ================Functions

def addproduct():
    p=product_cost.get()
    z=product_qty.get()*p
    l.append(z)
    if product.get()== '':
        messagebox.showerror('Error', 'Please "Enter Product Name"')
    elif product_qty.get()==0:
        messagebox.showerror('Error','Please "Enter Product Quantity"')
    elif product_cost.get()==0:
        messagebox.showerror('Error','Please "Enter Product Cost"')
    else:
        textarea.insert((10.0+float(len(l)-1)), f'{product.get()}\t\t\t{product_qty.get()}\t\tRs. {z}/-\n')
        product_cost.set(0)
        product_qty.set(0)
        product.set('')

def start():
    textarea.delete('1.0',END)
    textarea.insert(END, "\tWELCOME TO 'ADITHYA GENERAL STORES'")
    textarea.insert(END, f'\nCustomer Name: {customer_name.get()}')
    textarea.insert(END, f'\t\t\t\tBill Number: {bill_number.get()}')
    textarea.insert(END, f'\nMobile Number: {customer_phone.get()}')
    autodate = d.datetime.now().strftime('%d/%m/%Y-%H:%M')
    textarea.insert(END, f'\t\t\t\tDate: {autodate}')
    textarea.insert(END, f"\n----------------------------------------------------------------------------------")
    textarea.insert(END, '\nProduct Name\t\t\tQuantity\t\tTotal Cost(Rs.)')
    textarea.insert(END, f"\n----------------------------------------------------------------------------------\n")
    textarea.configure(font='arial 15 bold')

def generate_bill():
    if customer_name.get()=='' or customer_phone.get()=='':
        messagebox.showerror('Error','Enter Customer Details')
    else:
        txt = textarea.get(7.0,(10.0+float(len(l))))
        start()
        textarea.insert(END, txt)
        textarea.insert(END, f"\n----------------------------------------------------------------------------------")
        textarea.insert(END, f"\nTotal Paybill Amount :\t\t\t\t\tRs. {sum(l)}/-")
        textarea.insert(END, f"\n----------------------------------------------------------------------------------")

def save_bill():
    bill_area = textarea.get(1.0, END)
    if bill_area=='':
        messagebox.showerror('Error','There Is Nothing To Be Save')
    else:
        msg = messagebox.askyesno('Save Bill','Do You Want To Save The Bill?')
        if msg>0:
            billdata = textarea.get(1.0, END)
            f1=("bills/"+(bill_number.get())+".txt")
            open(f1,'w',encoding="utf-8").write(billdata)
            messagebox.showinfo('Bill Saved',f'Bill Number:{bill_number.get()} Saved Successfully')
        else:
            return

def print_bill():
    bill_area = textarea.get(1.0, END)
    if bill_area=='':
        messagebox.showerror('Error','There Is Nothing To Be Print')
    else:
        f1=("bills\\"+(bill_number.get())+'.txt')
        open(f1, 'w', encoding="utf-8").write(bill_area)
        os.startfile(f1, 'print')

def cleardata():
    msg_cnfm = messagebox.askyesno('Exit','Do You Really Want To Reset?')
    if msg_cnfm>0:
        customer_name.set('')
        customer_phone.set('')
        product.set('')
        product_cost.set(0)
        product_qty.set(0)
        bill_number.set('')
        start()
    else:
        return

def exitsoftware():
    msg_cnf = messagebox.askyesno('Exit','Do You Really Want To Exit?')
    if msg_cnf>0:
        mw.destroy()

def findbill():
    present="no"
    for i in os.listdir("bills\\"):
        if i.split('.')[0]==bill_number.get():
            f3=open(f"bills/{i}",'r')
            textarea.delete(1.0,END)
            for d in f3:
                textarea.insert(END,d)
            f3.close()
            present="yes"
    if present=="no":
        messagebox.showerror("Error",'Invalid Bill Number')


# =============Customer Detail Frame

F1=LabelFrame(mw,text="Customer Details",font=("Arial",16,"bold"),fg="gold",bg=bg_color)
F1.place(x=0,y=70,relwidth=1)

cname_lbl = Label(F1,text="Customer Name:",bg=bg_color,fg='white',font=("Arial",16,"bold"))
cname_lbl.grid(row=0,column=0,padx=10,pady=5)

cname_txt=Entry(F1,width=18,font="arial 16",bd=7,relief=SUNKEN, textvariable=customer_name)
cname_txt.grid(row=0,column=1,padx=10,pady=5)

cphn_lbl = Label(F1,text="Mobile Number:",bg=bg_color,fg='white',font=("Arial",16,"bold"))
cphn_lbl.grid(row=0,column=2,padx=10,pady=5)

cphn_txt=Entry(F1,width=16,font="arial 16",bd=7,relief=SUNKEN, textvariable=customer_phone)
cphn_txt.grid(row=0,column=3,pady=10,padx=5)

cbill_lbl = Label(F1,text="Bill Number:",bg=bg_color,fg='white',font=("Arial",15,"bold"))
cbill_lbl.grid(row=0,column=4,padx=10,pady=5)

cbill_txt=Entry(F1,width=10,font="arial 15",bd=7,relief=SUNKEN, textvariable=bill_number)
cbill_txt.grid(row=0,column=5,padx=10,pady=5)

search_btn=Button(F1,text="Search",font='arial 15 bold',bd=5,width=7,command=findbill)
search_btn.grid(row=0,column=6,padx=10,pady=5)

# ================Product Details Frame

F2=LabelFrame(mw,text="Product Details",font=("Arial",16,"bold"),fg="gold",bg=bg_color)
F2.place(x=0,y=160,width=645,height=253)

item_lbl = Label(F2, text='Product Name:', font=("Arial",16,"bold"), bg=bg_color, fg='lightyellow')
item_lbl.grid(row=0, column=0, padx=30, pady=15)

item_txt = Entry(F2, width=20, font='arial 15 bold', bd=7, relief=SUNKEN, textvariable=product)
item_txt.grid(row=0, column=1, padx=30, pady=15)

cost_lbl = Label(F2, text='Product Cost:\n(Inclusion Of All Taxes)', font=("Arial",16,"bold"), bg=bg_color, fg='lightyellow')
cost_lbl.grid(row=1, column=0, padx=30, pady=15)

cost_txt = Entry(F2, width=20, font='arial 15 bold', bd=7, relief=SUNKEN, textvariable=product_cost)
cost_txt.grid(row=1, column=1, padx=30, pady=15)

quantity_lbl = Label(F2, text='Product Quantity:', font=("Arial",16,"bold"), bg=bg_color, fg='lightyellow')
quantity_lbl.grid(row=2, column=0, padx=30, pady=15)

quantity_txt = Entry(F2, width=20, font='arial 15 bold', bd=7, relief=SUNKEN, textvariable=product_qty)
quantity_txt.grid(row=2, column=1, padx=30, pady=15)



# ==================Buttons

F4=LabelFrame(mw,text="Billing Menu",font=("Arial",16,"bold"),fg="gold",bg=bg_color)
F4.place(x=0,y=415,width=645,height=312)

additem_btn = Button(F4, text='Add Item', font='arial 15 bold', padx=5, pady=10, bg='gold', fg='black', width=15, command=addproduct)
additem_btn.grid(row=1, column=0, padx=50, pady=10)

gntbill_btn = Button(F4, text='Generate Bill', font='arial 15 bold', padx=5, pady=10, bg='gold', fg='black', width=15, command=generate_bill)
gntbill_btn.grid(row=1, column=1, padx=30, pady=10)

savebill_btn = Button(F4, text='Save Bill', font='arial 15 bold', padx=5, pady=10, bg='gold', fg='black', width=15, command=save_bill)
savebill_btn.grid(row=2, column=0, padx=50, pady=10)

prntbill_btn = Button(F4, text='Print Invoice', font='arial 15 bold', padx=5, pady=10, bg='gold', fg='black', width=15, command=print_bill)
prntbill_btn.grid(row=2, column=1, padx=30, pady=10)

clear_btn = Button(F4, text='Reset', font='arial 15 bold', padx=5, pady=10, bg='gold', fg='black', width=15, command=cleardata)
clear_btn.grid(row=3, column=0, padx=50, pady=10)

exit_btn = Button(F4, text='Exit', font='arial 15 bold', padx=5, pady=10, bg='gold', fg='black', width=15, command=exitsoftware)
exit_btn.grid(row=3, column=1, padx=30, pady=10)

# =================Bill Area Frame

F3=Frame(mw,relief=GROOVE,bd=10)
F3.place(x=650,y=160,width=630,height=552)

bill_title = Label(F3, text='Bill Area', font='arial 15 bold', relief=GROOVE, bd=7, bg=bg_color, fg='white')
bill_title.pack(fill=X)

scroll_y = Scrollbar(F3, orient=VERTICAL)
textarea = Text(F3,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()
start()

# ================Developer

Deveoper_lbl = Label(F4, text='"Developed By Adithya"', font='Poppins 18 bold', bg=bg_color, fg='white')
Deveoper_lbl.grid(row=4, columnspan=2)

mw.mainloop()
