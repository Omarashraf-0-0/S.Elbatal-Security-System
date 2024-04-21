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
                                                    image=self.logo_image, anchor="w")  # , command=self.first_button)
        self.secondButton.grid(row=1, column=1, sticky="ew" , pady=5)
        self.thirdButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="third way",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    image=self.logo_image, anchor="w")  # , command=self.first_button)
        self.thirdButton.grid(row=2, column=0, sticky="ew" , pady=5)
        self.fourthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="fourth way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.logo_image, anchor="w")  # , command=self.first_button)
        self.fourthButton.grid(row=2, column=1, sticky="ew" , pady=5)
        self.fifthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                   border_spacing=10,
                                                   text="third way",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.logo_image, anchor="w")  # , command=self.first_button)
        self.fifthButton.grid(row=3, column=0, sticky="ew", pady=5)
        self.sixthButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=10,
                                                    text="third way",
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    image=self.logo_image, anchor="w")  # , command=self.first_button)
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
        self.firstFrame.grid_columnconfigure(0, weight=1)
        self.firstFrame.grid_rowconfigure(6,weight=1)

        self.firstFrame_label = customtkinter.CTkLabel(self.firstFrame, text="First Way" , font=Font)       #, image=self.large_test_image)
        self.firstFrame_label.grid(row=0, column=0, padx=20, pady=40 , columnspan = 2 )
        self.radio_var = tkinter.IntVar(value=0)
        self.encryptionRadio = customtkinter.CTkRadioButton(master=self.firstFrame, variable=self.radio_var,value=0 , text = "Encryption")
        self.encryptionRadio.grid(row=1, column=0, pady=0, padx=00, sticky="s")
        self.decryptionRadio = customtkinter.CTkRadioButton(master=self.firstFrame, variable=self.radio_var, value=1 , text = "Decryption")
        self.decryptionRadio.grid(row=1, column=1, pady=0, padx=100, sticky="w")
        self.encryptTextbox = customtkinter.CTkEntry(self.firstFrame, placeholder_text="Encryption" , height= 50 , width= 50 )
        self.encryptTextbox.grid(row=2, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew" )
        self.decryptTextbox = customtkinter.CTkEntry(self.firstFrame, placeholder_text="Decryption" , height= 50 , width= 50)
        self.decryptTextbox.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.processButton = customtkinter.CTkButton(self.firstFrame, corner_radius=0, height=40,
                                                    border_spacing=10,text="Process",fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),image=self.logo_image, anchor="w")  # , command=self.first_button)
        self.processButton.grid(row=3, column=0, sticky="s", pady=5 , columnspan = 2)

        self.selectFileButton = customtkinter.CTkButton(self.firstFrame, text="Select File", width= 300 , height= 40 , command=self.select_file)

        self.selectFileButton.grid(row=4, column=0, sticky="s", pady=5 , columnspan = 2 )
        self.downloadFileButton = customtkinter.CTkButton(self.firstFrame, text="Download File", width= 300 , height= 40 )
        # command=self.select_file)
        self.downloadFileButton.grid(row=5, column=0, sticky="s", pady=5 , columnspan= 2)
        # self.encryptTextbox = customtkinter.CTkTextbox(self.firstFrame, width=50 , height=40)
        # self.encryptTextbox.grid(row=2, column=0, padx=10, pady=0, sticky="nsew")
        self.select_frame_by_name("firstFrame")
        #==> Functions
    def change_appearance_mode_event(self, new_appearance_mode):
                customtkinter.set_appearance_mode(new_appearance_mode)
#________________________________________
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.firstButton.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        # self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        # self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "firstFrame":
            self.firstFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.firstFrame.grid_forget()
    #-----------------------------------------
    def firstFrame_button_event(self):
        self.select_frame_by_name("firstFrame")


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

