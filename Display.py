# -*- coding: utf-8 -*-

# Must do for compatibility win <> lnx
try:
    import Tkinter as tk
    print('using big tkinter (linux way)')
except ImportError:
    import tkinter as tk
    print('using small tkinter (windows way)')
    
# Contact list constructor
from Contact import ContactList


# Main logic and layout
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.active_sel = ''
        self.curr_loc = directory
        self.mode = tk.IntVar(value=0)
        self.contacts_lib = ''
        
        # ===================== (Main Menu + controls)
        self.current_location = tk.Label(self.master, text='Location : {0}'.format(directory))
        self.radio1 = tk.Radiobutton(self.master, text='Single file', value=False, variable=self.mode.get(), command=self.refresh)
        self.radio2 = tk.Radiobutton(self.master, text='Folder', value=True, variable=self.mode.get(), command=self.refresh)
        
        self.current_location.grid(row=0, column=0, sticky='w')
        self.radio1.grid(row=0, column=2)
        self.radio2.grid(row=0, column=3)
        
        # ===================== (Button Menu)
        self.btn_open = tk.Button(self.master, text='open', command=self.on_select)
        self.btn_prev = tk.Button(self.master, text='<')
        self.btn_save = tk.Button(self.master, text='save')
        self.btn_next = tk.Button(self.master, text='>')
        self.btn_exit = tk.Button(self.master, text='save')
        
        self.btn_open.grid(row=1, column=0)
        self.btn_prev.grid(row=1, column=1)
        self.btn_save.grid(row=1, column=2)
        self.btn_next.grid(row=1, column=3)
        
        # ===================== (Contacts list)
        self.contacts_list = tk.Listbox(self.master, height=7)
        self.contacts_list.bind('<<ListboxSelect>>', self.on_select)
        self.contacts_scroll = tk.Scrollbar(self.master, orient='vertical')
        
        self.contacts_list['yscrollcommand'] = self.contacts_scroll.set
        self.contacts_scroll['command'] = self.contacts_list.yview
        
        self.contacts_list.grid(row=2, column=0, rowspan=8, columnspan=1, sticky='nse', pady=(3, 3), padx=(3, 3))
        self.contacts_scroll.grid(row=2, column=0, rowspan=8, columnspan=1, sticky='nse', pady=(5, 5), padx=(5, 5))
        
        # ===================== (Fields list)
        
        self.f1_lab = tk.Label(self.master, text='Jmeno')
        self.f1_inp = tk.Label(self.master, text='Jmeno')
        
        se
        
        # TODO: 1. Switcher between folder and file mode still not working
        # TODO: 2. Field list 
        # TODO: 3. Exporting / Merging
        
        self.refresh()  # list widgets

    def browse_dir(self):
        if self.mode:
            vcf = tk.filedialog.askdirectory()
            print('setting directory to', vcf)
            #self.contacts_lib = ContactList(vcf, is_dir=True)
        else:
            vcf = tk.filedialog.askopenfilename()
            print('opening a file', vcf)
            # self.contacts_lib = ContactList(vcf)

    def refresh(self):
        self.contacts_list.delete(0, 'end') # refreshing whole layout
        print('selected option', self.mode, 'really?')
        if self.mode:
            self.contacts_lib = ContactList(self.curr_loc, is_dir=True)
            for c_file in self.contacts_lib.dic.keys():
                self.contacts_list.insert('end', c_file)
        else:
            self.contacts_lib = ContactList(self.curr_loc)
            # cycle library
        self.current_location['text'] = 'Location : {0}'.format(self.curr_loc)            
                 
    def on_select(self, evt):
        w = evt.widget
        if w == self.contacts_list:  # click in contact list
            if w.curselection():
                index = int(w.curselection()[0])
                self.active_sel = w.get(index)
                
        elif w == self.radio1:
            print('file reading mode')
            self.mode = False
        elif w == self.radio2:
            print('folder reading mode')
            self.mode = True        
        self.refresh()          


    
def contacts_editor():
    root = tk.Tk()

    root.title('Editor VCF kontaktu')
    root.resizable(10, 10)
    # root.geometry('1200x900')

    global directory
    # directory = os.getcwd()
    directory = 'C:\\Users\\jirib\\Downloads\\SD_samci\\work'
    print('using directory', directory)

    MainWindow(root)  # .pack(side="top", fill="both", expand=True)
    root.mainloop()

    
if __name__ == '__main__':
    contacts_editor()