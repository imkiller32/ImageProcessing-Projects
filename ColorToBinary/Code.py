#..Program To Convert a colored image to Binary image
#..Author : Ritesh Aggarwal
#..Concept : Thresholding
#..Complexity : O(r*c)
#..Used : Python3,OpenCv,Tkinter(GUI)
#..User Interactive : Yes
#..Github : www.github.com/imkiller32

import cv2
import PIL.Image, PIL.ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import ImageTk,Image

path = "C:\\Users\\imkiller\\Desktop\\"
imgpath = ""

root = Tk()
root.title('Convert Color To Black and White')
root.state('zoomed')
root.resizable(False,False)

text = ttk.Label(root,text = '\nChoose a image to convert to \'Binary Image\'\n')
text.config(justify = CENTER, font = ('Courier', 20, 'bold') )
text.pack()    

panedwindow = ttk.Panedwindow(root,orient = HORIZONTAL)
panedwindow.config(width=800,height=500)
panedwindow.pack(expand = FALSE)

frame1 = ttk.LabelFrame(panedwindow,text='Original',relief=SUNKEN)
frame1.config(width=200,height=400)    

frame2 = ttk.LabelFrame(panedwindow,text='Converted',relief=SUNKEN)
frame2.config(width=200,height=400)

panedwindow.add(frame1,weight=1)
panedwindow.add(frame2,weight=1)

original = ttk.Label(frame1, text = 'Image Not Available')
original.pack(padx=5,pady=5)

converted = ttk.Label(frame2, text = 'Try Convert image to view the result')
converted.config(justify = CENTER,wrap=100)
converted.pack(padx=5,pady=5)


def OPEN():
    global imgpath
    imgpath = (fd.askopenfile().name)
    timg = Image.open(imgpath)
    img = ImageTk.PhotoImage(timg)
    width, height = 400, 480

    if img.width() < 400:
        width = img.width()
    if img.height() < 480:
        height = img.height()
        
    s_img = timg.resize((width,height),Image.ANTIALIAS)
    s_img = ImageTk.PhotoImage(s_img)
    original.config(image = s_img)
    original.img=s_img

def CONVERT():
    if(imgpath == ""):
        messagebox.showinfo(title = 'Error', message = 'Please Choose an Image First')
        return
    global cimg
    cimg = cv2.imread(imgpath,0)
    r,c = cimg.shape
    mod = r*c
    sum = 0
    for i in range(r):
        for j in range(c):
            sum=(sum+cimg[i][j])
    threshold = sum//(mod)
    for i in range(r):
        for j in range(c):
            if(cimg[i][j]>threshold):
                cimg[i][j]=255
            else:
                cimg[i][j]=0
    nimg = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(cimg))
    timg = Image.fromarray(cimg)
    width, height = 400, 480
    
    if nimg.width() < 400:
        width = nimg.width()
    if nimg.height() < 480:
        height = nimg.height()

    
    s_img = timg.resize((width,height),Image.ANTIALIAS)
    s_img = ImageTk.PhotoImage(s_img)
    
    converted.config(image = s_img)
    converted.img=s_img
    save.config(state = '!disabled')

def SAVE():
    options={}
    options['initialdir']="C:\\Users\\imkiller\\Desktop\\"
    options['title']='Save Converted Image'
    options['defaultextension']='.jpg'
    options['filetypes']=[('all files','.*')]
    path = ""
    try:
        path = (fd.asksaveasfile(**options).name)
        cv2.imwrite(path,cimg)
        messagebox.showinfo(title = 'Success', message = 'Image Saved at '+path)
    except:
        messagebox.showinfo(title = 'Error', message = 'Select a File')
    

def CLOSE():
    res = False
    res=messagebox.askyesno(title = 'Exit?', message = 'Do you want exit?')
    if(res):
        root.withdraw()

choose_button = ttk.Button(root, text = 'Open')
choose_button.pack(padx = 5, pady = 5)
choose_button.config(command = OPEN)

convert = ttk.Button(root,text = 'Convert')
convert.pack(padx = 5, pady = 5)
convert.config(command = CONVERT)

save = ttk.Button(root,text = 'Save')
save.pack(padx = 5,pady = 5)
save.config(command = SAVE)
save.config(state='disabled')

close = ttk.Button(root,text = 'Exit')
close.pack(padx = 5, pady = 5)
close.config(command = CLOSE)

root.mainloop()
