# -*- coding: utf-8 -*-
"""
Created on Oct 2022

@author: Nikhtih
"""

import tkinter as tk
from tkinter import *
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox

window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
#window.title("Face_Recogniser")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)
 
window.geometry('720x720')
window.configure(background='#ffffff')
window.wm_title('EXOVISION - ATTENDANCE CAPTURE SYSTEM')
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

#path = "profile.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#panel = tk.Label(window, image = img)


#panel.pack(side = "left", fill = "y", expand = "no")

#cv_img = cv2.imread("img541.jpg")
#x, y, no_channels = cv_img.shape
#canvas = tk.Canvas(window, width = x, height =y)
#canvas.pack(side="left")
#photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img)) 
# Add a PhotoImage to the Canvas
#canvas.create_image(0, 0, image=photo, anchor=tk.NW)

#msg = Message(window, text='Hello, world!')

# Font is a tuple of (font_family, size_in_points, style_modifier_string)



#Declaring objects for all the resources (Icon images)

p1 = PhotoImage(file = f"windowIcon.png")
openPicture = ImageTk.PhotoImage(Image.open("openUEL.png"))
logoBefore = ImageTk.PhotoImage(Image.open("logo.png"))
logoAfter = ImageTk.PhotoImage(Image.open("logoIn.png"))
take = PhotoImage(file = f"takeImage.png")
track = PhotoImage(file = f"trackImage.png")
train = PhotoImage(file = f"trainImage.png")
openImage = PhotoImage(file = f"open.png")
loginImage = PhotoImage(file = f"loginButton.png")
backImage = PhotoImage(file = f"back.png")
clearImage = PhotoImage(file = f"clear.png")
quitImage = PhotoImage(file = f"quit.png")
u_id_image = PhotoImage(file = f"UserId.png")
u_name_image = PhotoImage(file = f"UserName.png")
attendance = PhotoImage(file = f"AttendanceButton.png")

#Window Icon
window.iconphoto(False, p1)

#Creating object for canvas
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 759,
    width = 708,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


Id = 0
name = ""

#Creating First Page (cavas)
canvas.create_image(210, 120, anchor=NW, image=openPicture)


#Input Field Object Declaration
txt = Entry(window,
        bd = 0,
        bg = "#ffffff",
        foreground = "#a9a9a9",
        font = "times 20",
        highlightthickness = 0)
txt2 = Entry(
        bd = 0,
        bg = "#ffffff",
        foreground = "#a9a9a9",
        font = "times 20",
        highlightthickness = 0)

txt3 = Entry(window,
        bd = 0,
        bg = "#ffffff",
        foreground = "#a9a9a9",
        font = "times 20",
        highlightthickness = 0)
txt4 = Entry(
        bd = 0,
        bg = "#ffffff",
        foreground = "#a9a9a9",
        font = "times 20",
        highlightthickness = 0)


#Output Field Object Declaration
lbl3 = tk.Label(text="Notification",width=20 ,height=2,bg="white" ,font=("Lato-Regular", int(20.0), 'bold')) 
message = Label(
        window,
        bd = 0,
        bg = "#C0BBBB",
        fg="white",
        borderwidth=3, relief="sunken",
        font=('times', 15, ' bold '),
        highlightthickness = 0)
lbl4 = tk.Label(text="Attendance",width=20 ,height=2,bg="white" ,font=("Lato-Regular", int(20.0), 'bold'))
message2 = Label(
        bd = 0,
        bg = "#C0BBBB",
        fg="black",
        borderwidth=3, relief="sunken",
        highlightthickness = 0)




#Window Quit Button
quitButton = Button(
    image = quitImage,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat",
    command=window.destroy)

quitButton.place(
    x = 370, y = 576,
    width = 228,
    height = 50)



##Old Code
#message = tk.Label(window, text="Face-Recognition-Based-Attendance-Management-System" ,bg="pink"  ,fg="white"  ,width=65  ,height=3,font=('times', 20, 'italic bold')) 

#message.place(x=100, y=20)

#lbl = tk.Label(window, text="Enter ID",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
#lbl.place(x=200, y=200)

#txt = tk.Entry(window,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
#txt.place(x=500, y=215)

#lbl2 = tk.Label(window, text="Enter Name",width=20  ,fg="red"  ,bg="yellow"    ,height=2 ,font=('times', 15, ' bold ')) 
#lbl2.place(x=200, y=300)

