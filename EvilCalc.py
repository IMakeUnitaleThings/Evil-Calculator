import random
import customtkinter

global EquationString
EquationString = ''
def AddSymbol(symbol):
    global EquationString
    EquationString = EquationString+str(symbol)
    DisplayTextbox.configure(state="normal")
    DisplayTextbox.delete(0.0, "end")
    DisplayTextbox.insert(0.0, EquationString)
    DisplayTextbox.configure(state="disabled")
def Clear():
    global EquationString
    EquationString = ""
    DisplayTextbox.configure(state="normal")
    DisplayTextbox.delete(0.0, "end")
    DisplayTextbox.insert(0.0, EquationString)
    DisplayTextbox.configure(state="disabled")
def Calculate():
    global EquationString
    EquationString = eval(EquationString)
    WrongEquationString = random.randint(int(round(int(EquationString)/1.2, 0)), int(round(int(EquationString)*1.2, 0)))
    if WrongEquationString == EquationString:
        WrongEquationString -= 1
    EquationString = WrongEquationString
    EquationString=str(EquationString)
    DisplayTextbox.configure(state="normal")
    DisplayTextbox.delete(0.0, "end")
    DisplayTextbox.insert(0.0, EquationString)
    DisplayTextbox.configure(state="disabled")

app = customtkinter.CTk()
app.title("Evil Calc")
app.geometry("480x720")
#app.iconbitmap("icon.ico")
customtkinter.set_default_color_theme("green")
#standard button is 120x120
DisplayTextbox = customtkinter.CTkTextbox(app, width=480, height=120, wrap=None, font=("Arial", 30))
DisplayTextbox.grid(row=0, column=0, columnspan=4)
DisplayTextbox.configure(state="normal")
DisplayTextbox.delete(0.0, "end")
DisplayTextbox.insert(0.0, EquationString)
DisplayTextbox.configure(state="disabled")

#Buttons - Row one
ClearButton = customtkinter.CTkButton(app,text="x", text_color="#ff0000", command=Clear, width=120, height=120, font=("Arial", 30))
ClearButton.grid(row=1, column=0)
ParenthesisLeft = customtkinter.CTkButton(app, text="(", command=lambda: AddSymbol("("), width=120, height=120, font=("Arial", 30))
ParenthesisLeft.grid(row=1, column=1)
ParenthesisRight = customtkinter.CTkButton(app, text=")", command=lambda: AddSymbol(")"), width=120, height=120, font=("Arial", 30))
ParenthesisRight.grid(row=1, column=2)
DivideButton = customtkinter.CTkButton(app,text="÷", command=lambda: AddSymbol("/"), width=120, height=120, font=("Arial", 30))
DivideButton.grid(row=1, column=3)

#Buttons - Row two
SevenButton = customtkinter.CTkButton(app, text="7", command=lambda: AddSymbol("7"), width=120, height=120, font=("Arial", 30))
SevenButton.grid(row=2, column=0)
EightButton = customtkinter.CTkButton(app, text="8", command=lambda: AddSymbol("8"), width=120, height=120, font=("Arial", 30))
EightButton.grid(row=2, column=1)
NineButton = customtkinter.CTkButton(app, text="9", command=lambda: AddSymbol("9"), width=120, height=120, font=("Arial", 30))
NineButton.grid(row=2, column=2)
MultiplyButton = customtkinter.CTkButton(app, text="X", command=lambda: AddSymbol("*"), width=120, height=120, font=("Arial", 30))
MultiplyButton.grid(row=2, column=3)

# Buttons - Row 3
FourButton = customtkinter.CTkButton(app, text="4", command=lambda: AddSymbol("4"), width=120, height=120, font=("Arial", 30))
FourButton.grid(row=3, column=0)
FiveButton = customtkinter.CTkButton(app, text="5", command=lambda: AddSymbol("5"), width=120, height=120, font=("Arial", 30))
FiveButton.grid(row=3, column=1)
SixButton = customtkinter.CTkButton(app, text="6", command=lambda: AddSymbol("6"), width=120, height=120, font=("Arial", 30))
SixButton.grid(row=3, column=2)
SubtractionButton = customtkinter.CTkButton(app, text="-", command=lambda: AddSymbol("-"), width=120, height=120, font=("Arial", 30))
SubtractionButton.grid(row=3, column=3)

# Buttons = Row 4
ThreeButton = customtkinter.CTkButton(app, text="3", command=lambda: lambda: AddSymbol("3"), width=120, height=120, font=("Arial", 30))
ThreeButton.grid(row=4, column=0)
TwoButton = customtkinter.CTkButton(app, text="2", command=lambda: AddSymbol("2"), width=120, height=120, font=("Arial", 30))
TwoButton.grid(row=4, column=1)
OneButton = customtkinter.CTkButton(app, text="1", command=lambda: AddSymbol("1"), width=120, height=120, font=("Arial", 30))
OneButton.grid(row=4, column=2)
AdditionButton = customtkinter.CTkButton(app, text="+", command=lambda: AddSymbol("+"), width=120, height=120, font=("Arial", 30))
AdditionButton.grid(row=4, column=3)

# Buttons Row 5
CalcButton = customtkinter.CTkButton(app, text="=", command=Calculate, width=120, height=120, font=("Arial", 30))
CalcButton.grid(row=5, column=0)
OneButton = customtkinter.CTkButton(app, text="1", command=lambda: AddSymbol("1"), width=120, height=120, font=("Arial", 30))
OneButton.grid(row=5, column=1)
DecimalButton = customtkinter.CTkButton(app, text=".", command=lambda: AddSymbol("."), width=120, height=120, font=("Arial", 30))
DecimalButton.grid(row=5, column=2)
ExponentButton = customtkinter.CTkButton(app, text="^", command=lambda: AddSymbol("**"), width=120, height=120, font=("Arial", 30))
ExponentButton.grid(row=5, column=3)
app.mainloop()


