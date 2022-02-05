import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from tkinter.scrolledtext import ScrolledText
from time import strftime

todos = {}

def detailTodo(cb=None):
    win = tk.Toplevel()
    win.wm_title('Detail kegiatan')
    selectedItem = treev.focus()
    selectedIndex = treev.item(selectedItem)['text'] #text adalah index dari kegiatan yang kita simpan
    selectedTodo = todos[tanggal][selectedIndex]
    judul = tk.StringVar(value=selectedTodo['judul'])
    tk.Label(win, text='Tanggal:').grid(row=0, column=0, sticky='N')
    tk.Label(win, text='{} | {}'.format(tanggal, selectedTodo['waktu'])).grid(row=0, column=1, sticky='E')
    tk.Label(win, text='Judul:').grid(row=1, column=0, sticky='N')
    tk.Entry(win, state='disabled', textvariable=judul).grid(row=1, column=1, sticky='E')
    tk.Label(win, text='Keterangan:').grid(row=2, column=0, sticky='N')
    keterangan = ScrolledText(win, width=12, height=5)
    keterangan.grid(row=2, column=1, sticky='E')
    keterangan.insert(tk.INSERT, selectedTodo['keterangan'])
    keterangan.configure(state='disabled')    

def saveTodo():
    f = open('MyTodo.txt','w')
    f.write(str(todos))
    f.close()

def loadTodo():
    global todos
    f = open('MyTodo.txt','r')
    data = f.read()
    f.close()
    todos = eval(data) #dengan eval, data yang string diterjemahkan menjadi dict
    ListTodo()
    

def delTodo():
    tanggal = str(cal.selection_get())
    selectedItem = treev.focus() #akan mendapatkan index dari item yang diklik di treeview
    todos[tanggal].pop(treev.item(selectedItem)['text'])
    ListTodo()
#pop berguna untuk menghapus item
    
def ListTodo(cb=None):
    for i in treev.get_children():
        treev.delete(i)
    tanggal = str(cal.selection_get())
    if tanggal in todos:
        for i in range(len(todos[tanggal])):
            treev.insert('','end', text=i, values=(todos[tanggal][i]['waktu'], todos[tanggal][i]['judul']))


def addTodo(win, key, jam, menit, judul, keterangan):
    newTodo = {
        'waktu':'{}:{}'.format(jam.get(), menit.get()),
        'judul': judul.get(),
        'keterangan': keterangan.get('1.0', tk.END) #mengambil keterangan dari line pertama sampai line terakhir
    }
    if key in todos:
        todos[key].append(newTodo)
    else:
        todos[key] = [newTodo]
    win.destroy()
    ListTodo()

def AddForm():
    win = tk.Toplevel()
    win.wm_title('+')
    jam = tk.IntVar(value=10) #Jam merupakan integer
    menit = tk.IntVar(value=30)
    judul = tk.StringVar(value='')
    tk.Label(win, text='Waktu: ').grid(row=0, column=0)
    tk.Spinbox(win, from_=0, to=23, textvariable=jam, width=3).grid(row=0, column=1)
    tk.Spinbox(win, from_=0, to=59, textvariable=jam, width=3).grid(row=0, column=2)
    tk.Label(win, text='Judul: ').grid(row=1, column=0)
    tk.Entry(win, textvariable=judul).grid(row=1, column=1, columnspan=2)
    tk.Label(win, text='Keterengan').grid(row=2, column=0)
    keterangan = ScrolledText(win, width=12, height=5)
    keterangan.grid(row=2, column=1, columnspan=2, rowspan=4)
    tanggal = str(cal.selection_get())
    tk.Button(win, text='Tambah', command=lambda: addTodo(win, tanggal, jam, menit, judul, keterangan)).grid(row=6, column=0)


def title():
    waktu = strftime('%H:%M')
    tanggal = str(cal.selection_get())
    root.title(tanggal + ' | ' + waktu + ' | Kalenderku')
    root.after(250,title)

root = tk.Tk()
root.title("Kalenderku")
style = ttk.Style(root)
style.configure('Treeview', rowheight=16)
style.theme_use("clam")
style.configure("Treeview", fieldbackground="black")


cal = Calendar(root, font='Arial 14', selectmode='day', locale='en_US', cursor='hand2',
               background='black', disabledbackground='black', bordercolor='black',
               headersbackground='black', normalbackground='black', foreground='white',
               normalforeground='red', headersforeground='yellow')
cal.grid(row=0, column=0, sticky='N', rowspan=7)
cal.bind('<<CalendarSelected>>', ListTodo) #Jika memilih tanggal yang berbeda, akan memanggil ListTodo

tanggal = str(cal.selection_get())

treev = ttk.Treeview(root)
treev.grid(row=0, column=1, sticky='WNE', rowspan=4, columnspan=2)
scrollBar = tk.Scrollbar(root, orient='vertical', command=treev.yview)
#artinya, scrollbar yang dibuat disini berfyungsi untuk mengatur posisi y (vertikal)
#atau atas bawah, seperti sb.y pada diagram kartesius
scrollBar.grid(row=0, column=3, sticky='ENS', rowspan=4)
#ens untuk memposisikan di pojok kanan dan ada di treeview

treev.configure(yscrollcommand=scrollBar.set)
treev.bind('<Double-1>', detailTodo) #membinding tombol klik kiri sebanyak 2 kali (double klik) dan memanggil detail todo
treev['columns'] = ('1', '2')
treev['show'] = 'headings'
treev.column('1', width=100)
treev.heading('1', text='JAM')
treev.heading('2', text='Judul')


#Adding button
btnAdd = tk.Button(root, font='Times 10', text='Tambah', width=20, command=AddForm)
btnAdd.grid(row=4, column=1, sticky='N')

btnDel = tk.Button(root, font='Times 10', text='Hapus', width=20, command=delTodo)
btnDel.grid(row=4, column=2, sticky='N')

btnLoad = tk.Button(root, font='Times 10', text='Load', width=20, command=loadTodo)
btnLoad.grid(row=6, column=1, sticky='S')

btnSave = tk.Button(root, font='Times 10', text='Save', width=20, command=saveTodo)
btnSave.grid(row=6, column=2, sticky='S')



title()
root.mainloop()
