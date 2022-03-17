import tkinter as tk
from tkinter import *
import os
from tkinter import messagebox
from PIL import ImageTk , Image
import mysql.connector
import webbrowser
import tkinter.font as tkfont
from tkinter import ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
connection=mysql.connector.connect(host="localhost",user="root",passwd="pdvk2108")
cursor=connection.cursor()
cursor.execute("create database if not exists Hackathon_Hackers")
cursor.execute("use Hackathon_Hackers")




def login():
  global login
  login_screen=Toplevel()
  login_screen.maxsize(1000,750)
  login_screen.title('JOIN COMMUNITY')
  login_screen.config(bg="white")
  login_screen_img =ImageTk.PhotoImage(Image.open(r"C:\Users\VISHAL KHUMAR P.D\Downloads\Untitled22.png"))
  lb2 = Label(login_screen,image =login_screen_img)
  lb2.image =login_screen_img
  lb2.pack()
  myfont=tkfont.Font(family="sans",size=25,slant="italic")
  def login1():
    if ye.get()=='' or username_login_entry.get()=='' or password__login_entry.get()=='':
      messagebox.showerror("EMPTY FIELDS","SEVERAL DETAILS AREN'T FILLED")
    else:

      global a
      a=random.randint(100000,999999)
      fromi = 'tourismmadesimple@gmail.com'
      to = ye.get()
      your_pass = "tourism1234"

      body = "Hi!! Thanks for Joining over here!!\nNow You happy, me happy and all are happy!\nTHE OTP IS: {}".format(a)
      subject = 'COMMUNITY EMAIL'
      message = MIMEMultipart()
      message['From'] = fromi
      message['To'] = to
      message['Subject'] = subject
      message.attach(MIMEText(body, 'plain'))
      text = message.as_string()

      mail = smtplib.SMTP('smtp.gmail.com', 587)
      mail.ehlo()
      mail.starttls()
      mail.login(fromi,your_pass)
      mail.sendmail(fromi,to, text)
      mail.close()

      
      window = Tk()
      # set window title
      window.title("OTP VERIFICATION")
      # set window width and height
      window.geometry("300x200")
      text=Label(window, text="ENTER THE OTP")
      text.config(font=('Helvatical bold',20))
      text.place(x=40,y=20)

      window.configure(width=300, height=200)
      window .resizable(False, False)
      window.eval('tk::PlaceWindow . center')
      yes = Entry(window,font='20',show='*')
      yes.configure(width=10)
      yes.place(x=50,y=80,width=200,height=30)
      window.configure(bg='Red')
      
      def verify():
        if yes.get()==str(a):
          messagebox.showinfo("Showinfo", "Your OTP had been validated")
          sql="insert into Login_table1 values(%s,%s,%s)"
          values=username_login_entry.get(),ye.get(),password__login_entry.get()
          cursor.execute(sql,values)
          connection.commit()
          window.destroy()
        else:
          messagebox.showerror("Showerror","You entered the wrong OTP")
          
      btn=Button(window,text = 'VERIFY',command=verify,bd=1) 
      btn.place(x=130,y=150)
      
  Label(login_screen, text="USERNAME :",font=myfont,bd=0,bg="white").place(x=200,y=500)
  username_login_entry = Entry(login_screen, textvariable="username",bg="#F4EED3",bd=0,font=20)
  username_login_entry.configure(width=45)
  Label(login_screen, text="EMAIL :",font=myfont,bd=0,bg="white").place(x=200,y=550)
  ye = Entry(login_screen, textvariable="email",bg="#F4EED3",bd=0,font=20)
  ye.configure(width=45)
  username_login_entry.place(x=425,y=500)
  ye.place(x=425,y=550)
  Label(login_screen, text="PASSWORD :",font=myfont,bd=0,bg="white").place(x=200,y=600)
  password__login_entry = Entry(login_screen, textvariable="password", show= '*',bg="#F4EED3",bd=0,font=20)
  password__login_entry.configure(width=45)
  password__login_entry.place(x=425,y=600)
  Button(login_screen,text="SIGN UP", height=1, command=login1,width=6,bg="#AFF8DB").place(x=650 , y = 650 )

