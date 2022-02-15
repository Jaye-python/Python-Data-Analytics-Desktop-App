import tkinter as tk
from tkinter import LabelFrame
import pandas as pd
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.constants import END
from datetime import date
import matplotlib.pyplot as plt
import io

ff = ('arial', 8)

mbg = '#484a49'

root = tk.Tk()
root.title(' Free Basic Data Analytics App by WebX Consulting')
# root.iconbitmap('favicon.ico')
root.geometry('1000x600')
root.configure(background=mbg)

fm = LabelFrame(root, bg='white',  )
fm.place(relx=0, rely=0.875, relwidth=1, )
# ima=ImageTk.PhotoImage(Image.open('log.png'))
# label = tk.Label(master=fm, image=ima, bg='white')
# label.grid(column=0, row=0,)
label2 = tk.Label(master=fm, text='We develop Python-based desktop and web apps. Email: contact@sellgence.xyz\n', bg='white')
label2.grid(column=3, row=1)
la = tk.Label(master=fm, text='www.sellgence.xyz', bg='white', font=('helvetica', 30))
la.grid(column=3, row=0,)


def ex():
    root.destroy()


def op():
    mtext.set(value='Loading...')
    file = askopenfilename(parent=root, title='Choose a file', filetypes=[('Excel file', '*.xlsx'), ('CSV file', '*.csv')] )
    
    if file.endswith('csv'):
        global d
        d = pd.read_csv(file)
    elif file.endswith('xlsx'):
        d = pd.read_excel(file)
    
    global ed
    ed = d
    
    # lbl['text'] ='Data has ' + str(len(d)) + ' rows'
    extext.set(value= str(len(d)) + '\nrows')
    e.delete(1.0, END)
    e.insert(1.0, d)
    # d.to_csv('eee.csv')
    mtext.set(value='Imported\n\n(Click to\nimport\nnew table)')

def op2():
    ntext.set(value='Loading...') 
    file = askopenfilename(parent=root, title='Choose a file', filetypes=[('Excel file', '*.xlsx'), ('CSV file', '*.csv')] )
    if file.endswith('csv'):
        global d2
        d2 = pd.read_csv(file)
    elif file.endswith('xlsx'):
        d2 = pd.read_excel(file)
    
        
    # lbl['text'] ='Data has ' + str(len(d)) + ' rows'
    extext.set(value= str(len(d2)) + '\nrows')
    e.delete(1.0, END)
    e.insert(1.0, d2)
    # d.to_csv('eee.csv')
    ntext.set(value='Imported\n\n(Click to\nimport\nnew table)')


def dropnull():

    global ed
    try:
        ed = ed.dropna(how='any')
        extext.set(value= 'Export ' + str(len(ed)) + '\nrows')
        e.delete(1.0, END)
        e.insert(1.0, ed)
        dntext.set(value='Null Dropped')
        messagebox.showinfo(' Null Dropped', 'Null values dropped')
    except:
        messagebox.showinfo(' File not imported', 'Please import file')


def filter():
    head = filter_heading.get()
    filt = filter_entry.get()

    if head and filt:

        global fd
        # ed = d[d[head] == filt]

        global ed
        # ed = d[d[head] == filt]

        fd = ed[ed[head].astype(str).str.contains(str(filt) )== True]

        extext.set(value= 'Export\n' + str(len(ed)) + '\nrows')
        e.delete(1.0, END)
        e.insert(1.0, fd)
    else:
        messagebox.showinfo('Info required', 'Please indicate column name and text to be filtered')


def exportfilter():
    global fd

    p = 'Filtered_List_' + str(date.today())+'.csv'
    file = asksaveasfilename(confirmoverwrite=True, defaultextension='.csv', filetypes=[('CSV file', '*.csv')], initialfile= p,) 
    
    try:
        fd.to_csv(file)
        messagebox.showinfo('Saved', 'Saved')
    except:
        messagebox.showinfo('Not Saved', 'Not saved. File may be open. Please rename and resave')



def look():
    try:
        head = filter_heading.get()
        filt = filter_entry.get()

        global d2
        global ed

        p = ed[ed[head]== filt]

        ed = pd.merge(p, d2, on= head)
        
            
        extext.set(value= 'Export\n' + str(len(ed)) + '\nrows')
        e.delete(1.0, END)
        e.insert(1.0, ed)
    except:
        messagebox.showinfo('Imports Required', 'Please import Table 1 and 2 then indicate common column name and record to Vlook up')


