import tkinter
from tkinter import filedialog, messagebox

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
                                                   command=self.ceaser_button_event)
        self.firstButton.grid(row=1, column=0, sticky="ew", pady=5)
        self.secondButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="play Fair",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),

                                                    image=self.logo_image, anchor="w",
                                                    command=self.playFair_button_event)

        self.secondButton.grid(row=1, column=1, sticky="ew", pady=5)
        self.RailFenceButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="Rail Fence",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),

                                                   image=self.logo_image, anchor="w",
                                                   command=self.RailFence_button_event)

        self.RailFenceButton.grid(row=2, column=0, sticky="ew", pady=5)
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
        self.ceaser = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.playFair = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.RailFence = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fifthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sixthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.seventhFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.eighthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.ninthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.tenthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.eleventhFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.twelvethFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.create_gui_elements(self.ceaser, "Ceaser")
        self.create_gui_elements(self.playFair, "play Fair")
        self.create_gui_elements(self.RailFence, "Rail Fence")
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
        self.bind_update_process_button_text(self.ceaser)
        self.bind_update_process_button_text(self.playFair)
        self.bind_update_process_button_text(self.RailFence)
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
        self.ceaser.processButton.configure(command=self.ceaserprocess_button_click)
        self.playFair.processButton.configure(command=self.playFairFunction)
        self.RailFence.processButton.configure(command = self.RailFenceButtonClicked)
        #Select first frame as a default ============================================
        self.select_frame_by_name("ceaser")

        # ==> Functions

    def ceaserprocess_button_click(self):
        # Get the ciphertext and key from the input fields
        PTxt = self.ceaser.encryptTextBox.get()
        K = self.ceaser.keyTextBox.get()
        CTxt = self.ceaser.decryptTextBox.get()
        rVar = self.ceaser.radioVar.get()
        # Perform decryption
        if rVar == 0 :
             decryptedText = self.CeaserEncryption(PTxt, int(K))
             self.ceaser.decryptTextBox.insert("end", decryptedText)
        else :
            encryptedText = self.CeaserDecryption(CTxt, int(K))
            self.ceaser.encryptTextBox.insert("end", encryptedText)

        def ceaserprocess_button_click(self):
            # Get the ciphertext and key from the input fields
            PTxt = self.ceaser.encryptTextBox.get()
            K = self.ceaser.keyTextBox.get()
            CTxt = self.ceaser.decryptTextBox.get()
            rVar = self.ceaser.radioVar.get()
            # Perform decryption
            if rVar == 0:
                decryptedText = self.CeaserEncryption(PTxt, int(K))
                self.ceaser.decryptTextBox.insert("end", decryptedText)
            else:
                encryptedText = self.CeaserDecryption(CTxt, int(K))
                self.ceaser.encryptTextBox.insert("end", encryptedText)

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
        self.ceaser.decryptTextBox.delete(0, "end")
        return ans
    def CeaserDecryption(self,plaintext,n):
        ans = ""
        for i in range(len(plaintext)):
            ch = plaintext[i]
            if ch == " ":
                ans += " "
            elif (ch.isupper()):
                ans += chr((ord(ch) - n - 65) % 26 + 65)
            else:
                ans += chr((ord(ch) - n - 97) % 26 + 97)
        self.ceaser.encryptTextBox.delete(0, "end")
        return ans