#txt2 = tk.Entry(window,width=20  ,bg="yellow"  ,fg="red",font=('times', 15, ' bold ')  )
#txt2.place(x=500, y=315)

#lbl3 = tk.Label(window, text="Notification : ",width=20  ,fg="red"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold underline ')) 
#lbl3.place(x=200, y=400)

#message = tk.Label(window, text="" ,bg="yellow"  ,fg="red"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
#message.place(x=500, y=400)

#lbl3 = tk.Label(window, text="Attendance : ",width=20  ,fg="red"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold  underline')) 
#lbl3.place(x=200, y=600)


#message2 = tk.Label(window, text="" ,fg="red"   ,bg="yellow",activeforeground = "green",width=30  ,height=2  ,font=('times', 15, ' bold ')) 
#message2.place(x=450, y=600)
 
#Code For Clear Button
def clear():
    txt.delete(0, 'end')
    txt2.delete(0, 'end')

#For Creating Round Rectangle
def round_rectangle(x1, y1, x2, y2, r=25, **kwargs):    
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    return canvas.create_polygon(points, **kwargs, smooth=True)

#def clear2():
    #txt2.delete(0, 'end')    
    #res = ""
    #message.configure(text= res)    

#For Validating whether the entered Id is number or not    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False


#Code for Second Page where User Id and UserName is entered
def open_button_click():
    canvas.delete("all")
    openButton['image']= loginImage
    if(openButton['text'] == "login"):
        login_button_click()
    elif(openButton['text'] == "back"):
        openButton['text'] = "login"
        canvas.create_image(225, 20, anchor=NW, image=logoBefore)
        round_rectangle(
        164, 140, 164+380, 140+400,25,
        fill = "#000000",
        outline = "")

        u_id_bg = canvas.create_image(
            354.0, 355.0,
            image = u_id_image)
        print(Id)
        print(name)
        txt.insert(0, Id)
        #txt.bind("<FocusIn>", lambda args: txt.delete('0', 'end'))
        txt.place(
            x = 214.0, y = 330,
            width = 280.0,
            height = 48)

        
        u_name_bg = canvas.create_image(
            354.0, 425.0,
            image = u_name_image)
        txt2.insert(0, name)
        #txt2.bind("<FocusIn>", lambda args: txt2.delete('0', 'end'))
        txt2.place(
            x = 214.0, y = 400,
            width = 280.0,
            height = 48)
    else:
        openButton['text'] = "login"       
        canvas.create_image(225, 20, anchor=NW, image=logoBefore)
        round_rectangle(
        164, 140, 164+380, 140+400,25,
        fill = "#000000",
        outline = "")

        canvas.create_text(
            354.5, 235.0,
            text = "ACS",
            fill = "#ffffff",
            font = ("Amiri-Bold", int(34.0)))

        u_id_bg = canvas.create_image(
            354.0, 355.0,
            image = u_id_image)
        
        txt.insert(0, 'User Id')
        txt.bind("<FocusIn>", lambda args: txt.delete('0', 'end'))
        txt.place(
            x = 214.0, y = 330,
            width = 280.0,
            height = 48)

        
        u_name_bg = canvas.create_image(
            354.0, 425.0,
            image = u_name_image)
        txt2.insert(0, 'User Name')
        txt2.bind("<FocusIn>", lambda args: txt2.delete('0', 'end'))
        txt2.place(
            x = 214.0, y = 400,
            width = 280.0,
            height = 48)

#Code for Universal Open Button
openButton = Button(
    image = openImage,
    text = "open",
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat",
    command = open_button_click)
openButton.place(
        x = 130, y = 576,
        width = 228,
        height = 50)

