import tkinter as tk


####################################
# DEFINE FUNCTIONS
####################################

def menu_switch(frame_from, frame_to):
    frame_from.pack_forget()
    frame_to.pack(expand=True)

# TODO - create function that disables completed objective when checkbox selected

# TODO - find a way to make check list left-aligned

# TODO - update other two frames to match changes made to fitness



def make_textbox(box, button):
    box.grid(
        row=3,
        column=1
    )
    button.grid(
        row=4,
        column=1
    )


def make_checkbox(textbox, frame):
    i = tk.IntVar()
    list_item = textbox.get("1.0", 'end-1c')
    new_entry = tk.Checkbutton(
        master=frame,
        text=list_item,
        variable=i,
        fg="blue4",
        activeforeground="blue",
        cursor="hand2",
        disabledforeground="SpringGreen2"
    )
    textbox.delete("1.0", "end")
    new_entry.pack()  # 'frame' parameter should hold only checkboxes.


# main window instance
window = tk.Tk()
window.geometry("500x500")
window.title("Progress Tracker")
# window.configure(bg="turquoise")

####################################
# Load images
####################################
# back_button_icon = PhotoImage(file=)
back_button_icon_large = tk.PhotoImage(file="C:\\Users\\Gillie\\PycharmProjects\\team\\back_button_image.png")
back_button_icon = back_button_icon_large.subsample(20, 20)

add_button_large = tk.PhotoImage(file="C:\\Users\\Gillie\\PycharmProjects\\team\\—Pngtree—vector plus icon_3989579.png")
add_button_icon = add_button_large.subsample(15, 15)
####################################
# DEFINE MAIN FRAMES
####################################

# frame containing buttons which navigate to
# the fitness tracker, productivity tracker, and
# time management tools
main_menu = tk.Frame(
    master=window
)

# main fitness frame
fit_frame = tk.Frame(
    master=window
)

# main productivity frame
product_frame = tk.Frame(
    master=window
)

# main time management frame
time_frame = tk.Frame(
    master=window
)

####################################
# home menu
####################################

# fitness menu button
fitness_select = tk.Button(
    master=main_menu,
    relief=tk.FLAT,
    text="Fitness Tracker",
    height=3,
    width=20,
    borderwidth=2,
    command=lambda: menu_switch(main_menu, fit_frame),
    highlightbackground="turquoise4",
    bg="turquoise",
    activebackground="turquoise3",
    cursor="hand2"
)

# productivity menu button
product_select = tk.Button(
    master=main_menu,
    relief=tk.FLAT,
    text="Productivity Tracker",
    height=3,
    width=20,
    borderwidth=2,
    command=lambda: menu_switch(main_menu, product_frame),
    highlightbackground="turquoise4",
    bg="turquoise",
    activebackground="turquoise3",
    cursor="hand2"
)

# time management menu button
time_select = tk.Button(
    master=main_menu,
    relief=tk.FLAT,
    text="Time Management",
    height=3,
    width=20,
    borderwidth=2,
    command=lambda: menu_switch(main_menu, time_frame),
    highlightbackground="turquoise4",
    bg="turquoise",
    activebackground="turquoise3",
    cursor="hand2"
)

# pack elements of main menu frame
fitness_select.grid(
    row=0,
    column=0,
    pady=5
)

product_select.grid(
    row=1,
    column=0,
)

time_select.grid(
    row=2,
    column=0,
    pady=5
)

main_menu.pack(
    expand=True
)

####################################
# fitness tracker menu
####################################

# return to home menu
fitness_back = tk.Button(
    image=back_button_icon,
    relief=tk.FLAT,
    master=fit_frame,
    command=lambda: menu_switch(fit_frame, main_menu),
    cursor="hand2"
)

# add item to checklist - creates textbox for user entry
fitness_add = tk.Button(
    relief=tk.FLAT,
    master=fit_frame,
    cursor="hand2",
    image=add_button_icon,
    command=lambda: make_textbox(fitness_entry, fitness_enter)
)

# textbox for user entry
fitness_entry = tk.Text(
    master=fit_frame,
    height=1,
    width=30,
    cursor="xterm"
)
# enter button - records text from textbox, creates a checkbox with that label,
# and packs checkbox into frame containing "to-do" list
fitness_enter = tk.Button(
    text="Enter",
    cursor="hand2",
    master=fit_frame,
    command=lambda: make_checkbox(fitness_entry, fitness_list)
)

# "to-do" list for fitness menu
fitness_list = tk.Frame(
    master=fit_frame
)

# pack elements of fitness menu
fitness_back.grid(
    row=0,
    column=0
)

fitness_add.grid(
    row=2,
    column=1
)

fitness_list.grid(
    row=1,
    column=1
)

####################################
# productivity tracker menu
####################################

# return to home menu
product_back = tk.Button(
    image=back_button_icon,
    relief=tk.FLAT,
    master=product_frame,
    command=lambda: menu_switch(product_frame, main_menu),
    cursor="hand2"
)

# button to add new item to list
product_add = tk.Button(
    relief=tk.FLAT,
    master=product_frame,
    cursor="hand2",
    image=add_button_icon,
    command=lambda: make_textbox(product_entry, product_enter)
)

# 'enter' button for when text entry is complete
product_enter = tk.Button(
    text="Enter",
    cursor="hand2",
    master=product_frame
)

product_entry = tk.Text(
    master=product_frame,
    height=1,
    width=30,
    cursor="xterm"
)

# pack elements of productivity menu
product_back.grid(
    row=0,
    column=0
)

product_add.grid(
    row=1,
    column=1
)

####################################
# time management menu
####################################

# return to home menu
time_back = tk.Button(
    image=back_button_icon,
    relief=tk.FLAT,
    master=time_frame,
    command=lambda: menu_switch(time_frame, main_menu),
    cursor="hand2"
)

# plus button to add element to list
time_add = tk.Button(
    relief=tk.FLAT,
    master=time_frame,
    cursor="hand2",
    image=add_button_icon,
    command=lambda: make_textbox(time_entry, time_enter)
)

# enter button for when text entry is complete
time_enter = tk.Button(
    text="Enter",
    cursor="hand2",
    master=time_frame
)

# box for user entry
time_entry = tk.Text(
    master=time_frame,
    height=1,
    width=30,
    cursor="xterm"
)

# pack elements of time management menu
time_back.grid(
    row=0,
    column=0
)

time_add.grid(
    row=1,
    column=1
)

####################################
window.mainloop()