#==========================================================>
    def generateKeyMatrix(self,key):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        keyMatrix = [[None] * 5 for _ in range(5)]
        keySet = set()
        for char in key + alphabet:
            if char not in keySet:
                row, col = divmod(len(keySet), 5)
                keyMatrix[row][col] = char
                keySet.add(char)
        return keyMatrix

    def prepareMessage(self,message):
        message = message.upper().replace(" ", "")
        preparedMessage = ""
        i = 0
        while i < len(message):
            if i == len(message) - 1:
                preparedMessage += message[i] + "X"
            elif message[i] == message[i + 1]:
                preparedMessage += message[i] + "X"
                i -= 1
            else:
                preparedMessage += message[i:i + 2]
            i += 2

        return preparedMessage

    def encryptMessage(self,keyMatrix, message):
        encryptedMessage = ""

        for i in range(0, len(message), 2):
            a, b = message[i], message[i + 1]
            rowA, colA = self.findPosition(keyMatrix, a)
            rowB, colB = self.findPosition(keyMatrix, b)
            if rowA == rowB:
                encryptedMessage += keyMatrix[rowA][(colA + 1) % 5] + keyMatrix[rowB][(colB + 1) % 5]
            elif colA == colB:
                encryptedMessage += keyMatrix[(rowA + 1) % 5][colA] + keyMatrix[(rowB + 1) % 5][colB]
            else:
                encryptedMessage += keyMatrix[rowA][colB] + keyMatrix[rowB][colA]
        return encryptedMessage

    def findPosition(self,keyMatrix, char):
        for i in range(5):
            for j in range(5):
                if keyMatrix[i][j] == char:
                    return i,j
    def decryptMessage(self,keyMatrix, message):
        decryptedMessage = ""
        for i in range(0, len(message), 2):
            a, b = message[i], message[i + 1]
            rowA, colA = self.findPosition(keyMatrix, a)
            rowB, colB = self.findPosition(keyMatrix, b)

            if rowA == rowB:
                decryptedMessage += keyMatrix[rowA][(colA - 1) % 5] + keyMatrix[rowB][(colB - 1) % 5]
            elif colA == colB:
                decryptedMessage += keyMatrix[(rowA - 1) % 5][colA] + keyMatrix[(rowB - 1) % 5][colB]
            else:
                decryptedMessage += keyMatrix[rowA][colB] + keyMatrix[rowB][colA]
        return decryptedMessage


    def playFairFunction(self):
        msg = self.playFair.encryptTextBox.get()
        ky = self.playFair.keyTextBox.get()
        rVar = self.playFair.radioVar.get()
        # Validate inputs
        if not msg or not ky or not ky.isalpha() :
            messagebox.showerror("Error", msg)
            return

        # Prepare key matrix
        key = ky.upper().replace(" ", "")
        keyMatrix = self.generateKeyMatrix(key)

        # Prepare message
        msg = self.prepareMessage(msg)

        # Perform operation
        if rVar == 0:
            result = self.encryptMessage(keyMatrix, msg)
            self.playFair.decryptTextBox.delete(0,tkinter.END)
            self.playFair.decryptTextBox.insert("end", result)
        elif rVar == 1:

            result = self.decryptMessage(keyMatrix, msg)
            self.playFair.decryptTextBox.delete(0,tkinter.END)
            self.playFair.decryptTextBox.insert("end", result)

        # return result
