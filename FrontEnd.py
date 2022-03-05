from cgitb import text
from faulthandler import disable
from tkinter import *
import sqlite3
import string
import random
indexvar = 0

def login(event=None):
    conn=sqlite3.connect('login.db')

    c = conn.cursor()

    c.execute("SELECT *, oid FROM Login_DB")
    r=c.fetchall()
    
    for rec in r:
        if user_value.get() == rec[0] and pass_value.get() == rec[2]:
            global oid_value
            oid_value = rec[3]
            oid_value = str(oid_value)

            root.destroy()
            nroot = Tk()
            nroot.title("Pass.IO")
            nroot.iconbitmap("icon.ico")
            w_screen = 450
            h_screen = 620
            screen_width = nroot.winfo_screenwidth()
            screen_height = nroot.winfo_screenheight()

            x_cor = (screen_width / 2) - (w_screen / 2)
            y_cor = (screen_height / 2) - (h_screen / 2)

            nroot.geometry("%dx%d+%d+%d" % (w_screen, h_screen, x_cor, y_cor))
            nroot.wm_resizable(width=False, height=False)
            bbg = PhotoImage(file="mainwindow.png")
            imgbbg = Canvas(nroot)
            imgbbg.pack(fill="both", expand=True)
            imgbbg.create_image(225, 310, image=bbg)

            symvar = IntVar()
            numvar = IntVar()
            lowvar = IntVar()
            uppvar = IntVar()
            
            def showpass_his():
                broot = Toplevel()
                broot.title("Pass.IO")
                broot.iconbitmap("icon.ico")
                w_screen = 450
                h_screen = 620
                screen_width = broot.winfo_screenwidth()
                screen_height = broot.winfo_screenheight()

                x_cor = (screen_width / 2) - (w_screen / 2)
                y_cor = (screen_height / 2) - (h_screen / 2)

                broot.geometry("%dx%d+%d+%d" % (w_screen, h_screen, x_cor, y_cor))
                broot.wm_resizable(width=False, height=False)

                conn=sqlite3.connect('passdb.db')
                c = conn.cursor()
                c.execute("SELECT *, oid FROM Pass_DB")
                records=c.fetchall()
                records.reverse()
                print_records = ""
                for rec in records:
                    if user_value.get() == rec[0] and pass_value.get() == rec[1]:
                        print_records += str(rec[2]) + "\n" 
                
                w = Text(broot, height=100,font=("Louis George Café", 20),bg="#ADC4DD")
                w.insert(1.0, print_records)
                w.pack(anchor=CENTER)
                

                conn.commit()
                conn.close()

            def generate_random_password(numvar,symvar,uppvar,lowvar,lenght_pass=14):
                characters = []
                
                
                while True:              
                    if numvar==1:
                        characters.extend(string.digits)                        
                        numvar=0
                                        
                    elif symvar==1:
                        characters.extend("!@#$%^&*()")                        
                        symvar=0
                                        
                    elif uppvar==1:
                        characters.extend(string.ascii_uppercase)                        
                        uppvar=0
                                            
                    elif lowvar == 1:
                        characters.extend(string.ascii_lowercase)                        
                        lowvar=0
                    else:
                        break
                
                len = lenght_pass
                random.shuffle(characters)
                password = []
                for i in range(len):
                    password.append(random.choice(characters))
                random.shuffle(password)
                generated = "".join(password)

                conn=sqlite3.connect('passdb.db')
                c = conn.cursor()
                c.execute("INSERT INTO Pass_DB VALUES (:user_value,:pass_value, :generated)",
                    {
                        "user_value":user_value.get(),
                        "pass_value":pass_value.get(),
                        "generated":generated
                    })
                conn.commit()
                conn.close()

                return(generated)
                
            def gen_fun():
                root = Toplevel() 
                root.title("Pass.IO")
                nroot.iconbitmap("icon.ico")
                w_screen = 450
                h_screen = 620

                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                
                x_cor = (screen_width / 2) - (w_screen / 2)
                y_cor = (screen_height / 2) - (h_screen / 2)
                
                root.geometry("%dx%d+%d+%d" % (w_screen, h_screen, x_cor, y_cor))
                root.wm_resizable(width=False, height=False)
           

                
                bg = PhotoImage(file="gen.png")    
                
                imgbg = Canvas(root)
                imgbg.pack(fill="both", expand=True)
                imgbg.create_image(225, 310, image=bg)

                pass_len = IntVar()
                pass_wid = Entry(root,textvariable=pass_len,font=("Louis George Café", 15),relief=FLAT)
                pass_wid.delete(0,END)
                pass_wid.insert(0,14)             
                imgbg.create_window(225, 340, window=pass_wid, height=30, width=30)
                
                app_button = Button(root, text="Apply", borderwidth=0, relief=FLAT, font=("Louis George Café", 15))
                imgbg.create_window(350, 340, window=app_button)

                gen_var = StringVar()
                gen_pass=Entry(root,textvariable=gen_var, font=("Louis George Café", 20),justify='center')
                gen_pass.delete(0,END)
                gen_pass.insert(0,generate_random_password(1,1,1,1))
                imgbg.create_window(225,60,window=gen_pass,width=425)


                def save_entry():

                    zroot = Toplevel(root)
                    zroot.title("Pass.IO")
                    w_screen = 450
                    h_screen = 620

                    screen_width = zroot.winfo_screenwidth()
                    screen_height = zroot.winfo_screenheight()
                                    
                    x_cor = (screen_width / 2) - (w_screen / 2)
                    y_cor = (screen_height / 2) - (h_screen / 2)
                                    
                    zroot.geometry("%dx%d+%d+%d" % (w_screen, h_screen, x_cor, y_cor))
                    zroot.wm_resizable(width=False, height=False)

                    bg = PhotoImage(file="savepass.png")

                    imgbg = Canvas(zroot)
                    imgbg.pack(fill="both", expand=True)
                    imgbg.create_image(225, 310, image=bg)

                    imgbg.create_text(80, 90, text="Domain", font=("Louis George Café light", 20), fill="#002e47")
                    imgbg.create_text(93, 200, text="Username", font=("Louis George Café light", 20), fill="#002e47")
                    imgbg.create_text(93, 330, text="Password", font=("Louis George Café light", 20), fill="#002e47")

                    domain_value = StringVar()
                    username_value = StringVar()
                    password_value = StringVar()

                    domain_entry = Entry(zroot, textvariable=domain_value, font=("Louis George Café light", 20), bg="#6f7de8", relief= FLAT,fg="#FFFFFF" ) 
                    user_entry = Entry(zroot, textvariable=username_value, font=("Louis George Café light", 20), bg="#6f7de8",relief=FLAT,fg="#FFFFFF" )
                    pass_entry = Entry(zroot, textvariable=password_value, font=("Bahnschrift Light", 20),justify='center', bg="#6f7de8",relief=FLAT, fg="#FFFFFF" )
                    
                    pass_entry.delete(0,END)
                    pass_entry.insert(0,gen_var.get())
                    def new_pass_():
                        pass_entry.delete(0,END)
                        pass_entry.insert(0,generate_random_password(numvar.get(),symvar.get(),uppvar.get(),lowvar.get(),pass_len.get()))
                    regen_button = Button(zroot, text="regenerate password", borderwidth=0, relief=FLAT, font=("Louis George Café Light", 15),bg='#7685f5',activebackground='#7685f5',fg='#002e47',command=new_pass_)
                    imgbg.create_window(225, 430, window=regen_button)

                    imgbg.create_window(225, 140, window=domain_entry, height=35, width=380)
                    imgbg.create_window(225, 250, window=user_entry, height=35, width=380)
                    imgbg.create_window(225, 380, window=pass_entry, height=35, width=380)   

                    def save_butt():
                        conn=sqlite3.connect('savepass.db')
                        c = conn.cursor()
                        c.execute("INSERT INTO save_pass VALUES (:user,:pass,:oid_value,:domain_value,:username_value,:generated)",
                                {
                                    "user":user_value.get(),
                                    "pass":pass_value.get(),
                                    "oid_value":oid_value,
                                    "domain_value":domain_value.get(),
                                    "username_value":username_value.get(),
                                    "generated":password_value.get()
                                })
                        conn.commit()
                        conn.close()
                        domain_entry.delete(0,END)
                        user_entry.delete(0,END)
                        imgbg.create_text(225, 485, text="Password Saved", font=("Louis George Café Light",15))



                    save_entry = Button(zroot, text="Save", borderwidth=0, relief=FLAT, font=("Louis George Café Light", 30),bg='#7685f5',activebackground='#7685f5',fg='#002e47',command=save_butt)                 
                    imgbg.create_window(225, 553, window=save_entry, width= 170 ,height= 70)
                    zroot.mainloop()

                def new_pass():
                    gen_pass.delete(0,END)
                    gen_pass.insert(0,generate_random_password(numvar.get(),symvar.get(),uppvar.get(),lowvar.get(),pass_len.get()))
                                
                def copy_pass():
                    root.clipboard_clear()
                    root.clipboard_append(gen_var.get())


                
                regen_button = Button(root, text="regenerate password", borderwidth=0, relief=FLAT, font=("Louis George Café Light", 15),bg='#004a87',activebackground='#004a87',fg='#f7e8c3',command=new_pass)
                imgbg.create_window(225, 240, window=regen_button)
                
                copy_button = Button(root, text="copy password", borderwidth=0, relief=FLAT, font=("Louis George Café Light", 15),bg='#004a87',activebackground='#004a87',fg='#f7e8c3', command=copy_pass)
                imgbg.create_window(225, 150, window=copy_button)

                hist_button = Button(root, text="password history", borderwidth=0, relief=FLAT, font=("Louis George Café Light", 15),bg='#004a87',activebackground='#004a87',fg='#f7e8c3',command=showpass_his)
                imgbg.create_window(225, 280, window=hist_button)

                save_button = Button(root, text="save password", borderwidth=0, relief=FLAT, font=("Louis George Café Light", 15),bg='#004a87',activebackground='#004a87',fg='#f7e8c3',command=save_entry)
                imgbg.create_window(225, 190    , window=save_button)

                imgbg.create_text(70, 340, text="Length", font=("Louis George Café light", 25), fill="#f7e8c3")

                imgbg.create_text(70, 400, text="A-Z", font=("Louis George Café light", 25), fill="#f7e8c3")

                imgbg.create_text(70, 460, text="a-z", font=("Louis George Café Light", 25), fill="#f7e8c3")

                imgbg.create_text(70, 520, text="0-9", font=("Louis George Café Light", 25), fill="#f7e8c3")

                imgbg.create_text(70, 580, text="!@#$%&*", font=("Louis George Café Light", 25), fill="#f7e8c3")

                
                
                
                uppcb=Checkbutton(root,variable=uppvar,padx=0,pady=0,bg='#004a87',relief=FLAT,activebackground='#004a87')
                uppcb.select()
                imgbg.create_window(400,400,window=uppcb)

                lowcb=Checkbutton(root,variable=lowvar,padx=0,pady=0,bg='#004a87',relief=FLAT,activebackground='#004a87')
                lowcb.select()
                imgbg.create_window(400,460,window=lowcb)

                numcb=Checkbutton(root,variable=numvar,padx=0,pady=0,bg='#004a87',relief=FLAT,activebackground='#004a87')
                numcb.select()
                imgbg.create_window(400,520,window=numcb)

                symcb=Checkbutton(root,variable=symvar,padx=0,pady=0,bg='#004a87',relief=FLAT,activebackground='#004a87')
                imgbg.create_window(400,580,window=symcb)
                symcb.select()

                
                        
                
                root.mainloop()

            def save_fun():
                sroot = Toplevel(nroot)
                sroot.title("Pass.IO")
                sroot.iconbitmap("icon.ico")
                w_screen = 450  
                h_screen = 620  

                screen_width = sroot.winfo_screenwidth() 
                screen_height = sroot.winfo_screenheight()   
                
                x_cor = (screen_width / 2) - (w_screen / 2) 
                y_cor = (screen_height / 2) - (h_screen / 2)    
                
                sroot.geometry("%dx%d+%d+%d" % (w_screen, h_screen, x_cor, y_cor))
                sroot.wm_resizable(width=False, height=False)
                           
                bg__ = PhotoImage(file="savedpass.png")    
                
                imgbg = Canvas(sroot)
                imgbg.pack(fill="both", expand=True)
                imgbg.create_image(225, 310, image=bg__)


                imgbg.create_text(85, 90, text="Domain", font=("Louis George Café bold", 20), fill="#094873")
                imgbg.create_text(98, 190, text="Username", font=("Louis George Café bold", 20), fill="#094873")
                imgbg.create_text(98, 290, text="Password", font=("Louis George Café bold", 20), fill="#094873")


                conn=sqlite3.connect('savepass.db')
                c = conn.cursor()          
                c.execute("SELECT * FROM save_pass ")
                r=c.fetchall()
                emptylist=[]
                conn.close()

                for rec in r:
                    if rec[2] == oid_value:
                        emptylist.append(rec)         
             
                domain_var= StringVar()
                user_var= StringVar()
                pass_var= StringVar()
                
                domain_entry = Entry(sroot,textvariable=domain_var, font=("Louis George Café Light", 20), bg="#db5e5e", relief= FLAT,fg="#3b3f46" ) 
                user_entry = Entry(sroot,textvariable=user_var, font=("Louis George Café Light", 20), bg="#db5e5e",relief=FLAT,fg="#3b3f46" )
                pass_entry = Entry(sroot,textvariable=pass_var, font=("Bahnschrift Light", 20),justify='center', bg="#db5e5e",relief=FLAT, fg="#3b3f46" )
                    
                def show_pass(indexvar=0):

                    domain_entry.delete(0,END)
                    domain_entry.insert(0,emptylist[indexvar][3])

                    user_entry.delete(0,END)
                    user_entry.insert(0,emptylist[indexvar][4])

                    pass_entry.delete(0,END)
                    pass_entry.insert(0,emptylist[indexvar][5])



                    imgbg.create_window(225, 130, window=domain_entry, height=35, width=380)
                    imgbg.create_window(225, 230, window=user_entry, height=35, width=380)
                    imgbg.create_window(225, 330, window=pass_entry, height=35, width=380)

                def next_butt():
                    global indexvar
                    if indexvar != len(emptylist) - 1:
                        indexvar = indexvar + 1 
                    else:
                        indexvar = 0                     
                    show_pass(indexvar)

                def prev_butt():
                    global indexvar
                    if indexvar != 0:
                        indexvar = indexvar - 1 
                    else:
                        indexvar = len(emptylist) - 1                     
                    show_pass(indexvar)

                def edit_butt():
                    eroot = Toplevel(sroot)
                    eroot.title("Pass.IO")
                    eroot.iconbitmap("icon.ico")
                    w_screen = 450  
                    h_screen = 620  

                    screen_width = eroot.winfo_screenwidth() 
                    screen_height = eroot.winfo_screenheight()   
                    
                    x_cor = (screen_width / 2) - (w_screen / 2) 
                    y_cor = (screen_height / 2) - (h_screen / 2)    
                    
                    eroot.geometry("%dx%d+%d+%d" % (w_screen, h_screen, x_cor, y_cor))
                    eroot.wm_resizable(width=False, height=False)
                            
                    bg__ = PhotoImage(file="editpass.png")    
                    
                    imgbg = Canvas(eroot)
                    imgbg.pack(fill="both", expand=True)
                    imgbg.create_image(225, 310, image=bg__)

                    imgbg.create_text(225, 90, text="Enter New Details", font=("Louis George Café bold", 30), fill="#2d2d2d")
                    imgbg.create_text(85, 170, text="Domain", font=("Louis George Café bold", 20), fill="#2d2d2d")
                    imgbg.create_text(98, 270, text="Username", font=("Louis George Café bold", 20), fill="#2d2d2d")
                    imgbg.create_text(98, 370, text="Password", font=("Louis George Café bold", 20), fill="#2d2d2d")

                    newdomain_entry = Entry(eroot, font=("Louis George Café Light", 20), bg="#f5b8c8", relief= FLAT,fg="#2d2d2d") 
                    newdomain_entry.insert(0,domain_entry.get())
                    newuser_entry = Entry(eroot, font=("Louis George Café Light", 20), bg="#f5b8c8",relief=FLAT,fg="#2d2d2d")
                    newuser_entry.insert(0,user_entry.get())
                    imgbg.create_text(225, 410, text=pass_var.get(), font=("Bahnschrift Light", 20), fill="#2d2d2d")                    
                
                    imgbg.create_window(225, 210, window=newdomain_entry, height=35, width=380)
                    imgbg.create_window(225, 310, window=newuser_entry, height=35, width=380)
                    
                    def updatedetails():
                        conn=sqlite3.connect('savepass.db')
                        c = conn.cursor()
                        olddomain = domain_entry.get()
                        newdomain = newdomain_entry.get()
                        olduser = user_entry.get()
                        newuser = newuser_entry.get()
                        c.execute("update save_pass set domain = ?, username = ? where domain = ? and username = ?", (newdomain,newuser,olddomain,olduser))
                        conn.commit()
                        conn.close()

                    def saverecbutt():
                        eroot.destroy()
                        sroot.destroy()
                        save_fun()
                    saverec_button=Button(eroot, text="Save", borderwidth=0, relief=FLAT, font=("Louis George Café Light", 30),bg='#ffbfd0',activebackground='#ffbfd0',fg='#2d2d2d',command=lambda: [updatedetails(),saverecbutt()])                 
                    imgbg.create_window(225,560, window=saverec_button, width= 140 ,height= 80)
        
                    eroot.mainloop()

                show_pass()

                next_button = Button(sroot, text="Next", borderwidth=0, relief=FLAT, font=("Louis George Café Light", 30),bg='#eb6565',activebackground='#eb6565',fg='#094873',command=next_butt)                 
                imgbg.create_window(360,520, window=next_button, width= 120 ,height= 80)

                prev_button = Button(sroot, text="Prev", borderwidth=0, relief=FLAT, font=("Louis George Café Light", 30),bg='#eb6565',activebackground='#eb6565',fg='#094873',command=prev_butt)                 
                imgbg.create_window(90,520, window=prev_button, width= 120 ,height= 80)

                edit_button=Button(sroot, text="Edit", borderwidth=0, relief=FLAT, font=("Louis George Café Light", 30),bg='#eb6565',activebackground='#eb6565',fg='#094873',command=edit_butt)                 
                imgbg.create_window(225,520, window=edit_button, width= 135 ,height= 80)
   
                sroot.mainloop()


            imgbbg.create_text(225,180,text=rec[1], font=("Louis George Café",20),fill="#30a5ff")


            gen_button = Button(nroot, text="Generate Password", borderwidth=0, relief=FLAT, font=("Louis George Café bold", 27),bg='#c6f2c8',activebackground='#c6f2c8',fg='#094873', command= gen_fun) 
            imgbbg.create_window(225, 385, window=gen_button, width=320, height= 50)
            saved_button= Button(nroot, text="View Passwords",borderwidth=0, relief=FLAT, font=("Louis George Café bold", 27),bg='#c6f2c8',activebackground='#c6f2c8',fg='#094873',command= save_fun)
            imgbbg.create_window(225, 520, window=saved_button, width=320, height= 50)


            nroot.mainloop()
    else:
        imgbg.create_text(225, 350, text="User doesnt exist", font=("Bahnschrift Light",15))

