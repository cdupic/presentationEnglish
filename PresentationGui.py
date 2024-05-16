from customtkinter import *
import customtkinter as ctk
from PIL import Image as PILImage, ImageTk
import tkinter as tk
from tkinter import *
import time
from itertools import count, cycle

class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """

    def load(self, im):
        if isinstance(im, str):
            im = PILImage.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.configure(image=next(self.frames))
            self.after(self.delay, self.next_frame)



class Gui(ctk.CTk):

    __slots__ = ["frame_initial", "label_initial", "image_accueil", "bouton_initial", "font"]

    def __init__(self):
        super().__init__()
        self.title("Presentation")

        # lancer l'appli en premier plan
        self.grab_set()

        # lancer l'appli au milieu de l'écran
        self.geometry(self.CenterWindowToDisplay(800, 600))

        # definition de la police
        self.font = CTkFont(family="Helvetica", size=25)

        self.recette_parcourues = [False, False, False, False]

        # Images
        self.image_cookies = CTkImage(PILImage.open("pictures/biscuits.png"), size=(100, 100))
        self.image_chocolate_cake = CTkImage(PILImage.open("pictures/brownie.png"), size=(100, 100))
        self.image_crepe = CTkImage(PILImage.open("pictures/crepe.png"), size=(100, 100))
        self.image_beignet = CTkImage(PILImage.open("pictures/beignet.png"), size=(100, 100))

        self.image_beurre = CTkImage(PILImage.open("pictures/butter.png"), size=(50, 50))
        self.image_lait = CTkImage(PILImage.open("pictures/milk.png"), size=(50, 50))
        self.image_sucre = CTkImage(PILImage.open("pictures/sugar.png"), size=(50, 50))
        self.image_sucre_canne = CTkImage(PILImage.open("pictures/food.png"), size=(50, 50))
        self.image_farine = CTkImage(PILImage.open("pictures/flour.png"), size=(50, 50))
        self.image_levure = CTkImage(PILImage.open("pictures/yeast.png"), size=(50, 50))
        self.image_oeuf = CTkImage(PILImage.open("pictures/egg.png"), size=(50, 50))
        self.image_huile = CTkImage(PILImage.open("pictures/olive-oil.png"), size=(50, 50))
        self.image_versus = CTkImage(PILImage.open("pictures/versus.png"), size=(50, 50))
        self.image_chocolat = CTkImage(PILImage.open("pictures/chocolate-chip.png"), size=(50, 50))
        self.image_star = CTkImage(PILImage.open("pictures/star.png"), size=(50, 50))
        self.image_chocolate_bar = CTkImage(PILImage.open("pictures/chocolate-bar.png"), size=(50, 50))
        self.image_first = CTkImage(PILImage.open("pictures/first.png"), size=(50, 50))
        self.image_second = CTkImage(PILImage.open("pictures/second.png"), size=(50, 50))
        self.image_third = CTkImage(PILImage.open("pictures/third.png"), size=(50, 50))



        self.image_next = CTkImage(PILImage.open("pictures/next.png"), size=(100, 100))
        self.trophy = CTkImage(PILImage.open("pictures/trophy.png"), size=(100, 100))

        self.expectation_cake = CTkImage(PILImage.open("pictures/cake_expectation.png"), size=(500, 500))
        self.expectation_crepe = CTkImage(PILImage.open("pictures/crepes_expectation.png"), size=(500, 500))
        self.expectation_cookie = CTkImage(PILImage.open("pictures/cookies_expectation.png"), size=(500, 500))
        self.expectation_beignet = CTkImage(PILImage.open("pictures/beignet_expectation.png"), size=(500, 500))

        self.result_crepe = CTkImage(PILImage.open("pictures/result_crepe.png"), size=(500, 500))
        self.result_cookies = CTkImage(PILImage.open("pictures/result_cookie.png"), size=(500, 500))
        self.result_chocolate_cake = CTkImage(PILImage.open("pictures/result_cake.png"), size=(500, 500))
        self.result_beignet = CTkImage(PILImage.open("pictures/result_beignet.png"), size=(500, 500))

        self.recepe_cookie = CTkImage(PILImage.open("pictures/recepe_cookie.png"), size=(400, 500))
        self.recepe_beignet = CTkImage(PILImage.open("pictures/recepe_beignet.png"), size=(575, 600))
        self.recepe_crepe = CTkImage(PILImage.open("pictures/recepe_crepe.png"), size=(350, 450))
        self.recepe_crepe_2 = CTkImage(PILImage.open("pictures/recepe_2_crepe.png"), size=(350, 450))

        self.gif_cooking = PILImage.open("pictures/cooking_gif.gif")
        self.gif_crepe = PILImage.open("pictures/crepe_gif.gif")
        self.gif_beignet = PILImage.open("pictures/beignet_gif.gif")




        self.ecran_initial()



    def CenterWindowToDisplay(self, width: int, height: int):
        """Centers the window to the main display/monitor"""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int(((screen_width / 2) - (width / 2)) * self._get_window_scaling())
        y = int(((screen_height / 2) - (height / 2)) * self._get_window_scaling())
        return f"{width}x{height}+{x}+{y}"

    def ecran_initial(self):

        self.frame_initial = CTkFrame(self, fg_color="#EEDECF")
        self.frame_initial.pack(expand=True, fill="both")

        self.image_accueil = PhotoImage(file='pictures/acceuilV2.png')

        self.label_initial = CTkLabel(self.frame_initial, text="", image=self.image_accueil, compound="bottom")
        self.label_initial.pack(expand=True, fill="both")

        self.bouton_initial = CTkButton(self.frame_initial, text="Start presentation", height=30, font=self.font)
        self.bouton_initial.pack(side="bottom", pady=30)
        self.bouton_initial.bind('<Button-1>', self.ecran_selection)

    def ecran_selection(self, event=None):
        self.frame_initial.destroy()

        self.frame_selection = CTkFrame(self, fg_color="#EEDECF")
        self.frame_selection.pack(expand=True, fill="both")

        self.frame_selection.columnconfigure(0, weight=1)
        self.frame_selection.columnconfigure(1, weight=5)

        self.frame_selection.rowconfigure(0, weight=1)
        self.frame_selection.rowconfigure(1, weight=1)
        self.frame_selection.rowconfigure(2, weight=1)
        self.frame_selection.rowconfigure(3, weight=1)
        self.frame_selection.rowconfigure(4, weight=1)


        #self.image_ruban = CTkImage(PILImage.open("pictures/ruban.png"), size=(1000, 40))


        #Boutons relatifs aux gateaux

        self.button_cookies = CTkButton(self.frame_selection, text="   Cookies  ", font=self.font, image=self.image_cookies, compound="left", text_color="purple", fg_color="#EEDECF", hover_color="#FED4E7")
        self.button_cookies.grid(row=0, column=0)

        self.button_chocolate_cake = CTkButton(self.frame_selection, text="   Cake  ", font=self.font, image=self.image_chocolate_cake, compound="left", text_color="purple", fg_color="#EEDECF", hover_color="#FED4E7")
        self.button_chocolate_cake.grid(row=1, column=0)

        self.button_crepe = CTkButton(self.frame_selection, text="   Crepe  ", font=self.font, image=self.image_crepe, compound="left", text_color="purple", fg_color="#EEDECF", hover_color="#FED4E7")
        self.button_crepe.grid(row=2, column=0)

        self.button_beignet = CTkButton(self.frame_selection, text="   Doughnut  ", font=self.font, image=self.image_beignet, compound="left", text_color="purple", fg_color="#EEDECF", hover_color="#FED4E7")
        self.button_beignet.grid(row=3, column=0)

        self.button_classement = CTkButton(self.frame_selection, text="", image=self.trophy, fg_color="grey", hover_color="#FED4E7", state="disabled", command= lambda : self.conclusion())
        self.button_classement.grid(row=4, column=0)




        #Frame pour l'affichage des recettes
        self.cooking_recepe_frame = CTkFrame(self.frame_selection, fg_color="#E5B769")
        self.cooking_recepe_frame.grid(row=0, column=1, rowspan=5, sticky="nsew", pady=20, padx=20)

        self.cooking_recepe_label = CTkLabel(self.cooking_recepe_frame, text="Cooking recepe", font=self.font)
        self.cooking_recepe_label.pack(side="top", pady=20, fill="x")

        self.frame_liste_ingredients = CTkFrame(self.cooking_recepe_frame, fg_color="#E5B769")
        self.frame_liste_ingredients.pack(side="top", pady=20, fill="x")



        self.button_cookies.bind('<Button-1>', lambda event: self.ecran_recete('cookies'))
        self.button_chocolate_cake.bind('<Button-1>', lambda event: self.ecran_recete('chocolate_cake'))
        self.button_crepe.bind('<Button-1>', lambda event: self.ecran_recete('crepe'))
        self.button_beignet.bind('<Button-1>', lambda event: self.ecran_recete('beignet'))


    def ecran_recete(self, recette: str):

        if recette == 'cookies':
            self.cooking_recepe_label.configure(text="     You've choosen cookies recepe, lets get started !")
            self.cooking_recepe_label.configure(image=self.image_cookies, compound="left")
            self.affichage_liste_ingredients('cookies')

        elif recette == 'chocolate_cake':
            self.cooking_recepe_label.configure(text="     You've choosen chocolate cake recepe, lets get started !")
            self.cooking_recepe_label.configure(image=self.image_chocolate_cake, compound="left")
            self.affichage_liste_ingredients('chocolate_cake')

        elif recette == 'crepe':
            self.cooking_recepe_label.configure(text="     You've choosen crepe recepe, lets get started !")
            self.cooking_recepe_label.configure(image=self.image_crepe, compound="left")
            self.affichage_liste_ingredients('crepe')

        elif recette == 'beignet':
            self.cooking_recepe_label.configure(text="     You've choosen doughnut recepe, lets get started !")
            self.cooking_recepe_label.configure(image=self.image_beignet, compound="left")
            self.affichage_liste_ingredients('beignet')

    def affichage_liste_ingredients(self, recette: str):


        if recette == "cookies":

            self.frame_liste_ingredients.destroy()

            # self.disable_buttons()

            self.frame_liste_ingredients = CTkFrame(self.cooking_recepe_frame, fg_color="#E5B769")
            self.frame_liste_ingredients.pack(side="top", pady=5, fill="x")


            self.label_ingredient_1 = CTkLabel(self.frame_liste_ingredients,text="   85 g of butter", image=self.image_beurre, compound="left", font=self.font)
            self.label_ingredient_1.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_2 = CTkLabel(self.frame_liste_ingredients, text="   85 g of sugar", image=self.image_sucre, compound="left", font=self.font)
            self.label_ingredient_2.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_3 = CTkLabel(self.frame_liste_ingredients, text="   1 bag of yeast", image=self.image_levure, compound="left", font=self.font)
            self.label_ingredient_3.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_4 = CTkLabel(self.frame_liste_ingredients, text="   1 egg", font=self.font, image=self.image_oeuf, compound="left")
            self.label_ingredient_4.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_5 = CTkLabel(self.frame_liste_ingredients, text="   150 g of flour", font=self.font, image=self.image_farine, compound="left")
            self.label_ingredient_5.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_6 = CTkLabel(self.frame_liste_ingredients, text="   chocolate chips", font=self.font, image=self.image_chocolat, compound="left")
            self.label_ingredient_6.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_7 = CTkLabel(self.frame_liste_ingredients, text="   an ounce of nutella", font=self.font, image=self.image_star, compound="left")
            self.label_ingredient_7.pack(side="top", pady=20, fill="x")


            self.next_button = CTkButton(self.frame_liste_ingredients, text="next step", font=self.font)
            self.next_button.pack(side="top", pady=20)
            self.next_button.bind('<Button-1>', lambda event: self.show_preparation('cookies'))

            # self.enable_button()






        elif recette == "chocolate_cake":

            self.frame_liste_ingredients.destroy()

            # disable les autres buttons sinon
            # self.disable_buttons()

            self.frame_liste_ingredients = CTkFrame(self.cooking_recepe_frame, fg_color="#E5B769")
            self.frame_liste_ingredients.pack(side="top", pady=20, fill="x")


            self.label_ingredient_1 = CTkLabel(self.frame_liste_ingredients,text="   50 g of chocolate", image=self.image_chocolate_bar, compound="left", font=self.font)
            self.label_ingredient_1.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_2 = CTkLabel(self.frame_liste_ingredients, text="   33.5 g of sugar", image=self.image_sucre, compound="left", font=self.font)
            self.label_ingredient_2.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_3 = CTkLabel(self.frame_liste_ingredients, text="   1 bag of yeast", image=self.image_levure, compound="left", font=self.font)
            self.label_ingredient_3.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_4 = CTkLabel(self.frame_liste_ingredients, text="   1 egg", font=self.font, image=self.image_oeuf, compound="left")
            self.label_ingredient_4.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_5 = CTkLabel(self.frame_liste_ingredients, text="   26.5 g of butter", font=self.font, image=self.image_beurre, compound="left")
            self.label_ingredient_5.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_6 = CTkLabel(self.frame_liste_ingredients, text="   20 g of flour", font=self.font, image=self.image_farine, compound="left")
            self.label_ingredient_6.pack(side="top", pady=20, fill="x")

            self.next_button = CTkButton(self.frame_liste_ingredients, text="next step", font=self.font)
            self.next_button.pack(side="top", pady=40)
            self.next_button.bind('<Button-1>', lambda event: self.show_result('chocolate_cake'))



            # self.enable_button()

        elif recette == "crepe":

            self.frame_liste_ingredients.destroy()

            # disable les autres buttons sinon
            # self.disable_buttons()

            self.frame_liste_ingredients = CTkFrame(self.cooking_recepe_frame, fg_color="#E5B769")
            self.frame_liste_ingredients.pack(side="top", pady=20, fill="x")


            self.label_ingredient_1 = CTkLabel(self.frame_liste_ingredients,text="   33.5g of melted butter", image=self.image_beurre, compound="left", font=self.font)
            self.label_ingredient_1.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_2 = CTkLabel(self.frame_liste_ingredients, text="   2 spoons of sugar", image=self.image_sucre, compound="left", font=self.font)
            self.label_ingredient_2.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_3 = CTkLabel(self.frame_liste_ingredients, text="   40 cl of milk", image=self.image_lait, compound="left", font=self.font)
            self.label_ingredient_3.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)


            self.label_ingredient_4 = CTkLabel(self.frame_liste_ingredients, text="   2 eggs", font=self.font, image=self.image_oeuf, compound="left")
            self.label_ingredient_4.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_5 = CTkLabel(self.frame_liste_ingredients, text="   200g of flour", font=self.font, image=self.image_farine, compound="left")
            self.label_ingredient_5.pack(side="top", pady=20, fill="x")

            self.label_ingredient_6 = CTkLabel(self.frame_liste_ingredients, text="   1.5 spoon of olive oil", font=self.font, image=self.image_huile, compound="left")
            self.label_ingredient_6.pack(side="top", pady=20, fill="x")

            self.next_button = CTkButton(self.frame_liste_ingredients, text="  next step", font=self.font)
            self.next_button.pack(side="top", pady=40)
            self.next_button.bind('<Button-1>', lambda event: self.show_preparation('crepe'))

            self.enable_button()

        elif recette == "beignet":

            self.frame_liste_ingredients.destroy()

            # disable les autres buttons sinon
            self.disable_buttons()

            self.frame_liste_ingredients = CTkFrame(self.cooking_recepe_frame, fg_color="#E5B769")
            self.frame_liste_ingredients.pack(side="top", pady=20, fill="x")


            self.label_ingredient_1 = CTkLabel(self.frame_liste_ingredients,text="   1/3 bag of yeast", image=self.image_levure, compound="left", font=self.font)
            self.label_ingredient_1.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_2 = CTkLabel(self.frame_liste_ingredients, text="   1.5 spoons of sugar", image=self.image_sucre, compound="left", font=self.font)
            self.label_ingredient_2.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_3 = CTkLabel(self.frame_liste_ingredients, text="   63 ml of milk", image=self.image_lait, compound="left", font=self.font)
            self.label_ingredient_3.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)


            self.label_ingredient_4 = CTkLabel(self.frame_liste_ingredients, text="   1 egg", font=self.font, image=self.image_oeuf, compound="left")
            self.label_ingredient_4.pack(side="top", pady=20, fill="x")
            self.update()
            time.sleep(1)

            self.label_ingredient_5 = CTkLabel(self.frame_liste_ingredients, text="   125 g of flour", font=self.font, image=self.image_farine, compound="left")
            self.label_ingredient_5.pack(side="top", pady=20, fill="x")

            self.label_ingredient_6 = CTkLabel(self.frame_liste_ingredients, text="   1/2 vanilla sugar", font=self.font, image=self.image_star, compound="left")
            self.label_ingredient_6.pack(side="top", pady=20, fill="x")

            self.next_button = CTkButton(self.frame_liste_ingredients, text="next step", font=self.font)
            self.next_button.pack(side="top", pady=40)
            self.next_button.bind('<Button-1>', lambda event: self.show_preparation('beignet'))

            # self.enable_button()

    def show_preparation(self, recette : str):

        self.frame_liste_ingredients.destroy()
        # self.disable_buttons()

        self.frame_liste_ingredients = CTkFrame(self.cooking_recepe_frame, fg_color="#E5B769")
        self.frame_liste_ingredients.pack(side="top", pady=20, fill="x")

        if recette == "cookies":
            self.cooking_recepe_label.configure(text="     Let's start the preparation of cookies", image=self.image_cookies, compound="left")
            self.preparation_button = CTkButton(self.frame_liste_ingredients, text="", font=self.font, image=self.image_next, fg_color="#E5B769", hover_color="#E5B769")
            self.preparation_button.pack(side="bottom", pady=100)
            self.preparation_button.bind('<Button-1>', lambda event: self.show_image_preparation('cookies'))

            self.lbl = ImageLabel(self.frame_liste_ingredients)
            self.lbl.pack()
            self.lbl.load('pictures/cooking_gif.gif')
            self.lbl.mainloop()



        elif recette == "crepe":
            self.cooking_recepe_label.configure(text="     Let's start the preparation of crepes", image=self.image_crepe, compound="left")
            self.preparation_button = CTkButton(self.frame_liste_ingredients, text="", font=self.font, image=self.image_next, fg_color="#E5B769", hover_color="#E5B769")
            self.preparation_button.pack(side="bottom", pady=100)
            self.preparation_button.bind('<Button-1>', lambda event: self.show_image_preparation('crepe'))

            self.lbl = ImageLabel(self.frame_liste_ingredients)
            self.lbl.pack()
            self.lbl.load('pictures/crepe_gif.gif')
            self.lbl.mainloop()


        elif recette == "beignet":
            self.cooking_recepe_label.configure(text="     Let's start the preparation of doughnuts", image=self.image_beignet, compound="left")
            self.lbl = ImageLabel(self.frame_liste_ingredients)
            self.preparation_button = CTkButton(self.frame_liste_ingredients, text="", font=self.font, image=self.image_next, fg_color="#E5B769", hover_color="#E5B769")
            self.preparation_button.pack(side="bottom", pady=100)
            self.preparation_button.bind('<Button-1>', lambda event: self.show_image_preparation('beignet'))

            self.lbl.pack()
            self.lbl.load('pictures/beignet_gif.gif')
            self.lbl.mainloop()


        # self.label_gif = CTkLabel(self.frame_liste_ingredients, fg_color="transparent", bg_color="transparent", text="")
        # self.label_gif.pack(side="top", pady=20)

    def show_image_preparation(self, recette: str):
        self.lbl.destroy()
        if recette == "cookies":

            self.label_preparation_cookie = CTkLabel(self.frame_liste_ingredients, text="", image=self.recepe_cookie)
            self.label_preparation_cookie.pack(side="top", anchor='center')
            self.preparation_button.bind('<Button-1>', lambda event: self.show_result('cookies'))

        elif recette == "crepe":
            self.label_preparation_crepe = CTkLabel(self.frame_liste_ingredients, text="", image=self.recepe_crepe)
            self.label_preparation_crepe.pack(side="left", pady=50, padx=200, anchor='center')
            self.label_preparation_crepe2 = CTkLabel(self.frame_liste_ingredients, text="", image=self.recepe_crepe_2)
            self.label_preparation_crepe2.pack(side="left", pady=50, anchor='center')
            self.preparation_button.bind('<Button-1>', lambda event: self.show_result('crepe'))

        elif recette == "beignet":
            self.label_preparation_cookie = CTkLabel(self.frame_liste_ingredients, text="", image=self.recepe_beignet)
            self.label_preparation_cookie.pack(side="top")
            self.preparation_button.bind('<Button-1>', lambda event: self.show_result('beignet'))





    def show_result(self, recette : str):
        self.frame_liste_ingredients.destroy()
        self.frame_liste_ingredients = CTkFrame(self.cooking_recepe_frame, fg_color="#E5B769")
        self.frame_liste_ingredients.pack(side="top", pady=20, fill="x")

        self.cooking_recepe_label.configure(text="Expectation         Reality        ", compound="center", image=self.image_versus)
        if recette== "cookies":
            self.recette_parcourues[0] = True
            self.label_expectation_cookie = CTkLabel(self.frame_liste_ingredients, text="", image=self.expectation_cookie)
            self.label_expectation_cookie.pack(side="left", pady=50, padx=100, anchor='center')
            self.label_result_cookie = CTkLabel(self.frame_liste_ingredients, text="", image=self.result_cookies)
            self.label_result_cookie.pack(side="left", pady=50, anchor='center')

            value = True
            for el in self.recette_parcourues:
                if not el :
                    value = False
                    break
            if value:
                self.button_classement.configure(fg_color="#E5B769", hover_color="pink", state="normal")




        elif recette == "chocolate_cake":
            self.recette_parcourues[1] = True

            self.label_expectation_cake = CTkLabel(self.frame_liste_ingredients, text="", image=self.expectation_cake)
            self.label_expectation_cake.pack(side="left", pady=50, padx=100, anchor='center')
            self.label_result_cake = CTkLabel(self.frame_liste_ingredients, text="", image=self.result_chocolate_cake)
            self.label_result_cake.pack(side="left", pady=50, anchor='center')

            value = True
            for el in self.recette_parcourues:
                if not el :
                    value = False
                    break
            if value:
                self.button_classement.configure(fg_color="#E5B769", hover_color="pink", state="normal")


        elif recette == "crepe":
            self.recette_parcourues[2] = True

            self.label_expectation_crepe = CTkLabel(self.frame_liste_ingredients, text="", image=self.expectation_crepe)
            self.label_expectation_crepe.pack(side="left", pady=50, padx=100, anchor='center')
            self.label_result_crepe = CTkLabel(self.frame_liste_ingredients, text="", image=self.result_crepe)
            self.label_result_crepe.pack(side="left", pady=50, anchor='center')
            value = True
            for el in self.recette_parcourues:
                if not el :
                    value = False
                    break
            if value:
                self.button_classement.configure(fg_color="#E5B769", hover_color="pink", state="normal")


        elif recette == "beignet":
            self.recette_parcourues[3] = True

            self.label_expectation_beignet = CTkLabel(self.frame_liste_ingredients, text="", image=self.expectation_beignet)
            self.label_expectation_beignet.pack(side="left", pady=50, padx=100, anchor='center')
            self.label_result_beignet = CTkLabel(self.frame_liste_ingredients, text="", image=self.result_beignet)
            self.label_result_beignet.pack(side="left", pady=50, anchor='center')

            value = True
            for el in self.recette_parcourues:
                if not el :
                    value = False
                    break
            if value:
                self.button_classement.configure(fg_color="#E5B769", hover_color="pink", state="normal")



    def conclusion(self, event=None):
        ## idée :,mettre un tableau avec une ligne pour chacune des recettes et en colonne : une note/5 pour : facilité, rapidité de consommation,et saveur
        self.frame_liste_ingredients.destroy()
        self.frame_liste_ingredients = CTkFrame(self.cooking_recepe_frame, fg_color="#E5B769")
        self.frame_liste_ingredients.pack(side="top", pady=20, fill="x")
        self.cooking_recepe_label.configure(text="Ranking", image=None)


        self.button1 = CTkButton(self.frame_liste_ingredients, text="", image=self.image_first, compound="left",  fg_color="#E5B769", hover_color="#E5B769", text_color="white")
        self.button1.pack(side="top", anchor='center', pady=40)

        self.button2 = CTkButton(self.frame_liste_ingredients, text="", image=self.image_second, compound="left",  fg_color="#E5B769", hover_color="#E5B769", text_color="white")
        self.button2.pack(side="top", anchor='center', pady=40)

        self.button3 = CTkButton(self.frame_liste_ingredients, text="", image=self.image_third, compound="left", fg_color="#E5B769", hover_color="#E5B769", text_color="white")
        self.button3.pack(side="top", anchor='center', pady=40)

        self.button1.bind('<Button-1>', self.affiche_1)
        self.button2.bind('<Button-1>', self.affiche_2)
        self.button3.bind('<Button-1>', self.affiche_3)




        self.criteres = ["difficulty", "time", "taste"]

        self.cookies_notes = [1, 3, 4]
        self.chocolate_cake_notes = []
        self.crepes_notes = [2, 3, 3]
        self.beignets_notes = [3, 2, 2]

        self.sources = ["https://www.marmiton.org/recettes/recette_cookies-maison_86989.aspx", "https://www.marmiton.org/recettes/recette_cake-au-chocolat_17391.aspx", "https://www.marmiton.org/recettes/recette_pate-a-crepes_12372.aspx", "https://cuisine.journaldesfemmes.fr/recette/310213-beignets-rapides-pupperchen"]

    def affiche_1(self, event=None):
        self.button1.configure(text="     Cookies !", state="disabled", font=self.font)

    def affiche_2(self, event=None):
        self.button2.configure(text="     Muffin !", state="disabled",  font=self.font)

    def affiche_3(self, event=None):
        self.button3.configure(text="     Crepes !", state="disabled",  font=self.font)


    def disable_buttons(self):
        self.button_chocolate_cake.configure(state="disabled")
        self.button_cookies.configure(state="disabled")
        self.button_crepe.configure(state="disabled")
        self.button_beignet.configure(state="disabled")

    def enable_button(self):
        self.button_chocolate_cake.configure(state="enabled")
        self.button_cookies.configure(state="enabled")
        self.button_crepe.configure(state="enabled")
        self.button_beignet.configure(state="enabled")





if __name__ == "__main__":
    root = Gui()
    root.mainloop()
