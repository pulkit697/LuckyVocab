from tkinter import *


def add_server(_window, name, score):
    return Label(_window, text=name + ' (Host) : ' + str(score), padx=10, pady=5, borderwidth=2, relief="groove",
                 width=10)


def add_client(_window, name, score):
    return Label(_window, text='' + name + ':' + str(score), padx=10, pady=5, borderwidth=2, relief="groove", width=10)


def exit_button(_window):
    return Button(_window, text='EXIT GAME', bg='blue', fg='white', padx=2, pady=2,
                  activebackground='#0000ff', relief='ridge', activeforeground='#ffffff')


def response_box(_window):
    return Entry(_window, width=10, borderwidth=2, relief='groove')


def change_query(_query_label, query):
    _query_label.configure(text=query)


def show_correct_answer(_answer_label, answer):
    _answer_label.configure(text='Correct answer is: ' + answer, fg='green', font=('Helvetica', 12, 'bold'))


def hide_answer_label(_answer_label):
    _answer_label.configure(text='')


def get_answer_box(_middle_frame):
    return Label(_middle_frame)


def get_timer_box(_window):
    return Label(_window, text='10', font=('Times New Roman',10,'bold'))


window = Tk()
window.title('LuckyVocab')
# window.geometry('500x500')
window.resizable(0, 0)
window.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
left_frame = Frame(window, width=120, borderwidth=2, padx=2, pady=2, bg='blue')
left_frame.pack(side="left", fill="y")
middle_frame = Frame(window, width=120, borderwidth=2, padx=2, pady=2, bg='red')
middle_frame.pack(side="left", fill="y")
right_frame = Frame(window, width=50, borderwidth=2, padx=2, pady=2, bg='green')
right_frame.pack(side="right", fill="y")
add_server(left_frame, 'Pulkit', 55).pack()
add_client(left_frame, 'Prashant', 35).pack()
query_label = Label(middle_frame, text='_ _ _ _ _ _ _ _ _ _', padx=10, pady=10)
query_label.pack()
answer_label = get_answer_box(middle_frame)
answer_label.pack()
show_correct_answer(answer_label, 'Alligator')
timer_box = get_timer_box(right_frame).pack(side='top', anchor='ne')
response_box(right_frame).pack(side='bottom')
exit_button(left_frame).pack(side='bottom', anchor='sw')
window.mainloop()