def ab():
  
  k=Tk()
  with open('about.txt', 'r', encoding='utf-8') as f:
    j=f.read()
  lbl_label=Label(k,text=j,justify=LEFT,font=['Lucida calligraphy','14'],bg='lavender')
  lbl_label.place(x=10,y=20)
  def back1():
      k.destroy()
  login_btn=Button(k,text = 'BACK',font=['arial',20],command=back1,bd=1,bg='snow') 
  login_btn.place(x=1300,y=650)
  k.title("MAIN PAGE")
  
  k.geometry('1500x1200+0+0')
  k.resizable(0,0)
  k.config(bg="deeppink")
  k.mainloop()
def login2():
  global login2
  login2_screen=Toplevel()
  login2_screen.maxsize(1000,750)
  login2_screen.title('JOIN COMMUNITY')
  login2_screen.config(bg="white")
  login2_screen_img =ImageTk.PhotoImage(Image.open(r"C:\Users\VISHAL KHUMAR P.D\Downloads\Untitled22.png"))
  lb2 = Label(login2_screen,image =login2_screen_img)
  lb2.image =login2_screen_img
  lb2.pack()
  myfont=tkfont.Font(family="sans",size=15,slant="italic")
  Label(login2_screen, text="EMAIL :",font=myfont,bd=0,bg="white").place(x=200,y=550)
  ye = Entry(login2_screen, textvariable="email",bg="#F4EED3",bd=0,font=20)
  ye.configure(width=45)
  ye.place(x=425,y=550)
  Label(login2_screen, text="PASSWORD :",font=myfont,bd=0,bg="white").place(x=200,y=600)
  password__login_entry = Entry(login2_screen, textvariable="password", show= '*',bg="#F4EED3",bd=0,font=20)
  password__login_entry.configure(width=45)
  password__login_entry.place(x=425,y=600)
  def dear():
    if password__login_entry.get()=='' or ye.get()=='':
      messagebox.showinfo("INFORMATION", "PLEASE ENTER THE REQUIRED DETAILS")
    else:
      sqlite_select_query = """SELECT * from Login_table1"""
      cursor.execute(sqlite_select_query)
      a = cursor.fetchall()
      Output = [item for item in a
          if item[1] == ye.get() and item[2] ==password__login_entry.get() ]
      if Output==[]:
        messagebox.showinfo("INFORMATION","THE ACCOUNT WITH THESE DETAILS DOSEN'T EXIST")
      else:
        def city_screen():
        
          global city_screen
        city_screen=Toplevel()
        city_screen.geometry('1200x750')
        city_screen.config(bg = "white" )
        city_screen_img = ImageTk.PhotoImage(file=r"C:\Users\VISHAL KHUMAR P.D\Downloads\image.png")
        lo=Label(city_screen)
        lo.place(x=0,y=0)
        lo.config(image=city_screen_img)

        
        city_screen.title("HACKATHON HACKERS")

        def chennai():
          root = Toplevel()
          #background color
          color='#21252b'
          root.configure(background = color)
          root.geometry('1200x1200')

          #Notebook color
          sky_color = "sky blue"
          gold_color = "gold"
          color_tab = "#ccdee0"
          #style
          style = ttk.Style()
          style.theme_create( "beautiful", parent = "alt", settings ={
                  "TNotebook": {
                      "configure": {"tabmargins": [10, 10, 20, 10], "background":sky_color }},
                  "TNotebook.Tab": {
                      "configure": {"padding": [30, 15], "background": sky_color, "font":('consolas italic', 14), "borderwidth":[0]},
                      "map":       {"background": [("selected", gold_color), ('!active', sky_color), ('active', color_tab)],
                                    "expand": [("selected", [1, 1, 1, 0])]}}})
          style.theme_use("beautiful")
          style.layout("Tab",
                              [('Notebook.tab', {'sticky': 'nswe', 'children':
                                  [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                                      #[('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                                          [('Notebook.label', {'side': 'top', 'sticky': ''})],
                                      #})],
                                  })],
                              })]
                           )
          style.configure('TLabel', background = color , foreground = 'white')
          style.configure('TFrame', background = color)
          #frame
          frame_main_notebook = ttk.Frame(root, width = 200, height = 100)
          frame_main_notebook.pack(side = LEFT , expand = 2, fill = 'both')
          frame_main_notebook.pack()
          #note book
          main_notebook = ttk.Notebook(frame_main_notebook, width = 500, height = 500)
          main_notebook.pack(side = LEFT , expand = 2, fill = 'both')
          #first tab
          frame_one = ttk.Frame(main_notebook, width = 200, height = 100)
          frame_one.pack(side = RIGHT)
          main_notebook.add(frame_one, text = 'PLACES TO VISIT')
          image1=ImageTk.PhotoImage(file=r"C:\Users\VISHAL KHUMAR P.D\Downloads\chennai.jpg")
          l=Label(frame_one)
          l.place(x=20,y=150)
          l.config(image=image1)
          image2=ImageTk.PhotoImage(file=r"C:\Users\VISHAL KHUMAR P.D\Downloads\san.jpg")
          l=Label(frame_one)
          l.place(x=1000,y=150)
          l.config(image=image2)
          image3=ImageTk.PhotoImage(file=r"C:\Users\VISHAL KHUMAR P.D\Downloads\beach.jpg")
          l=Label(frame_one)
          l.place(x=460,y=150)
          l.config(image=image3)
          t=ttk.Label(frame_one, text ='1)San Thome Cathedral Basilica\n   San Thome Church, is known as St. Thomas Cathedral Basilica and National Shrine of Saint Thomas, is a Roman Catholic minor \n basilica in the Santhome neighbourhood of the city of Madras, in Tamil Nadu, India. The present structure dates to 1523 AD, \n when it was built by the Portuguese, over the tomb of Thomas the Apostle, one of the apostles of Jesus.\n In 1896, it was rebuilt in British Madras according to Neo-Gothic style, as was favoured by British architects in the late 19th century.\n This church is one of the three known churches in the world built over the tomb of an apostle of Jesus that are still standing today.',width = 200,font=20).pack() 
          #second tab
          frame_two = ttk.Frame(main_notebook, width = 200, height = 100)
          ima=ImageTk.PhotoImage(file=r"C:\Users\VISHAL KHUMAR P.D\Downloads\marina.jpg")
          l=Label(frame_two)
          l.place(x=460,y=150)
          l.config(image=ima)
          imaf=ImageTk.PhotoImage(file=r"C:\Users\VISHAL KHUMAR P.D\Downloads\sundal.jpg")
          l=Label(frame_two)
          l.place(x=460,y=400)
          l.config(image=imaf)
          frame_two.pack(side = TOP)
          ttk.Label(frame_two, text = '1) STREET FOOD \n A very popular and tasty street food in Chennai, Sundal is found at many beaches. However, the ones found at Marina Beach \n are considered to be the best. Sundal is made from boiled chickpeas mixed with onions, an assortment of spices, herbs, \n and topped off with shredded coconut. It is an exotic street food worthy of the \n exotic city.',width = 200,font=20).pack()
          main_notebook.add(frame_two, text = '   FOODS TO TRY   ')
          #third tab
          frame_two = ttk.Frame(main_notebook, width = 200, height = 100)
          frame_two.pack(side = TOP)
          imafi=ImageTk.PhotoImage(file=r"C:\Users\VISHAL KHUMAR P.D\Downloads\amanoj.jpg")
          l=Label(frame_two)
          l.place(x=460,y=300)
          l.config(image=imafi)
 
          l=ttk.Label(frame_two, text = 'Thinking Out Loud by Manoj Prabakar. \n After his first successful solo show tour, `I TRIED`, across the country. \n Manoj Prabakar is back on road with his new English standup solo show, `THINKING OUT LOUD`. \n This show is a compilation of all the funny thoughts that he got in the past one year, where \n he will be talking about himself and his life observations in general.\n So come watch him tell his funny thoughts out loud at SoCo :D',width = 200,font=20).pack()

          main_notebook.add(frame_two, text = '    UPCOMING EVENTS ')
          root.mainloop()
                    
          
        
        chennai_button=ImageTk.PhotoImage(Image.open(r"C:\Users\VISHAL KHUMAR P.D\Downloads\20220316_083453_0000.png"))
        Button(city_screen,image = chennai_button, height=150, width=150,bd=2,compound="left",bg="white",command=chennai).place(x=225, y = 500)

        def jaipur():
          
          root = Toplevel()
          #background color
          color='#21252b'
          root.configure(background = color)
          root.geometry('1200x1200')

          #Notebook color
          sky_color = "sky blue"
          gold_color = "gold"
          color_tab = "#ccdee0"
          #style
          style = ttk.Style()
          style.theme_create( "ale_themes", parent = "alt", settings ={
                  "TNotebook": {
                      "configure": {"tabmargins": [10, 10, 20, 10], "background":sky_color }},
                  "TNotebook.Tab": {
                      "configure": {"padding": [30, 15], "background": sky_color, "font":('consolas italic', 14), "borderwidth":[0]},
                      "map":       {"background": [("selected", gold_color), ('!active', sky_color), ('active', color_tab)],
                                    "expand": [("selected", [1, 1, 1, 0])]}}})
          style.theme_use("ale_themes")
          style.layout("Tab",
                              [('Notebook.tab', {'sticky': 'nswe', 'children':
                                  [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                                      #[('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                                          [('Notebook.label', {'side': 'top', 'sticky': ''})],
                                      #})],
                                  })],
                              })]
                           )
          style.configure('TLabel', background = color , foreground = 'white')
          style.configure('TFrame', background = color)
          #frame
          frame_main_notebook = ttk.Frame(root, width = 200, height = 100)
          frame_main_notebook.pack(side = LEFT , expand = 2, fill = 'both')
          frame_main_notebook.pack()
          #note book
          main_notebook = ttk.Notebook(frame_main_notebook, width = 500, height = 500)
          main_notebook.pack(side = LEFT , expand = 2, fill = 'both')
          #first tab
          frame_one = ttk.Frame(main_notebook, width = 200, height = 100)
          frame_one.pack(side = RIGHT)
          image4=ImageTk.PhotoImage(file=r"C:\Users\VISHAL KHUMAR P.D\Downloads\hawa.jpg")
          l=Label(frame_one)
          l.place(x=600,y=400)
          l.config(image=image4)
          main_notebook.add(frame_one, text = 'PLACES TO VISIT')
          t=ttk.Label(frame_one, text ='Hawa Mahal\nBuilt from red and pink sandstone, the palace sits on the edge of the City Palace,\n Jaipur, and extends to the Zenana, or women chambers. \nThe structure was built in 1799 by the Maharaja Sawai Pratap Singh, \nthe grandson of Maharaja Sawai Jai Singh, who was the founder of the city of Jaipur, India. \nHe was so inspired by the unique structure the of Khetri Mahal that he built this grand and historical palace. \nIt was designed by Lal Chand Ustad',width=200,font=20).pack()
          #second tab
          frame_two = ttk.Frame(main_notebook, width = 200, height = 100)
          frame_two.pack(side = TOP)
          image5=ImageTk.PhotoImage(file=r"C:\Users\VISHAL KHUMAR P.D\Downloads\thali.jpg")
          l=Label(frame_two)
          l.place(x=800,y=400)
          l.config(image=image5)
          image6=ImageTk.PhotoImage(file=r"C:\Users\VISHAL KHUMAR P.D\Downloads\las.jpg")
          l=Label(frame_two)
          l.place(x=0,y=400)
          l.config(image=image6)
          ttk.Label(frame_two, text = 'Rajasthani Thali (Plate) at Chokhi Dhani Village Resort\n  Try out authentic Rajasthani food with tons of ghee\n (added for that authentic flavour) at Chokhi Dhani Village Resort. \n You will find daal (lentil curry), Bati (baked round bread topped with a dollop of ghee), \n Churma (dessert), Kheer & Sangri (fried version of dried veggie), \n Gatte ki sabzi (curry) and all typical Rajasthani dishes and the fun of food get doubled here with village ambience,\n the local artist performing folk dances, camel rides, and other entertaining activities.\n Thus all these fun ingredients form win-win situation for explorers \n with famous foods in Jaipur.\n\n\n Laal Maans at Handi\n   Lassi is the famous street food in Jaipur and it is the \n Indian style yoghurt beverage made by beating yoghurt and dress up with extra cream served with so much affection in Kulhads (earthen glasses) by one and only Lassiwala at Mirza Ismael, Road. Better grab your Kulhad full of lassi to boost your energies to explore high spirits of Jaipur.',width=200,font=20).pack()
          main_notebook.add(frame_two, text = '   FOODS TO TRY   ')
          #third tab
          frame_two1 = ttk.Frame(main_notebook, width = 200, height = 100)
          frame_two1.pack(side = TOP)
          imag81=ImageTk.PhotoImage(file=r"C:\Users\VISHAL KHUMAR P.D\Downloads\bhav.jpg")
          l=Label(frame_two1)
          l.place(x=100,y=100)
          l.config(image=imag81)

          ttk.Label(frame_two1, text = '(9 APRIL) - Dhvani Bhanushali Live in Jaipur\n  SteppinOut by Dineout presents Indian’s Pop Sensation - Dhvani Bhanushali\n with her first-ever India Tour. The singer will be embarking on ten \n cities during the tour and promises to entertain the audience \n with her melodious voice.\n\nDhvani Bhanushali broke the internet with her songs right from the beginning of her music career.\n Starting with Vaaste, that released in April 2019, went on to become a massive \n success and was the only Indian non-film song that got featured in the YouTube Top 200 Global list\n. Dhvani’s songs like Leja Re, Ishare Tere, Baby Girl, Nayan, Radha went on to \n become a rage among the youngsters and she was soon named the Billionaire Baby. \n While Leja Re garnered more than 860 million views, both her songs Dilbar and Vaaste \n have crossed more than 1 billion views individually on YouTube. \n\nThe young singer who has 6.2 million followers on her Instagram recently released Mehendi \n and Mera Yaar has shown her versatility as a singer. Dhvani received \n massive love from her fans for both the through social media platforms \n like reels, short video platform apps, etc. \n The singer is all set to release her next single soon.\n So get ready to dance, groove & sing along. Get your tickets now.',width=200,font=20).pack()
          

          main_notebook.add(frame_two1, text = '    UPCOMING EVENTS ')
          root.mainloop()

        jaipur_button=ImageTk.PhotoImage(Image.open(r"C:\Users\VISHAL KHUMAR P.D\Downloads\20220316_083638_0000.png"))
        Button(city_screen,image = jaipur_button, height=150, width=150,bd=2,compound="left",command=jaipur,bg="white").place(x=400, y = 500)
        def mumbai():
          webbrowser.open('https://docs.google.com/document/d/1RhLzvLdfc2EnekVeyA_vVdZNKnCW3xa5Q0KcA8pYGYk/edit')
          

        mb_button=ImageTk.PhotoImage(Image.open(r"C:\Users\VISHAL KHUMAR P.D\Downloads\20220316_083415_0000.png"))
        Button(city_screen,image = mb_button, height=150, width=150,bd=2,compound="left",bg="white",command=mumbai).place(x=575 , y = 500)

        def goa():
          webbrowser.open('https://docs.google.com/document/d/1F0TCBLXnkIBgdwJZ4nLQvyLsDmlp4mHIxgMaBg1gGlw/edit')

        goa_button=ImageTk.PhotoImage(Image.open(r"C:\Users\VISHAL KHUMAR P.D\Downloads\20220316_083332_0000.png"))
        Button(city_screen,image = goa_button, height=150, width=150,bd=2,compound="left",bg="white",command=goa).place(x=750, y = 500)
      city_screen.mainloop()
        

       
    
  login_btnnnn=Button(login2_screen,text = 'SIGN IN',font=['arial',10],command=dear,bd=1,bg='snow')
  login_btnnnn.place(x=600,y=700)
    
