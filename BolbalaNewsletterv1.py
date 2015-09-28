"""Let US DO THIS. @BOLBALA. @Authors: Mustafa, Jhala and Yashwant"""


from Tkinter import *
import math,time,random
from tkMessageBox import *
''' BOLBALA! @Jhala, Yashwant and Mustafa'''
import smtplib
from datetime import datetime
# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText

from Tkinter import *
import Tkinter,tkFileDialog
#from PIL import ImageTk,Image
f = None
jke1=None
jke2=None
jke3=None
pathofimage=None
detailgui=None
q=None
v1=None
v2=None
v3=None
v4=None
v5=None
v6=None
v7=None
v8=None
v9=None
v0=None
c1=None
c2=None
c3=None
c4=None
c5=None
c6=None
c7=None
c8=None
c9=None
c0=None
eventvar=None
datevar=None

def check():
    print('Working.')

def detailwrite():
    global detailgui,jke1,jke2,jke3
    print "Reached here"
    if(jke1.get() == '' or jke2.get() =='' or jke3.get(0.0,END) =='\n'):
        if(jke1.get() == ''):
            showinfo('Error!',"Enter Event Name!")
        elif(jke2.get() ==''):
            showinfo('Error!',"Enter Date!")
        else:
            showinfo('Error!','Enter Event details!')
        
    else:                 
        print len(jke3.get(0.0,END))
        print jke3.get(0.0,END)
        global f
        global pathofimage
        f= open('BolbalaEvents.txt','a')
        try:     
            
            f.write('Event - ' +jke1.get() + '\n')
            f.write('Date : ' +jke2.get() + "\n")
            f.write('Details - '+jke3.get(0.0, END) + '\n')
            if pathofimage is not None:
                f.write("["+pathofimage+"]" + '\n')
            f.write('------------------------------------------------------------------------- \n')
        except Exception as e:
            print e
        f.close()
        pathofimage=None
        print "reached here"
        detailgui.destroy()
def attachimage():
    root = Tkinter.Tk()
    global pathofimage
    pathofimage = tkFileDialog.askopenfilename(title='Choose a file')
def _details() :
    global detailgui
    detailgui =Tk()
    detailgui.title('Add Data')
    detailgui.geometry('1366x786')
    detailgui.configure(bg='papaya whip')
    global eventvar
    eventvar=StringVar()
    global datevar
    datevar=StringVar()
    #frames
    jkf1= Frame(detailgui,bg='papaya whip')
    #Labels
    jklabel1= Label(jkf1,bg='papaya whip', text = "New Event", width=8, font =('Times New Roman',17))
    global jke1
    jke1 = Entry(jkf1,bg='seashell', textvariable= eventvar,font =('Times New Roman',14))
    jklabel2= Label(jkf1,bg='papaya whip', text='Date', width =5, font = ('Times New Roman', 17))
    global jke2
    jke2 = Entry(jkf1,bg='seashell',textvariable=datevar, font =('Times New Roman', 14))
    jklabel3 = Label(jkf1,bg='papaya whip', text='Event Details', width =9, font=('Times New Roman',17))
    global jke3
    jke3=Text(jkf1, bg='seashell', font=('Times New Roman', 14),width=75)
    jktplabel1=Label(jkf1, bg='papaya whip', height =4)
    JKB1 =Button(jkf1, bg='papaya whip', text= 'Done', command=detailwrite, width=5,font =('Times New Roman',14))
    JKB2 =Button(jkf1, bg='papaya whip', text= 'Attach an Image', command=attachimage, width=15,font =('Times New Roman',14))
    #packing
    
    JKB1.pack(side='bottom')
    JKB2.pack(side='bottom')
    global detailvar
    detailvar=jke3.get(0.0,END)
    jke3.pack(side='bottom')
    jklabel3.pack(side='bottom')
    jktplabel1.pack(side='bottom')
    jklabel1.pack(side='left')
    jke1.pack(side='left')
    jke2.pack(side='right')
    jklabel2.pack(side='right')
    jkf1.pack()
    

    
    
def _Register():
    root = Tk()
    root.configure(bg = 'papaya whip')
    text = Text(root)
    text.grid()
    scrl = Scrollbar(root, command=text.yview)
    text.config(yscrollcommand=scrl.set)
    file = open('BolbalaEvents.txt','r+')
    text.insert(END, file.read())
    scrl.grid(row=0, column=1, sticky='ns')
