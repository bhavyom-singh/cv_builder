## gui for project 2
## raw gui final
import os
from Tkinter import *
import ttk
import tkMessageBox
##cv = {}
name_e = ""
address_e = ""
city_e = ""
state_e = ""
zipp_e = ""
phone_e = ""
email_e=""
clg_e = ""
clg_loc_e = ""
degree_e = ""
lang_e = ""
frame_e = ""
database_e = ""
soft_e = ""
os_e = ""
cname_e = ""
loc_e = ""
position_name_e = ""
position_date_e = ""
duties_e = ""
l1 = []
l2 = []
def mcf():
    top = Tk()
    global name_e
    global address_e
    global city_e
    global state_e
    global zipp_e
    global phone_e
    global email_e
    global clg_e
    global clg_loc_e
    global degree_e
    global lang_e
    global frame_e
    global database_e
    global soft_e
    global os_e
    def newselection(event):
        value_of_combo = combox.get()
        f = open('month_1.txt','w')
        f.write(value_of_combo)
        f.close()

    def newselection_1(event):
        value_of_combo = combox_1.get()
        f = open('year_1.txt','w')
        f.write(value_of_combo)
        f.close()

    def newselection_2(event):
        value_of_combo = combox_2.get()
        f = open('month_2.txt','w')
        f.write(value_of_combo)
        f.close()

    def newselection_3(event):
        value_of_combo = combox_3.get()
        f = open('year_2.txt','w')
        f.write(value_of_combo)
        f.close()
        
    
    def show():
        tkMessageBox.showinfo("Important","Please note that is you are a fresher,put 'NA',in all the fields.")

    top.geometry("500x700")
    top.configure(bg = "white")
    ###
    cntct_l = Label(top,text="CONTACT INFO",pady = 3,bg = "white")
    cntct_l.grid(row = 1, column = 3)
    ###

    name_l = Label(top,text="Name",bg = "white")
    name_l.grid(row = 3, column = 2)

    name_e = Entry(top)
    name_e.grid(row = 3,column = 3)

    address_l = Label(top,text="Address",bg = "white")
    address_l.grid(row = 4, column = 2)

    address_e = Entry(top)
    address_e.grid(row = 4,column = 3)


    city_l = Label(top,text="City",bg = "white")
    city_l.grid(row = 5, column = 2)

    city_e = Entry(top)
    city_e.grid(row = 5,column = 3)

    state_l = Label(top,text="State",bg = "white")
    state_l.grid(row = 6, column = 2)

    state_e = Entry(top)
    state_e.grid(row = 6,column = 3)

    zipp_l = Label(top,text="Zip Code",bg = "white")
    zipp_l.grid(row = 7, column = 2)

    zipp_e = Entry(top,validate = 'focusout',validatecommand=(zipp_l.register(validate_zip),'%d','%i','%S'))
    zipp_e.grid(row = 7,column = 3)

    phone_l = Label(top,text="Phone No.",bg = "white")
    phone_l.grid(row = 8, column = 2)

    phone_e = Entry(top,validate = 'focusout',validatecommand=(phone_l.register(validate_phone),'%d','%i','%S'))
    phone_e.grid(row = 8,column = 3)

    email_l = Label(top,text="Email",bg = "white")
    email_l.grid(row = 9, column = 2)

    email_e = Entry(top,validate = 'focusout',validatecommand=(email_l.register(validate_email),'%d','%i','%S'))
    email_e.grid(row = 9,column = 3)

    do_not_l = Label(top,text="       ",bg = "white")
    do_not_l.grid(row = 10, column = 2)


    ####
    education_l = Label(top,text="EDUCATION",pady = 3,bg = "white")
    education_l.grid(row = 11, column = 3)
    ####

    clg_l = Label(top,text="College Name",bg = "white")
    clg_l.grid(row = 13, column = 2)

    clg_e = Entry(top)
    clg_e.grid(row = 13,column = 3)

    clg_loc_l = Label(top,text="Place",bg = "white")
    clg_loc_l.grid(row = 14, column = 2)

    clg_loc_e = Entry(top)
    clg_loc_e.grid(row = 14,column = 3)

    degree_l = Label(top,text="Degree",bg = "white")
    degree_l.grid(row = 15, column = 2)

    degree_e = Entry(top)
    degree_e.grid(row = 15,column = 3)

    date_from_l = Label(top,text="From",bg = "white")
    date_from_l.grid(row = 16, column = 2)

    combox = ttk.Combobox(top)
    combox["values"] = ('select month','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
    combox.current(0)
    combox.bind("<<ComboboxSelected>>", newselection)
    combox.grid(row = 16,column = 4)

    combox_1 = ttk.Combobox(top)
    combox_1["values"] = ('select year','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020')
    combox_1.current(0)
    combox_1.bind("<<ComboboxSelected>>", newselection_1)
    combox_1.grid(row = 16,column = 3)

    #date_from_e = Entry(top)
    #date_from_e.insert(END, 'from')
    #date_from_e.grid(row = 16,column = 3)

    date_to_l = Label(top,text="To",bg = "white")
    date_to_l.grid(row = 17, column = 2)
    
    combox_2 = ttk.Combobox(top)
    combox_2["values"] = ('select month','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
    combox_2.current(0)
    combox_2.bind("<<ComboboxSelected>>", newselection_2)
    combox_2.grid(row = 17,column = 4)

    combox_3 = ttk.Combobox(top)
    combox_3["values"] = ('select year','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020')
    combox_3.current(0)
    combox_3.bind("<<ComboboxSelected>>", newselection_3)
    combox_3.grid(row = 17,column = 3)
    #date_to_e = Entry(top)
    #date_to_e.insert(END,'to')
    #date_to_e.grid(row = 16,column = 4)

    
    
    #do_not2_l = Label(top,text="                ",bg = "white")
    #do_not2_l.grid(row = 17, column = 2)


    #### tech skill
    no_skill = Label(top,text = "ADD SKILLS",pady = 3,bg = "white")
    no_skill.grid(row = 18, column = 3)
    ####

    global l1 

    lang_l = Label(top,text="Languages",bg = "white")
    lang_l.grid(row = 20, column = 2)

    lang_e = Entry(top)
    lang_e.grid(row = 20,column = 3)

    frame_l = Label(top,text="Frameworks",bg = "white")
    frame_l.grid(row = 21, column = 2)

    frame_e = Entry(top)
    frame_e.grid(row = 21,column = 3)

    database_l = Label(top,text="Databases",bg = "white")
    database_l.grid(row = 22, column = 2)

    database_e = Entry(top)
    database_e.grid(row = 22,column = 3)

    soft_l = Label(top,text="Softwares",bg = "white")
    soft_l.grid(row = 23, column = 2)

    soft_e = Entry(top)
    soft_e.grid(row = 23,column = 3)

    os_l = Label(top,text="Operating Systems",bg = "white")
    os_l.grid(row = 24, column = 2)

    os_e = Entry(top,validate='focusout',validatecommand=show)
    os_e.grid(row = 24,column = 3)

    do_not3_l = Label(top,text="                ",bg = "white")
    do_not3_l.grid(row = 25, column = 2)


    ####
    workx_l = Label(top,text="WORK EXPERIENCE",pady = 3,bg = "white")
    workx_l.grid(row = 26, column = 3)
    ####
    l2 = []
    workx_button = Button(top,text = "Add Experience",command = add_workx,relief = GROOVE)
    workx_button.grid(row = 28,column = 3)
    ####

    donothing_l = Label(top,text="                                  ",bg = "white")##9 tab spaces
    donothing_l.grid(row = 29, column = 1)##to adjust the grid(only entry in column 1)


    b = Button(top,text = "Submit",command = print_kr,relief = GROOVE)
    b.grid(row = 30, column = 3)
    ####
    top.mainloop()

def os_calls():
    
    os.system('python build_resume.py article.txt')
    os.system('make.bat')
    os.system('clean.bat')
    os.rename('article.pdf','C:/Users/test/Desktop/python_generated_cv.pdf')
    os.startfile('C:/Users/test/Desktop/python_generated_cv.pdf')

def validate_zip(why,where,what):
    global zipp_e
    #while True:
    if len(zipp_e.get()) != 6:
        tkMessageBox.showerror('Error','Zip code should be 6 digit long.')
        return False
    else:
        return True
        
def validate_phone(why,where,what):
    global phone_e
    if len(phone_e.get()) != 10:
        tkMessageBox.showerror('Error','Phone no. should be 10 digit long.')
        return False
    else:
        return True
def validate_email(why,where,what):
    global email_e
    if email_e.get().find("@") == -1:
        tkMessageBox.showerror('Error','Incorrect email address')
        return False
    else:
        return True
    
def print_kr():
    name = name_e.get()
    address = address_e.get()
    city = city_e.get()
    state = state_e.get()
    
    zipp = int(zipp_e.get())
    
    phone = int(phone_e.get())
    
    email = email_e.get()

    clg = clg_e.get()
    clg_loc = clg_loc_e.get()
    degree = degree_e.get()
    q = open("month_1.txt",'r')
    w = open("year_1.txt",'r')
    e = open("month_2.txt",'r')
    r = open("year_2.txt",'r')
    date = str(q.read())+" "+str(w.read())+"-"+str(e.read())+" "+str(r.read())
    q.close()
    w.close()
    e.close()
    r.close()

    global l1
    dict1 = {'category':'Languages','entry':lang_e.get()}
    l1.append(dict1)

    dict2 = {'category':'Frameworks','entry':frame_e.get()}
    l1.append(dict2)

    dict3 = {'category':'Databases','entry':database_e.get()}
    l1.append(dict3)

    dict4 = {'category':'Softwares','entry':soft_e.get()}
    l1.append(dict4)

    dict5 = {'category':'Operating Systems','entry':os_e.get()}
    l1.append(dict5)
        
    resume = {'CONTACT_INFO':{'name':name,'address':address,'city':city,'state':state,'zip':zipp,'phone':phone,'email':email},
              'EDUCATION':{'name':clg,'location':clg_loc,'degree':degree,'dates':date},
              'TECHNICAL_SKILLS':l1
              ,'WORK_EXPERIENCE':l2
              }
##    for val in resume:
##        for vals in resume[val]:
##            print(resume[val][vals])
    #for eachval in resume:
    print(resume)
    f = open('article.txt','a+')
    f.write("RESUME = ")
    f.write(str(resume))
    f.close()
    
    
    os_calls()

def add_workx():
#    tkMessageBox.showinfo("Important","Please note that is you are a fresher,put 'NA',in all the fields.")
    def add_to_l2():
        dictx = {}
        dictx.setdefault('name','NA')
        dictx['name'] = cname_e.get()
        
        dictx.setdefault('location','NA')
        dictx['location'] = loc_e.get()

        q = open("month_11.txt",'r')
        w = open("year_11.txt",'r')
        e = open("month_22.txt",'r')
        r = open("year_22.txt",'r')
        position_date_e = str(q.read())+" "+str(w.read())+" - "+str(e.read())+" "+str(r.read())
        q.close()
        w.close()
        e.close()
        r.close()

        dictx1 = {}
        dictx1.setdefault('name','NA')
        dictx1.setdefault('dates','NA')
        dictx1 = {'name':position_name_e.get(),'dates':position_date_e}
        
        dictx['positions'] = [dictx1]
        dictx.setdefault('duties',[]).append('NA')
        dictx['duties'] = [duties_e.get()]
        global l2
        l2.append(dictx)
        workx.destroy()

    def newselection_0(event):
        value_of_combo = combox_0.get()
        f = open('month_11.txt','w')
        f.write(value_of_combo)
        f.close()

    def newselection_11(event):
        value_of_combo = combox_11.get()
        f = open('year_11.txt','w')
        f.write(value_of_combo)
        f.close()

    def newselection_22(event):
        value_of_combo = combox_22.get()
        f = open('month_22.txt','w')
        f.write(value_of_combo)
        f.close()

    def newselection_33(event):
        value_of_combo = combox_33.get()
        f = open('year_22.txt','w')
        f.write(value_of_combo)
        f.close()
    global cname_e
    global loc_e
    global position_name_e
    global position_date_e
    global duties_e
    workx = Tk()
    workx.geometry("500x300")
    workx.configure(bg = "white")
    
    head_l = Label(workx,text = "ADD WORK EXPERIENCE",bg = "white")
    head_l.grid(row = 1,column = 3)

    cname_l = Label(workx,text = "Company Name",bg = "white")
    cname_l.grid(row = 2)

    cname_e = Entry(workx)
    cname_e.grid(row=2,column=2)

    loc_l = Label(workx,text = "Location",bg = "white")
    loc_l.grid(row=3)

    loc_e = Entry(workx)
    loc_e.grid(row=3,column=2)
    
    position_l = Label(workx,text = "Positions",bg = "white")
    position_l.grid(row=4)

    position_name_l = Label(workx,text = "Name",bg = "white")
    position_name_l.grid(row=4,column = 2)

    position_date_from_l = Label(workx,text = "From",bg = "white")
    position_date_from_l.grid(row=5,column = 2)

    position_date_to_l = Label(workx,text = "To",bg = "white")
    position_date_to_l.grid(row=6,column = 2)
    
    position_name_e = Entry(workx)
    position_name_e.grid(row=4,column=3)

    combox_0 = ttk.Combobox(workx)
    combox_0["values"] = ('select month','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
    combox_0.current(0)
    combox_0.bind("<<ComboboxSelected>>", newselection_0)
    combox_0.grid(row = 5,column = 3)

    combox_11 = ttk.Combobox(workx)
    combox_11["values"] = ('select year','2013','2014','2015','2016','2017','2018','2019','2020')
    combox_11.current(0)
    combox_11.bind("<<ComboboxSelected>>", newselection_11)
    combox_11.grid(row = 5,column = 4)

    combox_22 = ttk.Combobox(workx)
    combox_22["values"] = ('select month','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
    combox_22.current(0)
    combox_22.bind("<<ComboboxSelected>>", newselection_22)
    combox_22.grid(row = 6,column = 3)

    combox_33 = ttk.Combobox(workx)
    combox_33["values"] = ('select year','2013','2014','2015','2016','2017','2018','2019','2020')
    combox_33.current(0)
    combox_33.bind("<<ComboboxSelected>>", newselection_33)
    combox_33.grid(row = 6,column = 4)
    
     

##    position_date_e = Entry(workx)
##    position_date_e.grid(row=5,column=3)
    
    duties_l = Label(workx,text = "Duties",bg = "white")
    duties_l.grid(row=7)

    duties_e = Entry(workx)
    duties_e.grid(row=7,column=2)

    add_ex_b = Button(workx,text = "Add Experience" ,command =add_to_l2,relief = GROOVE )
    add_ex_b.grid(row = 9,column = 2)

    workx.mainloop()
#### writing resume to txt file