def signup(event=None):
          

    def signupnew(event=None): #new signup function
        imgbg.create_text(225, 350, text="User account made", font=("Bahnschrift Light",15))
        conn=sqlite3.connect('login.db')
        c = conn.cursor()
        c.execute("INSERT INTO Login_DB VALUES (:user_entry, :name_entry, :pass_entry)",
            {
                "user_entry":user_value.get(),
                "name_entry":name_value.get(),
                "pass_entry":pass_value.get()
            })
        name_entry.delete(0,END)
        user_entry.delete(0,END)
        pass_entry.delete(0,END)
        conn.commit()
        conn.close()

    nroot = Toplevel()
    nroot.title("Pass.IO")
    nroot.iconbitmap("icon.ico")
    w_screen = 450
    h_screen = 620
    screen_width = nroot.winfo_screenwidth()
    screen_height = nroot.winfo_screenheight()
   

    x_cor = (screen_width / 2) - (w_screen / 2)
    y_cor = (screen_height / 2) - (h_screen / 2)

    nroot.geometry("%dx%d+%d+%d" % (w_screen, h_screen, x_cor, y_cor))
    nroot.wm_resizable(width=False, height=False)


    bg = PhotoImage(file="signup.png")

    imgbg = Canvas(nroot)
    imgbg.pack(fill="both", expand=True)
    imgbg.create_image(225, 310, image=bg)

    imgbg.create_text(225, 50, text="Name", font=("Louis George Café light", 25),fill="#1566c2")
    imgbg.create_text(225, 150, text="Username", font=("Louis George Café light", 25),fill="#1566c2")
    imgbg.create_text(225, 250, text="Password", font=("Louis George Café light", 25),fill="#1566c2")

    name_value = StringVar()
    user_value = StringVar()
    pass_value = StringVar()

    name_entry = Entry(nroot, textvariable=name_value, font=("Louis George Café light", 15),justify='center',relief=FLAT, bg="#e5a8c9",) 
    user_entry = Entry(nroot, textvariable=user_value, font=("Louis George Café light", 15),justify='center',relief=FLAT, bg="#e5a8c9")
    pass_entry = Entry(nroot, textvariable=pass_value, font=("Bahnschrift Light", 15),justify='center',relief=FLAT, bg="#e5a8c9",show="*")

    imgbg.create_window(225, 100, window=name_entry, height=30, width=250)
    imgbg.create_window(225, 200, window=user_entry, height=30, width=250)
    imgbg.create_window(225, 300, window=pass_entry, height=30, width=250)

    login_button = Button(nroot, text="LOGIN", command=nroot.destroy, borderwidth=0, relief=FLAT, font=("Louis George Café Bold", 15),bg='#5dbfe3',activebackground='#5dbfe3',fg='#000000')
    imgbg.create_window(225, 555, window=login_button)

    login_button.bind("<Return>", nroot.destroy)

    signup_button = Button(nroot, text="SIGN UP", command=signupnew, borderwidth=0, relief=FLAT, font=("Louis George Café Bold", 15),bg='#5dbfe3',activebackground='#5dbfe3',fg='#000000')
    imgbg.create_window(225, 485, window=signup_button)

    signup_button.bind("<Return>", signupnew)

    

    nroot.mainloop()