eventvar1=None
datevar1=None
jke31=None
jke21=None
jke11=None
def _Invitation():
    global detailfui,eventvar1,datevar1,jke31,jke21,jke11
    detailfui =Tk()
    detailfui.title('Invitation')
    detailfui.geometry('1366x786')
    detailfui.configure(bg='papaya whip')
    eventvar1=StringVar()
    datevar1=StringVar()
    
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global c8
    global c9
    global c0
    
    global v1
    global v2
    global v3
    global v4
    global v5
    global v6
    global v7
    global v8
    global v9
    global v0
    
    v1=IntVar()
    v2=IntVar()
    v3=IntVar()
    v4=IntVar()
    v5=IntVar()
    v6=IntVar()
    v7=IntVar()
    v8=IntVar()
    v9=IntVar()
    v0=IntVar()
    
    #frames
    jkf1= Frame(detailfui,bg='papaya whip')
    c1 = Checkbutton(jkf1, text="",bg='papaya whip', variable=v1,command=f1)
    c2= Checkbutton(jkf1, text="",bg='papaya whip', variable=v2,command=f2)
    c3 = Checkbutton(jkf1, text="Banks",bg='papaya whip', variable=v3,command=f3)
    c4 = Checkbutton(jkf1, text="Youth",bg='papaya whip', variable=v4,command=f4)
    c5 = Checkbutton(jkf1, text="Advocate",bg='papaya whip', variable=v5,command=f5)
    c6 = Checkbutton(jkf1, text="Doctor",bg='papaya whip', variable=v6,command=f6)
    c7 = Checkbutton(jkf1, text="Senior Citizen",bg='papaya whip', variable=v7,command=f7)
    c8 = Checkbutton(jkf1, text="Donor",bg='papaya whip', variable=v8,command=f8)
    c9= Checkbutton(jkf1, text="Trustee",bg='papaya whip', variable=v9,command=f9)
    c0 = Checkbutton(jkf1, text="",bg='papaya whip', variable=v0,command=f0)
    c1.var=v1
    c2.var=v2
    c3.var=v3
    c4.var=v4
    c5.var=v5
    c6.var=v6
    c7.var=v7
    c8.var=v8
    c9.var=v9
    c0.var=v0

    
        
    #Labels
    jklabel4=Label(jkf1,bg='papaya whip', text='INVITATION', width =10, font =('Times New Roman',25))
    jklabel1= Label(jkf1,bg='papaya whip', text = "Event", width=8, font =('Times New Roman',13))
    jke11 = Entry(jkf1,bg='seashell', textvariable= eventvar1,font =('Times New Roman',14))
    jklabel2= Label(jkf1,bg='papaya whip', text='Date Of Event', width =12, font = ('Times New Roman', 13))
    jke21 = Entry(jkf1,bg='seashell',textvariable=datevar1, font =('Times New Roman', 14))
    jklabel3 = Label(jkf1,bg='papaya whip', text='Event Details', width =9, font=('Times New Roman',14))
    jke31=Text(jkf1, bg='seashell', font=('Times New Roman', 14),width=75,height=7,yscrollcommand=5)
    jktplabel1=Label(jkf1, bg='papaya whip', height =1)
    jktplabel3=Label(jkf1,bg='papaya whip',height=2)
    jktplabel2=Label(jkf1,bg='papaya whip',height=2)
    jktplabel4=Label(jkf1,bg='papaya whip',height=2)
    JKB1 =Button(jkf1, bg='dim gray', text= 'Send Invitation',command= _sendInv, width=15,font =('Times New Roman',14))
    JKB2 =Button(jkf1, bg='dim gray', text= 'Cancel', command = detailfui.destroy, width=8,font =('Times New Roman',14))

    #packing
    JKB2.pack(side='bottom')
    JKB1.pack(side='bottom')
    c0.pack(side='bottom')
    c1.pack(side='bottom')
    c2.pack(side='bottom')
    c3.pack(side='bottom')
    c4.pack(side='bottom')
    c5.pack(side='bottom')
    c6.pack(side='bottom')
    c7.pack(side='bottom')
    c8.pack(side='bottom')
    c9.pack(side='bottom')
    
    jktplabel4.pack(side='bottom')
    jke31.pack(side= 'bottom')
    jklabel3.pack(side='bottom')
    jktplabel1.pack(side='bottom')
    jklabel1.pack(side='left')
    jke11.pack(side='left')
    jke21.pack(side='right')
    jklabel2.pack(side='right')
    jktplabel2.pack(side='bottom')
    jktplabel3.pack(side='bottom')
    jklabel4.pack(side='bottom')
    jkf1.pack()

    
