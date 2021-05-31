from tkinter import *
import pandas

df = pandas.read_csv('evenimente.csv')

print(df)

root = Tk()

T = Text(root, height=25, width=100)

T.pack()

root.title('Evenimente')

T.insert(END, "Evenimentele din luna aceasta:" +"\n")

for i in range (0,len(df['Evenimente'])):
 T.insert(END, df["Evenimente"][i]+"\n")

 T.insert(END,"\n")


mainloop()
