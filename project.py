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
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))

        #--> Begin of navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Home page",
                                                             image=self.logo_image,compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=10 , columnspan=2)
        self.firstButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="First way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.logo_image, anchor="w", command=self.firstFrame_button_event)
        self.firstButton.grid(row=1, column=0, sticky="ew" , pady=5)
        self.secondButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="Second way",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),

                                                    image=self.logo_image, anchor="w" , command=self.secondFrame_button_event)

        self.secondButton.grid(row=1, column=1, sticky="ew" , pady=5)
        self.thirdButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="third way",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),

                                                    image=self.logo_image, anchor="w", command=self.thirdFrame_button_event)

                                                 

        self.thirdButton.grid(row=2, column=0, sticky="ew" , pady=5)
        self.fourthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="fourth way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),

                                                   image=self.logo_image, anchor="w", command= self.fourthFrame_button_event)

                                             

        self.fourthButton.grid(row=2, column=1, sticky="ew" , pady=5)
        self.fifthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="third way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),

                                                   image=self.logo_image, anchor="w", command=self.fifthFrame_button_event)

                                                  

        self.fifthButton.grid(row=3, column=0, sticky="ew", pady=5)
        self.sixthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="third way",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),

                                                    image=self.logo_image, anchor="w", command=self.sixthFrame_button_event)

                                                  

        self.sixthButton.grid(row=3, column=1, sticky="ew", pady=5)
        self.sevenButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="third way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.logo_image, anchor="w")  # , command=self.first_button)
        self.sevenButton.grid(row=4, column=0, sticky="ew", pady=5)
        self.eightButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="third way",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    image=self.logo_image, anchor="w")  # , command=self.first_button)
        self.eightButton.grid(row=4, column=1, sticky="ew", pady=5)
        self.nineButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="third way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.logo_image, anchor="w")  # , command=self.first_button)
        self.nineButton.grid(row=5, column=0, sticky="ew", pady=5)
        self.tenButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="third way",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    image=self.logo_image, anchor="w")  # , command=self.first_button)
        self.tenButton.grid(row=5, column=1, sticky="ew", pady=5)
        self.elevenButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="third way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.logo_image, anchor="w")  # , command=self.first_button)
        self.elevenButton.grid(row=6, column=0, sticky="ew", pady=5)
        self.twelveButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="third way",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    image=self.logo_image, anchor="w")  # , command=self.first_button)
        self.twelveButton.grid(row=6, column=1, sticky="ew", pady=5)
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=0, pady=10, sticky="n" , columnspan=2)
        # ================> end of navigation <=================
        # ================> Frames Creation <===================
        self.firstFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.secondFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.thirdFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fifthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sixthFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.create_gui_elements(self.firstFrame,"firstWay")
        self.create_gui_elements(self.secondFrame,"second way")
        self.create_gui_elements(self.thirdFrame, "thirdFrame way")
        self.create_gui_elements(self.fourthFrame, "fourthFrame way")
        self.create_gui_elements(self.fifthFrame, "fifthFrame way")
        self.create_gui_elements(self.sixthFrame, "sixthFrame way")

       
        self.select_frame_by_name("firstFrame")
        #==> Functions
    def change_appearance_mode_event(self, new_appearance_mode):
                customtkinter.set_appearance_mode(new_appearance_mode)
#________________________________________
    def select_frame_by_name(self, name):
        # set button color for selected button

        self.firstButton.configure(fg_color=("gray75", "gray25") if name == "firstFrame" else "transparent")
        self.secondButton.configure(fg_color=("gray75", "gray25") if name == "secondFrame" else "transparent")
        self.thirdButton.configure(fg_color=("gray75", "gray25") if name == "thirdFrame" else "transparent")
        self.fourthButton.configure(fg_color=("gray75", "gray25") if name == "fourthFrame" else "transparent")
        self.fifthButton.configure(fg_color=("gray75", "gray25") if name == "fifthFrame" else "transparent")
        self.sixthButton.configure(fg_color=("gray75", "gray25") if name == "sixthFrame" else "transparent")
      


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
    #-----------------------------------------
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

    def create_gui_elements(self, frame_name , frame_label):
        frame_name.grid_columnconfigure(0, weight=1)
        frame_name.grid_rowconfigure(6, weight=1)

        Font = ("Arial", 12)  # Assuming Font is defined somewhere

        Frame_label = customtkinter.CTkLabel(frame_name, text=frame_label, font=Font)
        Frame_label.grid(row=0, column=0, padx=20, pady=40, columnspan=2)

        radio_var = customtkinter.IntVar(value=0)
        encryptionRadio = customtkinter.CTkRadioButton(master=frame_name, variable=radio_var, value=0, text="Encryption")
        encryptionRadio.grid(row=1, column=0, pady=0, padx=0, sticky="s")
        decryptionRadio = customtkinter.CTkRadioButton(master=frame_name, variable=radio_var, value=1, text="Decryption")
        decryptionRadio.grid(row=1, column=1, pady=0, padx=100, sticky="w")

        encryptTextbox = customtkinter.CTkEntry(frame_name, placeholder_text="Encryption", height=50, width=50)
        encryptTextbox.grid(row=2, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        decryptTextbox = customtkinter.CTkEntry(frame_name, placeholder_text="Decryption", height=50, width=50)
        decryptTextbox.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        processButton = customtkinter.CTkButton(frame_name, corner_radius=0, height=40, border_spacing=10, text="Process",
                                                fg_color="transparent", text_color=("gray10", "gray90"),
                                                hover_color=("gray70", "gray30"), anchor="w")
        processButton.grid(row=3, column=0, sticky="s", pady=5, columnspan=2)

        selectFileButton = customtkinter.CTkButton(frame_name, text="Select File", width=300, height=40,
                                                   command=self.select_file)
        selectFileButton.grid(row=4, column=0, sticky="s", pady=5, columnspan=2)

        downloadFileButton = customtkinter.CTkButton(frame_name, text="Download File", width=300, height=40)
        downloadFileButton.grid(row=5, column=0, sticky="s", pady=5, columnspan=2)

    
  



    def select_file(self):
     # Open a file dialog for the user to select the file to add
     filename = filedialog.askopenfilename(title="Select file to add")
     # Check if a file was selected
     if filename:
        try:
            # Open the selected file for reading
            with open(filename, "r") as file:
                # Read the content of the file
                file_content = file.read()

            # Perform edits on the file content (for example, convert to uppercase)
            edited_content = file_content.upper()

            # Specify the path for the new file with edited content
            edited_filename = "edited_file.txt"

            # Write the edited content to the new file
            with open(edited_filename, "w") as edited_file:
                edited_file.write(edited_content)

            # Print a message indicating the successful creation of the edited file
            print("Edited file created successfully:", edited_filename)
        except Exception as e:
            # Print an error message if any exception occurs
            print("Error:", e)
if __name__ == "__main__":
    app = App()
    app.mainloop()