def _sendInv():
    print "Send Invitation pressed!"
    global c1,c2,c3,c4,c5,c6,c7,c8,c9,c0
    global v1,v2,v3,v4,v5,v6,v7,v8,v9,v0
    global q,jke11,jke21,eventvar1,datevar1
    if(v0.get() == 1):
        #fil = open('','r')
        #q=fil.readlines()
        mandrillInvite(["hello"])
        q=''
        #fil.close()
    if(v1.get() == 1):
        #fil = open('','r')
        #q=fil.readlines()
        mandrillInvite(["hello1"])
        q=''
        #fil.close()
    if(v2.get() == 1):
        #fil = open('','r')
        #q=fil.readlines()
        mandrillInvite(["hello2"])
        q=''
        #fil.close()
    if(v3.get() == 1):
        #fil = open('Banks.txt','r')
        #q=fil.readlines()
        mandrillInvite(["hello3"])
        q=''
        #fil.close()
    if(v4.get() == 1):
        #fil = open('Youth.txt','r')
        #q=fil.readlines()
        #SENDIT()
        mandrillInvite(["hello4"])
        q=''
        #fil.close()
    if(v5.get() == 1):
        #fil = open('Advocate.txt','r')
        #q=fil.readlines()
        #SENDIT()
        q=''
        mandrillInvite(["hello5"])
        #fil.close()
    if(v6.get()== 1):
        fil = open('Doctor.txt','r')
        q=fil.readlines()
        #SENDIT()
        mandrillInvite(q)
        q=''
        fil.close()
    if(v7.get() == 1):
        #fil = open('SeniorCitizen.txt','r')
        #q=fil.readlines()
        #SENDIT()
        q=''
        mandrillInvite(["hello7"])
        #fil.close()
    if(v8.get()== 1):
        #fil = open('Donor.txt','r')
        #q=fil.readlines()
        #SENDIT()
        q=''
        mandrillInvite(["hello8"])
        #fil.close()
    if(v9.get() == 1):
        #fil = open('Trustee.txt','r')
        #q=fil.readlines()
        #SENDIT()
        #q=''
        #fil.close()
        mandrillInvite(["hello9"])
def SENDIT():
    global q
    #Write madrill
    print "Sent to " + q


detailfui=None
def f1():
    global v1
    if v1.get()==0:
        v1.set(1)
    else:
        v1.set(0)
    
def f2():
    global v2
    if v2.get()==0:
        v2.set(1)
    else:
        v2.set(0)
    
def f3():
    global v3
    if v3.get()==0:
        v3.set(1)
    else:
        v3.set(0)
    
def f4():
    global v4
    if v4.get()==0:
        v4.set(1)
    else:
        v4.set(0)
    
def f5():
    global v5
    if v5.get()==0:
        v5.set(1)
    else:
        v5.set(0)
    
def f6():
    global v6
    if v6.get()==0:
        v6.set(1)
    else:
        v6.set(0)
    
def f7():
    global v7
    if v7.get()==0:
        v7.set(1)
    else:
        v7.set(0)
    
def f8():
    global v8
    if v8.get()==0:
        v8.set(1)
    else:
        v8.set(0)
    
def f9():
    global v9
    if v9.get()==0:
        v9.set(1)
    else:
        v9.set(0)
def f0():
    global v0
    if v0.get()==0:
        v0.set(1)
    else:
        v0.set(0)



def _Newsletter():
    try:
        # Specifying the from and to addresses

        strFrom = 'Shri Bolbala Trust <shribolbala2@gmail.com>'
        

        # Writing the message (this message will appear in the email)
        global f
        message = MIMEMultipart()
        
        x=datetime.now()
        
    #    message['Subject'] = 'Bolbala Newsletter ' +str(x.day)+":"+str(x.month)+":"+str(x.year)
        message['Subject'] = 'Bolbala Invitation ' +str(x.day)+":"+str(x.month)+":"+str(x.year)

        
