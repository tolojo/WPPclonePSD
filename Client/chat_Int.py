import tkinter


def connectedUserInt():

    # call function when we click in the box
    def focusIn(entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tkinter.END)

    # call function when we click outside box
    def focusOut(entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)

    top = tkinter.Tk()
    top.title("Select User")

    messages_frame = tkinter.Frame(top)
    my_msg = tkinter.StringVar()  # For the messages to be sent.

    my_msg.set("Type your messages here.")
    scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
    global msg_list
    # Following will contain the messages.
    msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msg_list.pack()
    messages_frame.pack()

    placeholder = "Type your messages here."
    user = tkinter.StringVar()
    entry_field = tkinter.Entry(top, textvariable=user)
    entry_field.bind("<FocusIn>", lambda e: focusIn(entry_field, placeholder))
    entry_field.bind("<FocusOut>", lambda e: focusOut(entry_field, placeholder))
    entry_field.pack()

    connectButton = tkinter.Button(top, text="connect", command=(lambda: connect(user.get())))
    connectButton.pack()

    top.mainloop()