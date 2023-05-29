# -*- coding: utf-8 -*-
from tkinter import*
root=Tk()

root.title("Fibonacci Series")
root.geometry("400x200")

text= Entry(root)
label_series= Label(root, text="Fibonacci series: ")
label_total= Label(root)

def Fibonacci():
    num= int(text.get())
    first_num= 0
    sec_num= 1
    sum=0
    counter= 1
    result=0
    while (counter<= num):
        label_series["text"]+= str(sum) + " "
        result=result+sum
        counter= counter+1
        first_num= sec_num
        sec_num=sum
        sum= first_num + sec_num
      
  
    label_total["text"]= "Fibonacci sum: " +str(result)
  
btn = Button(root, text="Show Fibonacci series", command= Fibonacci)
text.pack()
btn.pack()
label_series.pack()
label_total.pack()

root.mainloop()