root = Tk()
root.title("Pass.IO")
root.iconbitmap("icon.ico")

w_screen = 450
h_screen= 620
screen_width= root.winfo_screenwidth()
screen_height= root.winfo_screenheight()

x_cor= (screen_width/2) - (w_screen/2)
y_cor= (screen_height/2) - (h_screen/2)

root.geometry("%dx%d+%d+%d" % (w_screen,h_screen, x_cor, y_cor))
root.wm_resizable(width=False,height=False)

bg = PhotoImage(file="loginwindow.png")

imgbg = Canvas(root)
imgbg.pack(fill="both", expand=True)
imgbg.create_image(225, 310, image=bg)

imgbg.create_text(225, 150, text="Username", font=("Louis George Café bold", 25),fill="#ffffff" )
imgbg.create_text(225, 270, text="Password", font=("Louis George Café bold", 25),fill="#ffffff" )

user_value = StringVar()
pass_value = StringVar()
                
user_entry= Entry(root, textvariable=user_value, font=("Louis George Café bold",15),justify='center', bg="#00bbcc", relief= FLAT,fg="#000000")
pass_entry= Entry(root, textvariable=pass_value, font=("Bahnschrift Light",15),justify='center',show="*", bg="#00bbcc", relief= FLAT,fg="#000000")

imgbg.create_window(225,200, window=user_entry, height=30, width=200)
imgbg.create_window(225,320, window=pass_entry, height=30, width=200)


login_button= Button(root, text="LOGIN", command=login, borderwidth= 0, relief=FLAT, font=("Louis George Café Bold", 15),bg='#b2c746',activebackground='#b2c746',fg='#FFFFFF',width=11,height=2)
imgbg.create_window(154,426, window=login_button)

login_button.bind("<Return>", login)

signup_button= Button(root, text="SIGN UP", command=signup, borderwidth= 0, relief=FLAT, font=("Louis George Café Bold", 15),bg='#b2c746',activebackground='#b2c746',fg='#FFFFFF',width=12,height=2)
imgbg.create_window(300,426, window=signup_button)

signup_button.bind("<Return>", signup)

root.mainloop()