def main_screen():
 global main_screen

main_screen=Tk()
main_screen.geometry('1200x750')
main_screen.config(bg = "white" )
main_screen.title("HACKATHON HACKERS")
main_screen_img = ImageTk.PhotoImage(Image.open(r"C:\Users\VISHAL KHUMAR P.D\Downloads\Picsart_22-03-12_13-42-59-103-02.jpeg"))
Label(text="",image = main_screen_img).pack()
logo_screen_img =ImageTk.PhotoImage(Image.open(r"C:\Users\VISHAL KHUMAR P.D\Downloads\IMG_09032022_124353_(300_x_200_pixel).png"))
lg = Label(main_screen,image =logo_screen_img,height=200, width=300,bd=0)
lg.image =logo_screen_img
lg.place(x=25 , y = 100)
abt_button=ImageTk.PhotoImage(Image.open(r"C:\Users\VISHAL KHUMAR P.D\Downloads\IMG_09032022_115714_(150_x_40_pixel).png"))
JC_button=ImageTk.PhotoImage(Image.open(r"C:\Users\VISHAL KHUMAR P.D\Downloads\magicut_1646806628965.png"))
Button(main_screen,image = JC_button, height=70, width=265,bd=0,compound="left",command=login,bg="white").place(x=25 , y = 400)
Button(main_screen,image = abt_button, height=25, width=120,bd=0,compound="left",command=ab,bg="white").place(x=85 , y = 500)
Button(main_screen,text="Already a member,LOGIN", command=login2,height=2,width=30,bg="white",bd=0,fg="#5D929E",).place(x=45 , y = 550)
main_screen.mainloop()
