import tkinter
from tkinter import filedialog

import customtkinter
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Home")
        self.geometry("900x500")
        Font = customtkinter.CTkFont(family="Georgia", size=40, weight="bold")
        customtkinter.set_default_color_theme("green")
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Assets")
        # self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
        #                                          dark_image=Image.open(os.path.join(image_path, "home_light.png")),
        #                                          size=(20, 20))
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),
                                                 size=(26, 26))

        # --> Begin of navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Home page",
                                                             image=self.logo_image, compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
        self.firstButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Ceaser",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.logo_image, anchor="w",
                                                   command=self.firstFrame_button_event)
        self.firstButton.grid(row=1, column=0, sticky="ew", pady=5)
        self.secondButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="Second way",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),

                                                    image=self.logo_image, anchor="w",
                                                    command=self.secondFrame_button_event)

        self.secondButton.grid(row=1, column=1, sticky="ew", pady=5)
        self.thirdButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="third way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),

                                                   image=self.logo_image, anchor="w",
                                                   command=self.thirdFrame_button_event)

        self.thirdButton.grid(row=2, column=0, sticky="ew", pady=5)
        self.fourthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="fourth way",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),

                                                    image=self.logo_image, anchor="w",
                                                    command=self.fourthFrame_button_event)

        self.fourthButton.grid(row=2, column=1, sticky="ew", pady=5)
        self.fifthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="third way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),

                                                   image=self.logo_image, anchor="w",
                                                   command=self.fifthFrame_button_event)

        self.fifthButton.grid(row=3, column=0, sticky="ew", pady=5)
        self.sixthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="third way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),

                                                   image=self.logo_image, anchor="w",
                                                   command=self.sixthFrame_button_event)

        self.sixthButton.grid(row=3, column=1, sticky="ew", pady=5)
        self.sevenButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="third way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),

                                                   image=self.logo_image, anchor="w",
                                                   command=self.seventhFrame_button_event)
        self.sevenButton.grid(row=4, column=0, sticky="ew", pady=5)
        self.eightButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="third way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.logo_image, anchor="w",
                                                   command=self.eighthFrame_button_event)
        self.eightButton.grid(row=4, column=1, sticky="ew", pady=5)
        self.nineButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                  border_spacing=10,
                                                  text="third way",
                                                  fg_color="transparent", text_color=("gray10", "gray90"),
                                                  hover_color=("gray70", "gray30"),
                                                  image=self.logo_image, anchor="w",
                                                  command=self.ninthFrame_button_event)
        self.nineButton.grid(row=5, column=0, sticky="ew", pady=5)
        self.tenButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                 border_spacing=10,
                                                 text="third way",
                                                 fg_color="transparent", text_color=("gray10", "gray90"),
                                                 hover_color=("gray70", "gray30"),
                                                 image=self.logo_image, anchor="w",
                                                 command=self.tenthFrame_button_event)
        self.tenButton.grid(row=5, column=1, sticky="ew", pady=5)
        self.elevenButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="third way",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    image=self.logo_image, anchor="w",
                                                    command=self.eleventhFrame_button_event)

        self.elevenButton.grid(row=6, column=0, sticky="ew", pady=5)
        self.twelveButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="third way",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                   
                                                    image=self.logo_image, anchor="w" , command=self.twelvethFrame_button_event)

        self.twelveButton.grid(row=6, column=1, sticky="ew", pady=5)
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=0, pady=10, sticky="n", columnspan=2)
        # ================> end of navigation <=================
        # ================> Frames Creation <===================
        self.firstFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.secondFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.thirdFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fifthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sixthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.seventhFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.eighthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.ninthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.tenthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.eleventhFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.twelvethFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")


        self.create_gui_elements(self.firstFrame, "Ceaser")
        self.create_gui_elements(self.secondFrame, "second way")
        self.create_gui_elements(self.thirdFrame, "thirdFrame way")
        self.create_gui_elements(self.fourthFrame, "fourthFrame way")
        self.create_gui_elements(self.fifthFrame, "fifthFrame way")
        self.create_gui_elements(self.sixthFrame, "sixthFrame way")
        self.create_gui_elements(self.seventhFrame, "seventh way")
        self.create_gui_elements(self.eighthFrame, "eighth way")
        self.create_gui_elements(self.ninthFrame, "ninth way")
        self.create_gui_elements(self.tenthFrame, "tenth way")
        self.create_gui_elements(self.eleventhFrame, "eleventh way")
        self.create_gui_elements(self.twelvethFrame, "twelveth way")