#==============================================================>
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

    def RailFenceButtonClicked(self):
        # Get the ciphertext and key from the input fields
        self.RailFence.decryptTextBox.delete(0,"end")
        PlainText = self.RailFence.encryptTextBox.get()
        Key = self.RailFence.keyTextBox.get()
        rVar = self.RailFence.radioVar.get()

        if rVar == 0 :
             decryptedText = self.rail_fence_encrypt(PlainText, int(Key))
             self.RailFence.decryptTextBox.insert("end", decryptedText)
        else :
            encryptedText = self.rail_fence_decrypt(PlainText, int(Key))
            self.RailFence.decryptTextBox.insert("end", encryptedText)

    def rail_fence_encrypt(self,plaintext, rails):
        rails = int(rails)
        fence = [[] for _ in range(rails)]  # Create a list of empty lists to represent the fence
        rail = 0
        direction = 1  # Direction of movement along the rails (down or up)
        space_indices = [i for i, char in enumerate(plaintext) if char == ' ']  # Store the indices of spaces

        # Fill the fence with characters from the plaintext
        for char in plaintext:
            if char == ' ':
                continue
            fence[rail].append(char)
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1  # Change direction when reaching the top or bottom rail

        # Flatten the fence and concatenate the characters
        encrypted_text = ''.join(char for rail in fence for char in rail)

        # Add the spaces back into the encrypted text
        for index in space_indices:
            encrypted_text = encrypted_text[:index] + ' ' + encrypted_text[index:]

        return encrypted_text

    def rail_fence_decrypt(self,ciphertext, rails):
        rails = int(rails)
        fence = [['' for _ in ciphertext] for _ in range(rails)]  # Create an empty fence matrix
        rail = 0
        direction = 1
        space_indices = [i for i, char in enumerate(ciphertext) if char == ' ']  # Store the indices of spaces

        # Remove spaces from ciphertext
        ciphertext = ciphertext.replace(' ', '')

        # Fill the fence matrix with placeholders for characters
        for i in range(len(ciphertext)):
            fence[rail][i] = '*'
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        # Fill the fence matrix with ciphertext characters
        index = 0
        for i in range(rails):
            for j in range(len(ciphertext)):
                if fence[i][j] == '*':
                    fence[i][j] = ciphertext[index]
                    index += 1

        # Read the characters from the fence matrix to retrieve the plaintext
        rail = 0
        direction = 1
        decrypted_text = ''
        for i in range(len(ciphertext)):
            decrypted_text += fence[rail][i]
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        # Add the spaces back into the decrypted text
        for index in space_indices:
            decrypted_text = decrypted_text[:index] + ' ' + decrypted_text[index:]

        return decrypted_text

    # ---------------------------------------------


    def select_frame_by_name(self, name):
        # set button color for selected button

        self.firstButton.configure(fg_color=("gray75", "gray25") if name == "ceaser" else "transparent")
        self.secondButton.configure(fg_color=("gray75", "gray25") if name == "playFair" else "transparent")
        self.RailFenceButton.configure(fg_color=("gray75", "gray25") if name == "RailFence" else "transparent")
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
        if name == "ceaser":
            self.ceaser.grid(row=0, column=1, sticky="nsew")
        else:
            self.ceaser.grid_forget()

        if name == "playFair":
            self.playFair.grid(row=0, column=1, sticky="nsew")
        else:
            self.playFair.grid_forget()

        if name == "RailFence":
            self.RailFence.grid(row=0, column=1, sticky="nsew")
        else:
            self.RailFence.grid_forget()

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
    def ceaser_button_event(self):
        self.select_frame_by_name("ceaser")
    def playFair_button_event(self):
        self.select_frame_by_name("playFair")


    def RailFence_button_event(self):
        self.select_frame_by_name("RailFence")

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
        rVar = self.ceaser.radioVar.get()
        if filename:
            try:
                with open(filename, "r") as file:
                    file_content = file.read()
                try:
                    K = int(self.ceaser.keyTextBox.get())
                except ValueError:
                    print("Invalid input: Please enter a valid integer.")
                    K = 0
                if rVar==0:
                    edited_content = self.CeaserEncryption(file_content,K)
                else :
                    edited_content = self.CeaserDecryption(file_content,K)
                edited_filename = "edited_file.txt"
                self.ceaser.filecontent = edited_content
                # with open(edited_filename, "w") as edited_file:
                #     edited_file.write(edited_content)
                print("Edited file Opened successfully:", edited_filename)
            except Exception as e:
                # Print an error message if any exception occurs
                print("Error:", e)
    def download_file(self):
        content = self.ceaser.filecontent
        # print(file)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")],
                                                 title=f"Save {type} Message As")
        if file_path:
            # Write the encrypted message to the chosen file
            with open(file_path, "w") as file:
                file.write(content)

        print("Edited file Downloaded successfully:", file)


if __name__ == "__main__":
    app = App()
    app.mainloop()
