from tkinter import Tk, messagebox
import tkinter as tk
from PIL import Image, ImageTk


class TextWritingApp(Tk):

    def __init__(self,**kwargs):
        super().__init__()
        self.title("Disappearing Text Writing App")
        self.resizable(False,False)
        self.center_screen()
        self.in_principal = True
        self.timer = None
        self.time_in_minutes = 2
        self.inactivity_timer = None
        self.inactivity_limit = 5
        self.words = 0
        self.setting_menu_principal()

    def setting_menu_principal(self):
        self.frame_p = tk.Frame(self)
        self.frame_p.pack(padx=20,pady=20)
        
        self.label = tk.Label(self.frame_p,text="Text Writing App",fg="white",font=('Arial',30,'bold'))
        self.label.pack(pady=5)

        self.label_2 = tk.Label(self.frame_p,text="Don't stop writing, or all progress will be lost.", font=('Arial',20,'normal'))
        self.label_2.pack(pady=5)

        self.frame_image = tk.Frame(self,highlightthickness=0)
        self.frame_image.pack(padx=20,pady=15)

        image1 = Image.open("/Users/gerardoherreragomez/Desktop/OnlyPython/PythonProyectos/DISAPPEARING TEXT WRITING APP/images/writing-image.jpg").resize((300,300))
        test = ImageTk.PhotoImage(image1)
        self.label_image = tk.Label(self.frame_image,image=test)
        self.label_image.image = test
        self.label_image.pack(pady=15)        

        self.button_start = tk.Button(self.frame_image,text="Start Test",width=8,highlightthickness=0,command=self.change_game_board)
        self.button_start.pack(pady=10)

    def change_game_board(self):
        if self.in_principal:
            self.forget_settings()
            self.text_area = tk.Text(self.frame_p,height=10,width=50,font=("Helmetica",16))
            self.text_area.pack(pady=20)

            self.time_label = tk.Label(self,text="The clock starts when you start writing 🥸",font=("Arial",18,"bold"))
            self.time_label.pack(pady=15)
            
            self.word_label = tk.Label(self,text=f"Words:  {self.words}",font=("Arial",16,"bold"))
            self.word_label.pack(pady=15)

            self.not_start = True
            self.text_area.bind("<Key>",self.on_key_press)
            
    def on_key_press(self,event=None):
        self.writing_(event)
        self.calcule_words()
    
    def writing_(self,event):
        if event.char.isprintable() and not event.char.isspace() and event.char != '':
            self.reset_inactivity_timer()
            self.start_clock(self.not_start)
            
    def calcule_words(self,event=None):

        text_content = self.text_area.get('1.0',tk.END).strip().split()
        if text_content != '':
            self.words = len(text_content)
        else:
            self.words = 0
        
        self.word_label.config(text=f"Words: {self.words}")


    def start_clock(self,state):
        if state is True:
            self.not_start = False
            real_time = self.time_in_minutes * 60
            self.countdown(real_time)

    def countdown(self,count_sec):
        self.time_label.config(text=f"Time Left ⏰:  {count_sec}")
        if count_sec > 0:
            self.timer = self.after(1000,self.countdown,count_sec-1)
        else:
            self.game_over("Time's up","No seconds left.")

    def reset_inactivity_timer(self):
        if self.inactivity_timer is not None:
            self.after_cancel(self.inactivity_timer)

        self.inactivity_timer =  self.after(self.inactivity_limit*1000,self.inactivity_game_over)

    def inactivity_game_over(self):
        self.game_over("Gamve Over","You stopped writing for too long!")

    def game_over(self,title,message):
        if self.timer is not None:
            self.after_cancel(self.timer)

        if self.inactivity_timer is not None:
            self.after_cancel(self.inactivity_timer)

        tk.messagebox.showinfo(title=title, message=message)
        self.quit()

    def forget_settings(self):
        self.label.pack_forget()
        self.label_2.pack_forget()
        self.frame_image.pack_forget()
        self.label_image.pack_forget()

    def center_screen(self):

        self.window_height = 600
        self.window_width = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (self.window_width/2))
        y_cordinate = int((screen_height/2) - (self.window_height/2))
        
        self.geometry("{}x{}+{}+{}".format(self.window_width,self.window_height, x_cordinate, y_cordinate))