#==============> Edit process button name
        self.bind_update_process_button_text(self.firstFrame)
        self.bind_update_process_button_text(self.secondFrame)
        self.bind_update_process_button_text(self.thirdFrame)
        self.bind_update_process_button_text(self.fourthFrame)
        self.bind_update_process_button_text(self.fifthFrame)
        self.bind_update_process_button_text(self.sixthFrame)
        self.bind_update_process_button_text(self.seventhFrame)
        self.bind_update_process_button_text(self.eighthFrame)
        self.bind_update_process_button_text(self.ninthFrame)
        self.bind_update_process_button_text(self.tenthFrame)
        self.bind_update_process_button_text(self.eleventhFrame)
        self.bind_update_process_button_text(self.twelvethFrame)
#================================================================>>
        self.firstFrame.processButton.configure(command=self.firstFrameprocess_button_click)

        #Select first frame as a default ============================================

        self.select_frame_by_name("firstFrame")
        # ==> Functions

    def firstFrameprocess_button_click(self):
        # Get the ciphertext and key from the input fields
        PTxt = self.firstFrame.encryptTextBox.get()
        K = self.firstFrame.keyTextBox.get()
        CTxt = self.firstFrame.decryptTextBox.get()
        rVar = self.firstFrame.radioVar.get()
        # Perform decryption
        if rVar == 0 :
             decryptedText = self.CeaserEncryption(PTxt, int(K))
             self.firstFrame.decryptTextBox.insert("end", decryptedText)
        else :
            encryptedText = self.CeaserDecryption(CTxt, int(K))
            self.firstFrame.encryptTextBox.insert("end", encryptedText)

    def bind_update_process_button_text(self, frame):
            frame.radioVar.trace("w", lambda *args, f=frame: self.update_process_button_text(f))

    def CeaserEncryption(self,plaintext,n):
        ans = ""
        for i in range(len(plaintext)):
            ch = plaintext[i]
            if ch == " ":
                ans += " "
            elif (ch.isupper()):
                ans += chr((ord(ch) + n - 65) % 26 + 65)
            else:
                ans += chr((ord(ch) + n - 97) % 26 + 97)
        self.firstFrame.decryptTextBox.delete(0, "end")
        return ans
    def CeaserDecryption(self,plaintext,n):
        ans = ""
        for i in range(len(plaintext)):
            ch = plaintext[i]
            if ch == " ":
                ans += " "
            elif (ch.isupper()):
                ans += chr((ord(ch) + n - 65) % 26 + 65)
            else:
                ans += chr((ord(ch) + n - 97) % 26 + 97)
        self.firstFrame.encryptTextBox.delete(0, "end")
        return ans
    def update_process_button_text(self, frame):
            # Get the value of the variable to determine which radio button is selected
            selected_value = frame.radioVar.get()

            if selected_value == 0:  # Encryption
                frame.processButton.configure(text="Encrypt")


            else:  # Decryption
                frame.processButton.configure(text="Decrypt")


    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # ________________________________________




    def select_frame_by_name(self, name):
        # set button color for selected button

        self.firstButton.configure(fg_color=("gray75", "gray25") if name == "firstFrame" else "transparent")
        self.secondButton.configure(fg_color=("gray75", "gray25") if name == "secondFrame" else "transparent")
        self.thirdButton.configure(fg_color=("gray75", "gray25") if name == "thirdFrame" else "transparent")
        self.fourthButton.configure(fg_color=("gray75", "gray25") if name == "fourthFrame" else "transparent")
        self.fifthButton.configure(fg_color=("gray75", "gray25") if name == "fifthFrame" else "transparent")
        self.sixthButton.configure(fg_color=("gray75", "gray25") if name == "sixthFrame" else "transparent")
        self.sevenButton.configure(fg_color=("gray75", "gray25") if name == "seventhFrame" else "transparent")
        self.eightButton.configure(fg_color=("gray75", "gray25") if name == "eighthFrame" else "transparent")
        self.nineButton.configure(fg_color=("gray75", "gray25") if name == "ninthFrame" else "transparent")
        self.tenButton.configure(fg_color=("gray75", "gray25") if name == "tenthFrame" else "transparent")
        self.elevenButton.configure(fg_color=("gray75", "gray25") if name == "eleventhFrame" else "transparent")
        self.twelveButton.configure(fg_color=("gray75", "gray25") if name == "twelvethFrame" else "transparent")


        # show selected frame
        if name == "firstFrame":
            self.firstFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.firstFrame.grid_forget()

        if name == "secondFrame":
            self.secondFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.secondFrame.grid_forget()

        if name == "thirdFrame":
            self.thirdFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.thirdFrame.grid_forget()

        if name == "fourthFrame":
            self.fourthFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourthFrame.grid_forget()

        if name == "fifthFrame":
            self.fifthFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifthFrame.grid_forget()

        if name == "sixthFrame":
            self.sixthFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sixthFrame.grid_forget()

        if name == "seventhFrame":
            self.seventhFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.seventhFrame.grid_forget()

        if name == "eighthFrame":
            self.eighthFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.eighthFrame.grid_forget()
        if name == "ninthFrame":
            self.ninthFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.ninthFrame.grid_forget()
        if name == "tenthFrame":
            self.tenthFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.tenthFrame.grid_forget()

        if name == "eleventhFrame":
            self.eleventhFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.eleventhFrame.grid_forget()
        if name == "twelvethFrame":
            self.twelvethFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.twelvethFrame.grid_forget()

    # -----------------------------------------

    def firstFrame_button_event(self):
        self.select_frame_by_name("firstFrame")
    def secondFrame_button_event(self):
        self.select_frame_by_name("secondFrame")

    def thirdFrame_button_event(self):
        self.select_frame_by_name("thirdFrame")

    def fourthFrame_button_event(self):
        self.select_frame_by_name("fourthFrame")

    def fifthFrame_button_event(self):
        self.select_frame_by_name("fifthFrame")

    def sixthFrame_button_event(self):
        self.select_frame_by_name("sixthFrame")
    def seventhFrame_button_event(self):
        self.select_frame_by_name("seventhFrame")
    def eighthFrame_button_event(self):
        self.select_frame_by_name("eighthFrame")
    def ninthFrame_button_event(self):
        self.select_frame_by_name("ninthFrame")
    def tenthFrame_button_event(self):
        self.select_frame_by_name("tenthFrame")
    def eleventhFrame_button_event(self):
        self.select_frame_by_name("eleventhFrame")
    def twelvethFrame_button_event(self):
        self.select_frame_by_name("twelvethFrame")

    def seventhFrame_button_event(self):
        self.select_frame_by_name("seventhFrame")

    def eighthFrame_button_event(self):
        self.select_frame_by_name("eighthFrame")

    def ninthFrame_button_event(self):
        self.select_frame_by_name("ninthFrame")

    def tenthFrame_button_event(self):
        self.select_frame_by_name("tenthFrame")

    def eleventhFrame_button_event(self):
        self.select_frame_by_name("eleventhFrame")

    def twelvethFrame_button_event(self):
        self.select_frame_by_name("twelvethFrame")

    def ClearFields(self, frame):
        # Access attributes from frame_name object
        frame.decryptTextBox.delete(0, "end")
        frame.keyTextBox.delete(0, "end")
        frame.encryptTextBox.delete(0, "end")
    def create_gui_elements(self, frame_name, frame_label):
        frame_name.grid_columnconfigure(0, weight=1)
        frame_name.grid_rowconfigure(7, weight=1)

        Font = ("Georgia", 40 , "bold")  # Assuming Font is defined somewhere
        rFont = ("Calibri", 20   )
        Frame_label = customtkinter.CTkLabel(frame_name, text=frame_label, font=Font)
        Frame_label.grid(row=0, column=0, padx=20, pady=40, columnspan=2)

        radio_var = customtkinter.IntVar(value=0)
        encryptionRadio = customtkinter.CTkRadioButton(master=frame_name, variable=radio_var, value=0,
                                                       text="Encryption", font=rFont)
        encryptionRadio.grid(row=1, column=0, pady=0, padx=0, sticky="s")
        decryptionRadio = customtkinter.CTkRadioButton(master=frame_name, variable=radio_var, value=1,
                                                       text="Decryption",font=rFont)
        decryptionRadio.grid(row=1, column=1, pady=0, padx=100, sticky="w")

        encryptTextBox = customtkinter.CTkEntry(frame_name, placeholder_text="Plain text", height=50, width=0, font= rFont)
        encryptTextBox.grid(row=2, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        decryptTextBox = customtkinter.CTkEntry(frame_name, placeholder_text="Cipher text", height=50, width=0, font= rFont)
        decryptTextBox.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        keyTextBox = customtkinter.CTkEntry(frame_name, placeholder_text="Key", height=50, width=250 , font= rFont)
        keyTextBox.grid(row=3, column=0, padx=(20, 20), pady=0, sticky="ns" , columnspan=2 )

        processButton = customtkinter.CTkButton(frame_name, corner_radius=0, height=40, border_spacing=10,text = "Encrypt",
                                                font=customtkinter.CTkFont(family="Arial", size=20, weight="bold"),
                                                fg_color="transparent", text_color=("gray10", "gray90"),
                                                hover_color=("gray70", "gray30"), anchor="ns")
        processButton.grid(row=4, column=0, sticky="s", pady=5, columnspan=2)
        clearButton = customtkinter.CTkButton(frame_name, corner_radius=0, height=40, border_spacing=10,
                                                text="Clear",
                                                font=customtkinter.CTkFont(family="Arial", size=20, weight="bold"),
                                                fg_color="transparent", text_color=("gray10", "gray90"),
                                                hover_color=("gray70", "gray30"), anchor="ns",command = lambda:self.ClearFields(frame_name))
        clearButton.grid(row=4, column=1, sticky="s", pady=5,padx=5, columnspan=2)

        selectFileButton = customtkinter.CTkButton(frame_name, text="Select File", width=300, height=40,
                                                   command=self.select_file)
        selectFileButton.grid(row=5, column=0, sticky="s", pady=5, columnspan=2)

        downloadFileButton = customtkinter.CTkButton(frame_name, text="Download File", width=300, height=40 , command = self.download_file)
        downloadFileButton.grid(row=6, column=0, sticky="s", pady=5, columnspan=2)

        frame_name.encryptTextBox = encryptTextBox
        frame_name.Frame_label = Frame_label
        frame_name.encryptionRadio = encryptionRadio
        frame_name.decryptionRadio = decryptionRadio
        frame_name.decryptTextBox = decryptTextBox
        frame_name.keyTextBox = keyTextBox
        frame_name.processButton = processButton
        frame_name.selectFileButton = selectFileButton
        frame_name.downloadButton = downloadFileButton
        frame_name.radioVar = radio_var



    def select_file(self):
        filename = filedialog.askopenfilename(title="Select file to add")
        if filename:
            try:
                with open(filename, "r") as file:
                    file_content = file.read()
                try:
                    K = int(self.firstFrame.keyTextBox.get())
                except ValueError:
                    print("Invalid input: Please enter a valid integer.")
                    K = 0
                edited_content = self.CeaserDecryption(file_content,K)
                edited_filename = "edited_file.txt"
                self.firstFrame.filecontent = edited_content
                with open(edited_filename, "w") as edited_file:
                    edited_file.write(edited_content)
                print("Edited file created successfully:", edited_filename)
            except Exception as e:
                # Print an error message if any exception occurs
                print("Error:", e)
    def download_file(self):
        file = self.firstFrame.filecontent
        edited_filename = "Encrypted file.txt"
        with open(edited_filename, "w") as edited_file:
            edited_file.write(file)
        print("Edited file created successfully:", edited_filename)


if __name__ == "__main__":
    app = App()
    app.mainloop()
