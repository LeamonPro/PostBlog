from tkinter import *
from PIL import ImageTk, Image
from lxml import etree
import xml.etree.ElementTree as ET 
from os.path import exists
tree= ET.parse("index.xml")



#interface
fenetre= Tk()
fenetre.geometry('730x400')
fenetre.title('Projet XML')

#bg image
img = ImageTk.PhotoImage(Image.open("bg5.webp"))  
l=Label(fenetre,image=img)
l.place(x=0,y=0,relwidth=1,relheight=1)
l.pack()

#Recherche interface
fenetre.resizable(height=False,width=False)
Title=Label(fenetre,text="PostBlog",font=("Verdana",40,"italic bold"),fg='#fb8500')
Title.place(x='0',y='0')
fenetre.wm_attributes("-transparentcolor", 'grey')
label=Label(fenetre,text="Merci de remplir les champs vides!",font=("Andalus ",10,"italic bold"),fg='red').place(x='0',y='90')
fenetre.wm_attributes("-transparentcolor", 'grey')

#Search input
my_search=StringVar()
sea=Label(fenetre,text="Type Name or tiltle or date to search : ",font=("Arial",10,"italic bold"),fg='blue')
sea.place(x='400',y='80')
search=Entry(fenetre,textvariable=my_search)
search.place(x='400',y='100',width=250,height=50)



#Authors input
my_name=StringVar()
name=Label(fenetre,text="Authors").place(x='20',y='140')
fenetre.wm_attributes("-transparentcolor", 'grey')
name=Entry(fenetre,textvariable=my_name)
name.place(x='140',y='140')


#title input
my_title=StringVar()
title=Label(fenetre,text="Title").place(x='20',y='180')
fenetre.wm_attributes("-transparentcolor", 'grey')
title=Entry(fenetre,textvariable=my_title)
title.place(x='140',y='180')


#date input
my_date=StringVar()
date=Label(fenetre,text="Date").place(x='20',y='220')
fenetre.wm_attributes("-transparentcolor", 'grey')
date=Entry(fenetre,textvariable=my_date)
date.place(x='140',y='220')



#page number input
my_nbPage=StringVar()
nbPage=Label(fenetre,text="Pages number").place(x='20',y='260')
fenetre.wm_attributes("-transparentcolor", 'grey')
nbPage=Entry(fenetre,textvariable=my_nbPage)
nbPage.place(x='140',y='260')





#Search fn
def fn():
    l=[]
    a=''
    z=''
    res=''
    ch='Liste des articles : \n'
    ch1='Liste des auteurs : \n'
    ch2='Liste des articles :\n'
    size=len(tree.getroot())
    for i in range(size):
        for a in tree.getroot()[i]:
            l.append(a.text)
    for i in range(len(l)-1):
        k=[]
        if (l[i+1].find('/')!= -1 and l[i].lower()==my_search.get().lower()) :
            ch1=ch1+l[i-1]
            a=l[i+1]
            z=l[i+2]
        elif((my_search.get() in l[i].split(',') or my_search.get()==l[i]) and i<len(l)-3):
            ch=ch+"Titre :"+l[i+1]+'\tDate de creation :'+l[i+2]+'\tNombre de pages :'+l[i+3]+"\n"
        elif (my_search.get().find('/') != -1 and my_search.get()==l[i]) :
            ch2=ch2+"Titre :"+l[i-1]+" écrit par :"+l[i-2]+"\n"
    if(a != '' and z!=''):
        ch1=ch1+"\nDate d'ecriture :"+a+"\nNombre de pages :"+z
    
    if(len(ch1)>22):
        res=ch
    elif(len(ch2)>22) :
        res=ch2
    elif(len(ch)>21) :
        res=ch
    else :
        res='Aucune résultat'
    search.delete(0,END)
    resultat=Label(fenetre,text=res)
    resultat.place(x='400',y='170',width=200)
    
    


#Search button
bt=Button(fenetre,text='Search',command=fn,borderwidth=3)
bt.place(x='650',y='100',width=80)




#add data to xml
def ajouter():
    racine=tree.getroot()
    element1 = ET.SubElement(racine,'article')
    l=my_name.get()
    s_elem1 = ET.SubElement(element1, 'Authors')
    s_elem1.text = l
    s_elem2 = ET.SubElement(element1, 'Title') 
    s_elem3 = ET.SubElement(element1, 'Date')   
    s_elem4 = ET.SubElement(element1, 'nbPages') 
    s_elem2.text = my_title.get()
    s_elem3.text = my_date.get()
    s_elem4.text = my_nbPage.get()
    with open("index.xml","wb") as file:
            tree.write(file_or_filename=file)
    file.close()

    #clear the inputs
    nbPage.delete(0,END)
    date.delete(0,END)
    title.delete(0,END)
    name.delete(0,END)
    
    
    




#button
button=Button(fenetre,text='Submite',bg='white',fg='black',borderwidth=3,command=ajouter)
button.place(x='280',y='310')



fenetre.mainloop()