def currdata():
    global ed
    try:
        e.delete(1.0, END)
        e.insert(1.0, ed)
    except:
        messagebox.showinfo('Import Required', 'Please import Table 1 to see its records')


def seconddata():
    global d2
    try:
        e.delete(1.0, END)
        e.insert(1.0, d2)
    except:
        messagebox.showinfo('Import Required', 'Please import Table 2 to see its records')


def export():
    
    p = 'Export_List_' + str(date.today())+'.csv'
    file = asksaveasfilename(confirmoverwrite=True, defaultextension='.csv', filetypes=[('CSV file', '*.csv')], initialfile= p,) 
    global ed
    try:
        ed.to_csv(file)
        messagebox.showinfo('Saved', 'Saved')
    except:
        messagebox.showinfo('Not Saved', 'Not saved. File may be open. Please rename and resave')


def exportcount():
    global eed

    p = 'Count_List_' + str(date.today())+'.csv'
    file = asksaveasfilename(confirmoverwrite=True, defaultextension='.csv', filetypes=[('CSV file', '*.csv')], initialfile= p,) 
    
    try:
        eed.to_csv(file)
        messagebox.showinfo('Saved', 'Saved')
    except:
        messagebox.showinfo('Not Saved', 'Not saved. File may be open. Please rename and resave')


def count():
    head = filter_heading.get()

    global d
    global ed
    global eed

    try:

        eed = ed[head].value_counts(ascending=False)
        # d['No-show'].groupby(d['SUB Category']).value_counts(normalize=True)
        # df.groupby('gender')['salary'].transform('count')
        
        # extext.set(value= 'Export\n' + str(len(ed)) + '\nrows')
        e.delete(1.0, END)
        e.insert(1.0, eed)
        eed.nlargest(10).plot(kind='barh', color=['cyan'], edgecolor='purple')
        # de = np.random.normal(200000, 25000, 5000)
        plt.title('Count of '+head)
        plt.xlabel('Count')
        plt.ylabel(head)
        plt.show()
    except:
        messagebox.showinfo('Info required', 'Please import Table 1 and indicate name of column to be counted')


def dup():
    head = filter_heading.get()

    global d
    global ed

    try:
        ed = ed.drop_duplicates(subset=[head],)
        
        extext.set(value= 'Export\n' + str(len(ed)) + '\nrows')
        e.delete(1.0, END)
        e.insert(1.0, ed)
        ddtext.set(value='Duplicates Dropped')
        messagebox.showinfo(' Duplicates Dropped', 'Duplicate values dropped')
    except:
        messagebox.showinfo('Info required', 'Please import Table 1 and indicate name of column having duplicate records')


def describe():
    
    global ed
    # global ed

    try:
        d = ed.describe()
        # extext.set(value= 'Export\n' + str(len(d)) + '\nrows')
        e.delete(1.0, END)
        e.insert(1.0, d)
    except:
        messagebox.showinfo('Table 1 Not Imported', 'Please import Table 1 to view its five number summary')


def info():
    
    global ed
    

    try:
        
        buffer = io.StringIO()
        ed.info(buf=buffer)
        s = buffer.getvalue()
        
        # ed = pd.DataFrame(s)
        # with open("df_info.txt", "w", encoding="utf-8") as f:
        #     f.write(s)
        
        e.delete(1.0, END)
        e.insert(1.0, s)
    except:
        messagebox.showinfo('Table 1 Not Imported', 'Please import Table 1 to view its info')

bg = '#545655'
fg = 'white'

# SELECT Table 1
mtext = tk.StringVar(master=root,)
mtext.set(value='Import\nTable 1')
btn = tk.Button(root, textvariable=mtext, command=op, bg='purple', fg='yellow' )
btn.place(relheight=0.15, relwidth=0.1, relx=0.05, rely=0.03)

# SELECT 2ND FILE
ntext = tk.StringVar(master=root,)
ntext.set(value='Import\nTable 2\n\n(Only\nrequired For\nVlookup)')
btn = tk.Button(root, textvariable=ntext, command=op2, bg='#318ce7', fg='white' )
btn.place(relheight=0.15, relwidth=0.1, relx=0.05, rely=0.2)

# BACK TO TABLE 1
btntt = tk.Button(root, text='Back to Table 1', command=currdata, bg= '#1c1c1c', fg = 'yellow' )
btntt.place(relheight=0.055, relwidth=0.1, relx=0.05, rely=0.368)