# me == the sender's email address
# family = the list of all recipients' email addresses
        message['From'] = strFrom
        message['To'] = ""
     #   message.preamble = 'Bolbala Newsletter ' 
        message.preamble = 'Bolbala Invitation ' 

        f= open('BolbalaEvents.txt','r')
        msg = f.read().split('------------------------------------------------------------------------- \n')
        textPart=""
        for i in msg:
            l=i.split("\n")
            
            event=l[0]
            for lmn in range(len(l)):
                print l[lmn]
                if l[lmn]=="":
                    continue
                if l[lmn][0]=='[':
                    
                    
                    fp = open(l[lmn][1:-1], 'rb')
                    img = MIMEImage(fp.read())
                    fp.close()
                    hh=event+"."+l[lmn][1:-1].split(".")[-1] 
                    print hh
                    try:
                        img.add_header('Content-Disposition', 'attachment',filename=hh)
                    except Exception as ee:
                        print ee
                    message.attach(img)
                else:
                   textPart+=l[lmn]
                   textPart+="\n"
            textPart+="-----------------------------------------------------\n"
        textPart+="\n\n\n"
        textPart+="We highly value your feedback. Please give us your feedback here: http://goo.gl/XafN0q"
        
        print textPart
        tp=MIMEText(textPart)
        message.attach(tp)
        # Gmail Login

        username = 'shribolbala2@gmail.com'
        password = 'j-fJ-cwn5F_rA2MRUilTwQ'
        username2='shribolbala1@gmail.com'
        password2='RH4DBoMl9H0Jug8Ua6nUKQ'
        # Sending the mail
        username3='shribolbala3@gmail.com'
        password3='twaBQCLNpOW4YKihlge3kg'
        
        server = smtplib.SMTP('smtp.mandrillapp.com',587)
        
        server.login(username,password)
        server2=smtplib.SMTP('smtp.mandrillapp.com',587)
        server2.login(username2,password2)
        server3=smtplib.SMTP('smtp.mandrillapp.com',587)
        server3.login(username3,password3)
        g=open("jhala.txt","r")
        m=g.readlines()
        var=2
        print m
        g.close()
        for qqq in m:
            try:
              #  message['To']=qqq
                if var==0:
                    server.sendmail(strFrom, qqq, message.as_string())
                    var=0
                elif var==1:
                    server2.sendmail(strFrom, qqq, message.as_string())
                    var=1
                else:
                    server3.sendmail(strFrom, qqq, message.as_string())
                    var=2
                    
                print "Sent to "+qqq
            except  Exception as e:
                print e
        server.quit()
        server2.quit()
        server3.quit()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("bolbalanewsletter@gmail.com","jaybajrangbali")
        server.sendmail("bolbalanewsletter@gmail.com","bolbalanewsletter@gmail.com",message.as_string())
        server.quit()
    except Exception as e:
        print e
        askretrycancel("Error!", 'No Internet connectivity. Please try again.')
        
def mandrillInvite(mails):
    global eventvar1,datevar1,jke31,jke11,jke21
    print mails
    try:
        strFrom = 'Shri Bolbala Trust <shribolbala2@gmail.com>'
        message = MIMEMultipart()
        x=datetime.now()
        message['Subject'] = 'Invitation for ' + jke11.get()+' on '+jke21.get()
        print message['Subject']
        message['From'] = strFrom
        message['To'] = ""
        message.preamble = message['Subject'] 
        textPart=jke31.get(0.0,END)
        tp=MIMEText(textPart)
        message.attach(tp)
        print textPart
        username = 'shribolbala2@gmail.com'
        password = 'j-fJ-cwn5F_rA2MRUilTwQ'
        username2='shribolbala1@gmail.com'
        password2='RH4DBoMl9H0Jug8Ua6nUKQ'
        sername3='shribolbala3@gmail.com'
        password3='twaBQCLNpOW4YKihlge3kg'
        server = smtplib.SMTP('smtp.mandrillapp.com',587)
        server.login(username,password)
        server2=smtplib.SMTP('smtp.mandrillapp.com',587)
        server2.login(username2,password2)
        server3=smtplib.SMTP('smtp.mandrillapp.com',587)
        server3.login(username3,password3)
        var=0
        
        for qqq in mails:
            try:
                if var==0:
                    server.sendmail(strFrom, qqq, message.as_string())
                    var=1
                elif var==1:
                    server2.sendmail(strFrom, qqq, message.as_string())
                    var=2
                else:
                    server3.sendmail(strFrom, qqq, message.as_string())
                    var=0
                    
                print "Sent to "+qqq
            except  Exception as e:
                print e
        server.quit()
        server2.quit()
        server3.quit()
        
    except Exception as e:
        print e
        askretrycancel("Error!", 'No Internet connectivity. Please try again.')
        


