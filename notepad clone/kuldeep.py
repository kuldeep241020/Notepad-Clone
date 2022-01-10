import tkinter as tk
from tkinter import ttk,font,colorchooser,filedialog,messagebox
import os
win=tk.Tk()
win.geometry('1200x800')
win.title("Notepad Clone")
win.wm_iconbitmap("icon.ico")
main_menu=tk.Menu(win) 
print(main_menu)
#for file menu_bar
file=tk.Menu(main_menu,tearoff=0)
main_menu.add_cascade(label='file',menu=file)
new_icon=tk.PhotoImage(file="D:\movies/new.png")
open_icon=tk.PhotoImage(file="D:\movies/open.png")
save_icon=tk.PhotoImage(file="D:\movies/save.png")
save_as_icon=tk.PhotoImage(file="D:\movies/save_as.png")
exit_icon=tk.PhotoImage(file="D:\movies/exit.png")
   
   
def new_file():
    url=''
    text_editor.delete(1.0,'end')
file.add_command(label='file',image=new_icon,compound=tk.LEFT,accelerator='ctrl+N',command=new_file )
def open_file(event=None):
    global url
    url = filedialog.askopenfilename( initialdir=os.getcwd(),title='select file',filetypes=(('Text File','*.txt'),('All files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,'end')
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
            return
    except:
            return  
            
    win.title(os.path.basename(url))  


file.add_command(label='open',image=open_icon,compound=tk.LEFT,accelerator='ctrl+O',command=open_file)
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
                url.close()
        else:
            url=filedialog.asksaveasfile(mode='w',defultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()        
    except:
        return        

file.add_command(label='save',image=save_icon,compound=tk.LEFT,accelerator='ctrl+S',command=save_file)
def saveas_file():
    global url
    try:
        url=filedialog.asksaveasfile(mode='w',defultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
        content2=text_editor.get(1.0,tk.END)
        url.write(content2)
        url.close() 
    except:
        return

file.add_command(label="save_as",image=save_as_icon,compound=tk.LEFT,accelerator='ctrl+sa',command=saveas_file)
def exit_func(event=None):
    global url,text_changed
    try:
        if text_chnaged:
            mbox=messagebox.askyesnocancel('warning','do you want to save the file ?')
            if mbox is True:
                if url is True :
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        win.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text file','*.txt'),('All files',"*.*")))
                    url.write(content2)
                    url.close()
                    win.destroy()
            elif mbox is False:
                win.destroy() 
        else:
            win.destroy()
    except:
        return













file.add_command(label='exit',image=exit_icon,compound=tk.LEFT,accelerator='ctrl+E',command=exit_func)
# for edit menu bar
edit=tk.Menu(main_menu,tearoff=0)
main_menu.add_cascade(label='edit',menu=edit)
copy_icon=tk.PhotoImage(file="D:\movies/copy.png")
paste_icon=tk.PhotoImage(file="D:\movies/paste.png")
cut_icon=tk.PhotoImage(file="D:\movies/cut.png")
clear_all_icon=tk.PhotoImage(file="D:\movies/clear_all.png")
find_icon=tk.PhotoImage(file="D:\movies/find.png")
edit.add_command(label='copy',image=copy_icon,compound=tk.LEFT,accelerator='ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='paste',image=paste_icon,compound=tk.LEFT,accelerator='ctrl+v',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='cut',image=cut_icon,compound=tk.LEFT,accelerator='ctrl+x',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='clear',image=clear_all_icon,compound=tk.LEFT,accelerator='ctrl+ALT+x',command=lambda:text_editor.delete(1.0,tk.END))
def find_func(event=None):
    #window inside window
    find_dialog=tk.Toplevel()
    find_dialog.geometry('450x250+500+200')
    find_dialog.title('find')
    find_dialog.resizable(0,0)
    #frame
    find_frame=ttk.LabelFrame(find_dialog,text="find/replace")
    find_frame.pack(pady=20)
    print(find_frame)
    #labels
    text_find_label=ttk.Label(find_frame,text='find')
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label=ttk.Label(find_frame,text="replace")
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
    #entry
    text=tk.StringVar()
    text2=tk.StringVar()
    find_input=ttk.Entry(find_frame,width=30,textvariable=text)
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input=ttk.Entry(find_frame,width=30,textvariable=text2)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    #button
   
    def find():
        word=text.get()
        num=text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                print(start_pos)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                print(end_pos)
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1 
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
        print(matches) 
    def replace():
        word=find_input.get()
        replace_text= text2.get() 
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)


    find_button=ttk.Button(find_frame,text='find',command=find)
    find_button.grid(row=2,column=0,padx=14,pady=4)
    replace_button=ttk.Button(find_frame,text='replace',command=replace)
    replace_button.grid(row=2,column=1,padx=14,pady=4)
    
   
edit.add_command(label='find',image=find_icon,compound=tk.LEFT,accelerator='ctrl+F',command=find_func)
# for view bar
view=tk.Menu(main_menu,tearoff=0)
main_menu.add_cascade(label='view',menu=view)
tool_bar_icon=tk.PhotoImage(file="D:\movies/tool_bar.png")
status_bar_icon=tk.PhotoImage(file="D:\movies/status_bar.png")
view.add_checkbutton(label='tool_bar',image=tool_bar_icon,onvalue=True,offvalue=0,compound=tk.LEFT,accelerator='ctrl+t')
view.add_checkbutton(label='status_bar',image=status_bar_icon,onvalue=1,offvalue=False,compound=tk.LEFT,accelerator='ctrl+s')

# for the bar
colour_theme=tk.Menu(main_menu,tearoff=0)
main_menu.add_cascade(label='theme',menu=colour_theme)
light_default_icon=tk.PhotoImage(file="D:\movies/light_default.png")
light_plus_icon=tk.PhotoImage(file="D:\movies/light_plus.png")
dark_icon=tk.PhotoImage(file="D:\movies/dark.png")
red_icon=tk.PhotoImage(file="D:\movies/red.png")
monokai_icon=tk.PhotoImage(file="D:\movies/monokai.png")
night_blue_icon=tk.PhotoImage(file="D:\movies/night_blue.png")
colour_icon=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
colour_dict={'light_default':('#000000','#ffffff'),'light_plus':('#474747','#e0e0e0'),'dark':('#c4c4c4','#2d2d2d'),'red':('#2d2d2d','ffe8e8'),'monokai':('#d3b774','#474747')
,'night_blue':('#ededed','#6b9dc2')}
theme_choice=tk.StringVar()

def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=colour_dict[chosen_theme]
    fg_color=color_tuple[0]
    bg_color=color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)

count=0
for i in colour_dict:
    colour_theme.add_radiobutton(label=i,image=colour_icon[count],compound=tk.LEFT,variable=theme_choice,command=change_theme) 
    count=count+1

# for font_theme combobox
tool_bar=ttk.Label(win)
tool_bar.pack(side=tk.TOP,fill=tk.X)
font_tuple=tk.font.families()    
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=16,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(10)
font_box.grid(row=0,column=0)
# for font_size combobox
font_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=16,textvariable=font_var,state='readonly')
font_size['values']=tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)
#for bold_button
bold_icon=tk.PhotoImage(file="D:\movies/bold.png")
bold_btn=ttk.Button(tool_bar,width=5,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

#italic_icon button 
italic_icon=tk.PhotoImage(file="D:\movies/italic.png")
italic_btn=ttk.Button(tool_bar,image=italic_icon,width=16)
italic_btn.grid(row=0,column=3,padx=5)
 #for underline_icon button
underline_icon=tk.PhotoImage(file="D:\movies/underline.png")
underline_btn=ttk.Button(tool_bar,width=16,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)
#forfont_colour button
font_color_icon=tk.PhotoImage(file="D:\movies/font_color.png")
font_color_btn=ttk.Button(tool_bar,image=font_color_icon,width=16)
font_color_btn.grid(row=0,column=5,padx=5)
# align_left button
align_left_icon=tk.PhotoImage(file="D:\movies/align_left.png")
align_left_btn=ttk.Button(tool_bar,width=16,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)
#align_center_icon
align_center_icon=tk.PhotoImage(file="D:\movies/align_center.png")
align_center_btn=ttk.Button(tool_bar,width=16,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)
#align_right_icon
align_right_icon=tk.PhotoImage(file="D:\movies/align_right.png")
align_right_btn=ttk.Button(tool_bar,width=16,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)
#for text editior
text_editor=tk.Text(win)
text_editor.config(wrap="word",relief=tk.FLAT)
text_editor.focus_set()
scrollbar=tk.Scrollbar(win)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scrollbar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scrollbar.set) 
#for ststus bar
status_bar=ttk.Label(win,text='status bar')
status_bar.pack(side=tk.BOTTOM)
current_font_family='system'
current_font_size=35

def change_font(win):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))
def change_fontsize(win):
    global current_font_size
    current_font_size=font_var.get() 
    text_editor.configure(font=(current_font_family,current_font_size))   