#Code for Login Button ( Basically Validation Code )
def login_button_click():
    Id=(txt.get())
    name=(txt2.get())
    if(Id=='User Id' or name=='User Name'):
        openButton['text'] = "open"
        txt.delete('0', 'end')
        txt2.delete('0', 'end')
        open_button_click()
        tkinter.messagebox.showerror("Error", "Please enter both user id and password")
        return
    elif(is_number(Id)==False):
        openButton['text'] = "open"
        txt.delete('0', 'end')
        txt2.delete('0', 'end')
        open_button_click()
        tkinter.messagebox.showerror("Error", "Please enter only numbers in user id")
        return
    elif(len(Id)>7):
        openButton['text'] = "open"
        txt.delete('0', 'end')
        txt2.delete('0', 'end')
        open_button_click()
        tkinter.messagebox.showerror("Error", "The user id should not exceed 7 characters")
    else:
        Id=(txt.get())
        name=(txt2.get())
        txt3.insert(0, Id)
        txt4.insert(0, name)
        print(Id)
        print(name)
        txt.delete('0','end')
        txt2.delete('0','end')
        track_page()

def track_page():
    canvas.delete("all")
    canvas.create_image(200, 20, anchor=NW, image=logoAfter)
    openButton['state']= 'disable'
    attendanceButton['state']= 'disable'
    txt['foreground']='#ffffff'
    txt2['foreground']='#ffffff'
    lbl3.place(x=-5.5, y=290.5)
    message.place(
        x = 260.0, y = 301,
        width = 350.0,
        height = 50)

     
    lbl4.place(x=-30, y=405.5)
    
    message2.place(
        x = 250.0, y = 396,
        width = 403.0,
        height = 80)

    takeButton = Button(
    image = take,
    borderwidth = 0,
    highlightthickness = 0,
    command = TakeImages,
    relief = "flat")

    takeButton.place(
        x = 70, y = 160,
        width = 170,
        height = 61)
    
    trackButton = Button(
    image = track,
    borderwidth = 0,
    highlightthickness = 0,
    command = TrainImages,
    relief = "flat")

    trackButton.place(
        x = 269, y = 160,
        width = 170,
        height = 61)

    trainButton = Button(
    image = train,
    borderwidth = 0,
    highlightthickness = 0,
    command = TrackImages,
    relief = "flat")

    trainButton.place(
        x = 468, y = 160,
        width = 170,
        height = 61)


def direct_Attendance():
    canvas.delete("all")
    canvas.create_image(200, 20, anchor=NW, image=logoAfter)
    openButton['state']= 'disable'
    
    attendanceButton['state']= 'disable'      
     
    lbl4.place(x=-20, y=320.5)
    
    message2.place(
        x = 240.0, y = 300,
        width = 403.0,
        height = 100)  
    
    
    trainButton = Button(
    image = train,
    borderwidth = 0,
    highlightthickness = 0,
    command = TrackImages,
    relief = "flat")

    trainButton.place(
        x = 280, y = 200,
        width = 170,
        height = 61)

#Attendace Button
attendanceButton = Button(
    image = attendance,
    text = 'takingattendance',
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat",
    command=direct_Attendance)

attendanceButton.place(
    x = 280, y = 650,
    width = 155,
    height = 45)


def TakeImages():        
    Id=(txt3.get())
    name=(txt4.get())
    print("Id"+Id)
    print("Name"+name)
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 20
            elif sampleNum>20:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for ID : " + Id +" Name : "+ name
        row = [Id , name]
        with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)
    
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Image Trained"#+",".join(str(f) for f in Id)
    message.configure(text= res)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)    
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    #print(attendance)
    res=attendance
    message2.configure(text= res)

  
#clearButton = tk.Button(window, text="Clear", command=clear  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
#clearButton.place(x=750, y=200)
#clearButton2 = tk.Button(window, text="Clear", command=clear2  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
#clearButton2.place(x=750, y=300)    
#takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
#takeImg.place(x=50, y=500)
#trainImg = tk.Button(window, text="Train Images", command=TrainImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
#trainImg.place(x=350, y=500)
#trackImg = tk.Button(window, text="Track Images", command=TrackImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
#trackImg.place(x=650, y=500)
#quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
#quitWindow.place(x=950, y=500)
#copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,font=('times', 15, 'italic bold'))
#copyWrite.tag_configure("superscript", offset=10)
#copyWrite.insert("insert", "Developed by Ace Students")
#copyWrite.configure(state="normal",fg="red"  )
#copyWrite.pack(side="right")
#copyWrite.place(x=550, y=650)

#canvas.create_text(
    #570.5, 670.5,
    #text = "Developed by ACE students",
    #fill = "#a2cdd2",
    #font = ("AlegreyaSC-Regular", int(15.0)))

window.resizable(False, False)
window.mainloop()