def passwordAccepted():
    global root
    root.destroy()
    gui=Tk()
    gui.title('Bolbala Newsletter')
    gui.geometry('1366x768')
    gui.configure(bg='white')
    kjf1= Frame(gui, height=100,width=140, bg='white')
    kjlabel1=Label(kjf1, bg='white',text= "BOLBALA NEWSLETTER v1.0",height=4, width=100, font=('Times New Roman',40))
    kjtplabel1=Label(kjf1,bg = 'white',height=2,width=100)
    kjtplabel2=Label(kjf1,bg = 'white',height=2,width=100)
    kjtplabel3=Label(kjf1,bg = 'white',height=2,width=100)
    kjB1= Button(kjf1,text="Add Details",justify=RIGHT,command=_details,bg='black',fg='white',width = 20, pady=15)
    kjB2= Button(kjf1,text="Send Invitation",bg='black',fg='white',justify=RIGHT,command=_Invitation,width = 20, pady=15)
    kjB3= Button(kjf1,text="View Register",bg='black',fg='white',justify=RIGHT,command=_Register,width = 20, pady=15)
    kjB4= Button(kjf1,text="Send NewsLetter",bg='black',fg='white',command=_Newsletter,width = 20, pady=15)
    kjB4.pack(side='bottom')
    kjtplabel3.pack(side='bottom')
    kjB2.pack(side='bottom')
    kjtplabel2.pack(side='bottom')
    kjB3.pack(side='bottom')
    kjtplabel1.pack(side='bottom')
    kjB1.pack(side='bottom')
    kjf1.pack()
    kjlabel1.pack(side='bottom')
    gui.mainloop()

root=Tk()
passwordVariable=None
YKEntryForPassword=None
YKFont=('Times New Roman',48)
YKFontForLabels=('Arial',10)
YKFontForPassword=('Arial',14)
YKFontForInstructions=('Arial',18)
currentPassword=None
newPassword=None
confirmNewPassword=None
toggle=0
def changePassword():
    global currentPassword,newPassword,confirmNewPassword
    YKCP=currentPassword.get()
    YKNP=newPassword.get()
    YKCNP=confirmNewPassword.get()
    passwordFile=None
    try:
        passwordFile=file("bolbala.txt","r")
    except Exception as e:
        about=showinfo(title="Error",message="File Not Found")
    YKSP=passwordFile.read()
    passwordFile.close()
    YKSP=decrpytpass(YKSP)
    if YKSP==YKCP:
        if YKNP==YKCNP:
            passwordFile=file("bolbala.txt","w")
            passwordFile.write(encryptpass(YKNP))
            passwordFile.close()
            about=showinfo(title="Successfull",message="Password Changed")
        else:
            about=showinfo(title="Error",message="The new Password and Confirm New Password do not match.")
    else:
        about=showinfo(title="Error",message="The current Password entered is wrong")
    currentPassword.set("Hello")
    newPassword.set("Hello")
    confirmNewPassword.set("Hello")
def encryptpass(inputpass):
    newpass=''
    f=random.randint(0,len(inputpass)-1)
    #print(f)
    for i in range(f,len(inputpass)):
        newpass+=inputpass[i]
    for i in range(0,f):
        newpass+=inputpass[i]
    
    mid=len(newpass)//2
    finalpass2=newpass[mid:len(newpass)]+newpass[0:mid]
    finalpass=''
    for i in range(0,len(finalpass2)):
        if(i%2==0):
            zf=ord(finalpass2[i])
            if(zf+f<=255):
                zf+=f
            else:
                zf=(zf+f)%256
            finalpass+=chr(zf)
        else:
            zf=ord(finalpass2[i])
            if(zf-f<0):
                zf=256+zf-f
            else:
                zf-=f;
            finalpass+=chr(zf)
    finalpass+=chr(f)
    
    return finalpass

