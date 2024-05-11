from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import Frame, Label
from PIL import Image, ImageTk
import cv2

class OpenPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('950x600')
        self.window.title('Opening Page')
        self.window.resizable(False, False)
        self.lgn_frame = Frame(self.window, bg='#000000', width=950, height=600)
        self.lgn_frame.place(x=0, y=0)
        self.show_login_page()

    def show_login_page(self):
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#000000', width=950, height=600)
        self.lgn_frame.place(x=0, y=0)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=410, y=40)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                   font=("Butcherman", 20, "bold"))
        self.sign_in_label.place(x=425, y=160)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=330, y=250)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=360, y=285, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=330, y=309)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\userIcon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=330, y=282)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=330, y=340)  # Decreased y from 380 to 340

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=360, y=376, width=244)  # Decreased y from 416 to 376

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=330, y=400)  # Decreased y from 440 to 400

        # Password icon
        self.password_icon = Image.open('images\\lockIcon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=330, y=374)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=330, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)


        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=330, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405",
                                          command=self.open_register_page)
        self.signup_button_label.place(x=450, y=555, width=111, height=35)


        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\viewIcon.jpg')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hideIcon.jpg')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="black"
                                  , borderwidth=0, background="black", cursor="hand2")
        self.show_button.place(x=640, y=380)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="black"
                                  , borderwidth=0, background="black", cursor="hand2")
        self.hide_button.place(x=640, y=380)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="black"
                                  , borderwidth=0, background="black", cursor="hand2")
        self.show_button.place(x=640, y=380)
        self.password_entry.config(show='*')

    def show_register_page(self):
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#000000', width=950, height=600)
        self.lgn_frame.place(x=0, y=0)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=410, y=40)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign Up", bg="#040405", fg="white",
                                   font=("Butcherman", 20, "bold"))
        self.sign_in_label.place(x=425, y=160)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=330, y=220)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=360, y=255, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=330, y=279)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\userIcon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=330, y=252)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=330, y=300)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=360, y=336, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=330, y=360)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\lockIcon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=330, y=334)

        # ========================================================================
        # ============================Confirm Password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Confirm Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=330, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=360, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=330, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\lockIcon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=330, y=414)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\lockIcon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=330, y=414)

        # ========================================================================
        # ============================Register button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=330, y=450)
        self.login = Button(self.lgn_button_label, text='Register', font=("yu gothic ui", 13, "bold"), width=25,
                            bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)

        # =========== Login Page Button ==================================================
        self.sign_label = Label(self.lgn_frame, text='Login?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=330, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\btn2.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405",
                                          command=self.open_login_page)

        self.signup_button_label.place(x=450, y=555, width=111, height=35)


        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\viewIcon.jpg')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hideIcon.jpg')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="black"
                                  , borderwidth=0, background="black", cursor="hand2")

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="black"
                                  , borderwidth=0, background="black", cursor="hand2")

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="black"
                                  , borderwidth=0, background="black", cursor="hand2")
        self.show_button.place(x=640, y=380)
        self.password_entry.config(show='*')
    def clear_frame(self):
        # Destroy all widgets in the frame
        for widget in self.lgn_frame.winfo_children():
            widget.destroy()
    def open_register_page(self):
        self.clear_frame()
        self.show_register_page()

    def open_login_page(self):
        self.clear_frame()
        self.show_login_page()



def page():
    window = Tk()
    OpenPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