font_box.bind("<<ComboboxSelected>>",change_font) 
font_size.bind("<<ComboboxSelectd>>",change_fontsize) 



def change_bold():
     name=text_property=tk.font.Font(font=text_editor['font']).actual()
     print(name)

     text_property=tk.font.Font(font=text_editor['font'])
     print(text_property)
     
     if text_property.actual()['weight'] == 'normal':
          text_editor.configure(font=(current_font_family,current_font_size,'bold'))
     if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
     
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])     
    if text_property.actual()['slant'] == 'roman':
         text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
         text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_btn.configure(command=change_italic)         


bold_btn.configure(command=change_bold)  
def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])     
    if text_property.actual()['underline'] == 0:
         text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline'] == 1:
         text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_btn.configure(command=change_underline)  
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    print(color_var)
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)
def align_left():
    text_content=text_editor.get(1.0,'end') 
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')  
align_left_btn.configure(command=align_left)    

def align_center():
    text_content=text_editor.get(1.0,'end') 
    text_editor.tag_configure('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center') 
align_center_btn.configure(command=align_center) 

def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
    print(text_editor.edit_modified())
    
    
align_right_btn.configure(command=align_right)
text_changed=False
def changed(event=None):
    if text_editor.edit_modified():
        text_changed=True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        status.bar.config(text=f'characters:{characters} words:{words}')
    text_editor.edit_modified(False)


text_editor.bind('<<modified>>',changed)
win.bind("<Control-n>",new_file)
win.bind("<Control-o>",open_file)
win.bind("<Control-s>",save_file)
win.bind("<Control-Alt-s>",saveas_file)
win.bind("<Control-q>",exit_func)

  

win.config(menu=main_menu)
win.mainloop()