def decrpytpass(encryptedpass):
    multiplier=ord(encryptedpass[len(encryptedpass)-1])
    semi2=encryptedpass[0:len(encryptedpass)-1]
    semi=''
    for i in range(0,len(semi2)):
        if(i%2==0):
            q=ord(semi2[i])
            if(q<multiplier):
                semi+=chr(256-multiplier)
            else:
                semi+=chr(q-multiplier)
        else:
            q=ord(semi2[i])
            q+=multiplier
            if(q>255):
                semi+=chr(q%256)
            else:
                semi+=chr(q)
    mid=len(semi)//2
    if(len(semi)%2==1):
        mid+=1
    semi=semi[mid:len(semi)]+semi[0:mid]
    finalans=''
    for j in range(len(semi)-multiplier,len(semi)):
        finalans+=semi[j]
    for j in range(0,len(semi)-multiplier):
        finalans+=semi[j]
    return finalans



def showPassword():
    global toggle
    if toggle==0:
        YKEntryForPassword.configure(show="")
        toggle=1
    else:
        YKEntryForPassword.configure(show="*")
        toggle=0
    
def checkThis():
    entered=passwordVariable.get()
    passwordFile=None
    try:
        passwordFile=file("bolbala.txt","r")
        checkWith=passwordFile.read()
        checkWith=decrpytpass(checkWith)
        if checkWith==entered:
            passwordAccepted()
            #about=showinfo(title="Correct",message="Correct")
            
        else:
            about=showinfo(title="Incorrect",message="Incorrect")

    except Exception as e:
        print e
        about=showinfo(title="Error",message="File Not Found")
    passwordVariable.set("AAAAAA")
l=None

