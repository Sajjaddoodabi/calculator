from tkinter import *

# ========================================= settings ===================================
root = Tk()

root.title("calculator")
root.geometry("400x450")
root.resizable(width=False, height=False)

color = "gray"
root.configure(bg=color)
# ========================================= variables ===================================
input_num = StringVar()
input_text = StringVar()
# ========================================= frames ======================================
topFirst = Frame(root, width=400, height=20, bg="#eee")
topFirst.pack(side=TOP)

topFirst3 = Frame(root, width=400, height=40, bg="#eee")
topFirst3.pack(side=TOP)

topSecond = Frame(root, width=125, height=800, bg=color)
topSecond.pack(side=RIGHT)

topFirst2 = Frame(root, width=275, height=60, bg=color)
topFirst2.pack(side=TOP)

topThird = Frame(root, width=400, height=60, bg=color)
topThird.pack(side=TOP)

topForth = Frame(root, width=400, height=60, bg=color)
topForth.pack(side=TOP)

topFifth = Frame(root, width=400, height=60, bg=color)
topFifth.pack(side=TOP)

topSixth = Frame(root, width=400, height=60, bg=color)
topSixth.pack(side=TOP)

# ========================================= functions ===================================
listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "."]


def errorMassage():
    pass


def click_btn(item):
    global operation, nums, isNotNum, isEqual

    if isNotNum:
        nums = ""
        isNotNum = False

    if not isEqual or item not in listNum:
        if item != 0 or nums != "":
            if item not in listNum:
                if operation[-1] not in str(listNum):
                    print("a")
                    operation = operation[:-1]
                    input_text.set(operation)

            operation = operation + str(item)
            input_text.set(operation)

            if item in listNum:
                nums = nums + str(item)

            elif item not in listNum:
                isNotNum = True

            input_num.set(nums)

            isEqual = False


def clear_btn():
    global operation, nums, isEqual, isNotNum
    operation = ""
    nums = ""
    input_text.set("")
    input_num.set("")
    isEqual = False
    isNotNum = False


def backSpace_btn():
    global operation, nums, isNotNum

    if nums != "" and not isEqual:
        nums = nums[:-1]
        operation = operation[:-1]
        input_text.set(operation)
        input_num.set(nums)


def equal_btn():
    global operation, nums, isEqual

    if nums[-1] == ".":
        nums = nums + "0"
        operation = operation + "0"

    counter = 0
    for item in listNum:
        if operation[-1] == str(item):
            counter += 1

    if counter == 0:
        result = str(eval(operation[:-1]))
    else:
        result = str(eval(operation))

    input_text.set(result)
    input_num.set(result)
    operation = result
    nums = result
    isEqual = True


def negative():
    pass


isEqual = False
isNotNum = False
operation = ""
nums = ""

# ========================================= buttons =====================================
btnDivide = Button(topSecond, font=("arial", 9, 'bold'), text="/", width=13, height=4, bg="gray",
                   command=lambda: click_btn("/"))
btnDivide.pack(side=TOP, padx=1, pady=1)

btnMultiPly = Button(topSecond, font=("arial", 9, 'bold'), text="*", width=13, height=4, bg="gray",
                     command=lambda: click_btn("*"))
btnMultiPly.pack(side=TOP, padx=1, pady=1)

btnMinus = Button(topSecond, font=("arial", 9, 'bold'), text="-", width=13, height=4, bg="gray",
                  command=lambda: click_btn("-"))
btnMinus.pack(side=TOP, padx=1, pady=1)

btnPlus = Button(topSecond, font=("arial", 9, 'bold'), text="+", width=13, height=4, bg="gray",
                 command=lambda: click_btn("+"))
btnPlus.pack(side=TOP, padx=1, pady=1)

btnEqual = Button(topSecond, font=("arial", 9, 'bold'), text="=", width=13, height=4, bg="cyan",
                  command=lambda: equal_btn())
btnEqual.pack(side=TOP, padx=1, pady=1)

btnOne = Button(topFirst2, font=("arial", 9, 'bold'), text="c", width=28, height=4, bg="gray",
                command=lambda: clear_btn())
btnOne.pack(side=LEFT, padx=1, pady=1)

btnOne = Button(topFirst2, font=("arial", 9, 'bold'), text="<=", width=13, height=4, bg="gray",
                command=lambda: backSpace_btn())
btnOne.pack(side=LEFT, padx=1, pady = 1)

btnOne = Button(topThird, font=("arial", 9, 'bold'), text="1", width=13, height=4, bg="gray",
                command=lambda: click_btn(1))
btnOne.pack(side=LEFT, padx=1, pady=1)

btnTwo = Button(topThird, font=("arial", 9, 'bold'), text="2", width=13, height=4, bg="gray",
                command=lambda: click_btn(2))
btnTwo.pack(side=LEFT, padx=1, pady=1)

btnThree = Button(topThird, font=("arial", 9, 'bold'), text="3", width=13, height=4, bg="gray",
                  command=lambda: click_btn(3))
btnThree.pack(side=LEFT, padx=1, pady=1)

btnFour = Button(topForth, font=("arial", 9, 'bold'), text="4", width=13, height=4, bg="gray",
                 command=lambda: click_btn(4))
btnFour.pack(side=LEFT, padx=1, pady=1)

btnFive = Button(topForth, font=("arial", 9, 'bold'), text="5", width=13, height=4, bg="gray",
                 command=lambda: click_btn(5))
btnFive.pack(side=LEFT, padx=1, pady=1)

btnSix = Button(topForth, font=("arial", 9, 'bold'), text="6", width=13, height=4, bg="gray",
                command=lambda: click_btn(6))
btnSix.pack(side=LEFT, padx=1, pady=1)

btnSeven = Button(topFifth, font=("arial", 9, 'bold'), text="7", width=13, height=4, bg="gray",
                  command=lambda: click_btn(7))
btnSeven.pack(side=LEFT, padx=1, pady=1)

btnEight = Button(topFifth, font=("arial", 9, 'bold'), text="8", width=13, height=4, bg="gray",
                  command=lambda: click_btn(8))
btnEight.pack(side=LEFT, padx=1, pady=1)

btnNine = Button(topFifth, font=("arial", 9, 'bold'), text="9", width=13, height=4, bg="gray",
                 command=lambda: click_btn(9))
btnNine.pack(side=LEFT, padx=1, pady=1)

btnNegative = Button(topSixth, font=("arial", 9, 'bold'), text="+/-", width=13, height=4, bg="gray",
                     command=lambda: negative())
btnNegative.pack(side=LEFT, padx=1, pady=1)

btnZero = Button(topSixth, font=("arial", 9, 'bold'), text="0", width=13, height=4, bg="gray",
                 command=lambda: click_btn(0))
btnZero.pack(side=LEFT, padx=1, pady=1)

btnDot = Button(topSixth, font=("arial", 9, 'bold'), text=".", width=13, height=4, bg="gray",
                command=lambda: click_btn("."))
btnDot.pack(side=LEFT, padx=1, pady=1)
# ========================================= Entries =====================================
operation_label = Label(topFirst, textvariable=input_text, width=60)
operation_label.pack(ipady=1)

input_field = Entry(topFirst3, font=('arial', 23, 'bold'), text=input_num, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=20)

root.mainloop()