# BACK TO TABLE 2
btnsf = tk.Button(root, text='Back to Table 2', command=seconddata, bg= '#1c1c1c', fg = 'yellow' )
btnsf.place(relheight=0.055, relwidth=0.1, relx=0.05, rely=0.43)


width = 0.09
relx = 0.05668
relheight = 0.03
# bg = '#545655'
# fg = 'white'

# FIVE NUMBER SUMMARY
btncount = tk.Button(root, text='Describe Table 1', command=describe, bg=bg, fg=fg)
btncount.place(relx=0.05, rely=0.52, relwidth= 0.1, relheight= 0.055)

# EXPORT
extext = tk.StringVar(master=root, )
extext.set(value='No Data\nto Export')
export_btn = tk.Button(root, textvariable=extext, command=export, bg= '#1c1c1c', fg = 'yellow' )
# export_btn.place(relheight=0.14, relwidth=0.1, relx=0.05, rely=0.53)
export_btn.place(relheight=0.08, relwidth=0.1, relx=0.05, rely=0.608)

# EXIT
exit_btn = tk.Button(root, text='Exit', command=ex, fg='white', bg='red' )
exit_btn.place(relheight=0.1, relwidth=0.1, relx=0.05, rely=0.7)

# FRAME START
fr = LabelFrame(master=root, bg= mbg, )

# fr = LabelFrame(master=root, bg='#222222', )
fr.place(relx=0.219, rely=0.03, relwidth=0.4, relheight=0.152)

# FILTER HEADING
filter_heading = tk.Entry(root,)
filter_heading.place(relx=0.225, rely=0.04, relwidth=0.23, relheight=0.05)

# COLUMN HEADER
# lbl = tk.Label(root, text='Column\nHeader', bg='#add8e6' )
# lbl.place(relx=0.48, rely=0.04, )



# FILTER TEXT
filter_entry = tk.Entry(root,)
filter_entry.place(relx=0.225, rely=0.116, relwidth=0.2, relheight=0.05)

# COLUMN HEADER
C_btn = tk.Button(root, text='Table 1 Info', command=info, bg=bg, fg=fg)
C_btn.place(relx=0.48, rely=0.04, relwidth=0.13, relheight=0.05)

# FILTER BUTTON
btnfilter = tk.Button(root, text='Filter (Table 1)', command=filter, bg='#1c1c1c', fg=fg )
btnfilter.place(relx=0.48, rely=0.116, relwidth=0.08, relheight=0.05)

# EXPORT FILTER BUTTON
btnefilter = tk.Button(root, text='Export', command=exportfilter, bg='#1c1c1c', fg=fg )
btnefilter.place(relx=0.56, rely=0.116, relwidth=0.0485, relheight=0.05)

# REMOVE DUPLICATES
ddtext = tk.StringVar(master=root,)
ddtext.set(value='Drop Duplicates (Table 1)')
btncount = tk.Button(root, textvariable=ddtext, command=dup, bg=bg, fg=fg)
btncount.place(relx=0.63, rely=0.04, relwidth=0.18, relheight=0.05)

# DROP NULL
dntext = tk.StringVar(master=root,)
dntext.set(value='Drop Null (Table 1)')
btnnull = tk.Button(root, textvariable=dntext, command=dropnull, bg= bg, fg= fg)
btnnull.place(relx=0.82, rely=0.04, relwidth=0.11, relheight=0.05)
# ddbtn.place(relheight=relheight, relwidth=width, relx=relx, rely=0.568)

# COUNT
btncount = tk.Button(root, text='Count Column (Table 1)', command=count, bg='#1c1c1c', fg=fg)
btncount.place(relx=0.63, rely=0.116, relwidth=0.131, relheight=0.05)

# EXPORT COUNT
btnexcount = tk.Button(root, text='Export', command=exportcount, bg='#1c1c1c', fg=fg)
btnexcount.place(relx=0.761, rely=0.116, relwidth=0.048, relheight=0.05)

# LOOKUP
btncount = tk.Button(root, text='VLookup', command=look, bg='#318ce7', fg='white')
btncount.place(relx=0.82, rely=0.116, relwidth=0.11, relheight=0.05)


# FRAME END

# BODY
y = LabelFrame(root, text='Output', bg=mbg, fg='yellow')
y.place(relheight=0.61, relwidth=0.71, relx=0.219, rely=0.194,)
e = tk.Text(y,  )
e.place(relheight=0.96, relwidth=0.96, relx=0.02, rely=0.02,)


  

root.mainloop()