def main():
    global YKEntryForPassword,passwordVariable,YKFont,YKFontForLabels,YKFontForPassword,YKFontForInstructions
    global currentPassword,newPassword,confirmNewPassword
    passwordVariable=StringVar()
    passwordVariable.set("AAAAAA")
    root.configure(background='white')
    root.title('Newsletter Bolbala')
    #root.resizable(1024,768)
    
    #THR FRAME FOR PASSWORD
    YKFrameForPassword=Frame(root,bg="white")
    YKLabelForPaddingUpInPassword=Label(YKFrameForPassword,bg="white",text="",width=20)
    YKLabelForPaddingUpInPassword.pack(side=BOTTOM)
    YKLabelForInstructions=Label(YKFrameForPassword,text="Enter the password to continue.",bg="white",font=YKFontForInstructions,pady=10,padx=10)
    
    YKLabelForInstructions.pack()
    #Frame inside "The Frame For Password". Nesting Level=1
    
    YKFrameForALine=Frame(YKFrameForPassword,bg="white")
    """YKLabelForPassword=Label(YKFrameForALine,bg="white",text="Password",width=10,font=YKFontForLabels)
    
    YKLabelForPassword.pack(side=LEFT)"""
    YKButtonForPassword=Button(YKFrameForALine,bg="black",fg="white",text="Toggle",command=showPassword)
    YKButtonForPassword.pack(side=RIGHT)
    YKLabelBetween=Label(YKFrameForALine,bg="white",width=3)
    YKLabelBetween.pack(side=RIGHT)
    YKEntryForPassword=Entry(YKFrameForALine,bg="white",textvariable=passwordVariable,font=YKFontForPassword,show="*")
    YKEntryForPassword.pack(side=RIGHT)
    
    YKFrameForALine.pack()
    YKLabelForButton=Label(YKFrameForPassword,bg="white",width=20)
    YKLabelForButton.pack()
    YKButtonLogin=Button(YKFrameForPassword,text="Login",bg="black",fg="white",padx=5,pady=5,font=YKFontForInstructions,command=checkThis)
    YKButtonLogin.pack()
    YKLabelBetweenButtons=Label(YKFrameForPassword,bg="white",width=20)
    YKLabelBetweenButtons.pack()
    YKLabelBetweenButtons2=Label(YKFrameForPassword,bg="white",width=20)
    YKLabelBetweenButtons2.pack()
    YKLabelChangePassword=Label(YKFrameForPassword,text="Change Password",bg="white",font=YKFontForInstructions)
    YKLabelChangePassword.pack()
    currentPassword=StringVar()
    currentPassword.set("Hello")
    confirmNewPassword=StringVar()
    confirmNewPassword.set("Hello")
    newPassword=StringVar()
    newPassword.set("Hello")
    YKLabelStart=Label(YKFrameForPassword,bg="white",width=3)
    YKLabelStart.pack()
    YKFrameCurrent=Frame(YKFrameForPassword,bg="white")
    YKLabelCurrentPassword=Label(YKFrameCurrent,bg="white",fg="black",text="Current Password:",width=21,justify=CENTER,font=YKFontForLabels)
    YKLabelCurrentPassword.pack(side=LEFT)
    YKCurrentPassword=Entry(YKFrameCurrent,bg="white",text="DDD",textvariable=currentPassword,font=YKFontForPassword,show="*")
    YKCurrentPassword.pack(side=LEFT)
    YKLabelRightC=Label(YKFrameCurrent,width=3,bg="white")
    YKLabelRightC.pack()
    
    YKFrameCurrent.pack()
    YKLabelA=Label(YKFrameForPassword,bg="white",width=3)
    YKLabelA.pack()
    YKFrameNew=Frame(YKFrameForPassword,bg="white")
    YKLabelNewPassword=Label(YKFrameNew,bg="white",fg="black",text="New Password:",width=21,justify=CENTER,font=YKFontForLabels)
    YKLabelNewPassword.pack(side=LEFT)

    YKNewPassword=Entry(YKFrameNew,bg="white",text="DDD",textvariable=newPassword,font=YKFontForPassword,show="*")
    YKNewPassword.pack(side=LEFT)
    YKLabelRightB=Label(YKFrameNew,width=3,bg="white")
    YKLabelRightB.pack()
    
    YKFrameNew.pack()
    YKLabelB=Label(YKFrameForPassword,bg="white",width=3)
    YKLabelB.pack()
    YKFrameConfirm=Frame(YKFrameForPassword,bg="white")
    YKLabelConfirmPassword=Label(YKFrameConfirm,bg="white",fg="black",text="Confirm New Password:",width=21,justify=CENTER,font=YKFontForLabels)
    YKLabelConfirmPassword.pack(side=LEFT)
    YKConfirmPassword=Entry(YKFrameConfirm,bg="white",text="DDD",textvariable=confirmNewPassword,font=YKFontForPassword,show="*")
    YKConfirmPassword.pack(side=LEFT)
    YKLabelRightA=Label(YKFrameConfirm,width=3,bg="white")
    YKLabelRightA.pack()
    YKFrameConfirm.pack()    
    YKLabelC=Label(YKFrameForPassword,bg="white",width=3)
    YKLabelC.pack()
    YKLabelD=Label(YKFrameForPassword,bg="white",width=3)
    YKLabelD.pack()
    YKButtonChangePassword=Button(YKFrameForPassword,text="Change Password",bg="black",fg="white",padx=5,pady=5,font=YKFontForInstructions,command=changePassword)
    YKButtonChangePassword.pack()
    YKLabelE=Label(YKFrameForPassword,bg="white",width=3)
    YKLabelE.pack()
    YKLabelForName=Label(YKFrameForPassword,bg="white",fg="black", text="Developed by: Kuljeet, Mustafa and Yashwant.",width=500,justify=RIGHT)
    YKLabelForName.pack()
    YKFrameForPassword.pack(side=BOTTOM)
    #THE FRAME FOR TITLE
    YKFrameForTitle=Frame(root,bg='white')
    YKLabelForPaddingUp=Label(YKFrameForTitle,bg="white",text="",width=10)
    YKLabelForPaddingUp.pack()
    YKLabelForName=Label(YKFrameForTitle,bg="white",fg="black",font=YKFont,text="Bolbala Newsletter Software v1.0", padx=20, pady=20)
    YKLabelForName.pack(side=BOTTOM)
    YKLabelForPaddingDown=Label(YKFrameForTitle,bg="white",text="",width=20)
    YKLabelForPaddingDown.pack(side=BOTTOM)
    
    YKFrameForTitle.pack(side=BOTTOM)

    root.mainloop()
    
main()
