from tkinter import *
from Constants import *


def add_client(_window, _name, score):
    name = ''
    if len(_name) > 10:
        for i in range(7):
            name += _name[i]
        name += '...'
    else:
        name += _name
    return Label(_window, text='' + name + ' : ' + str(score), padx=10, pady=5, borderwidth=2, relief="groove", width=10,
                 bg=PARTICIPANTS_BG_COLOR)


def exit_button(_window):
    return Button(_window, text='EXIT GAME', bg=EXIT_BUTTON_BG_COLOR, fg=EXIT_BUTTON_FG_COLOR, padx=2, pady=2,
                  activebackground=EXIT_BUTTON_BG_COLOR_ACTIVATED, relief='ridge',
                  activeforeground=EXIT_BUTTON_FG_COLOR_ACTIVATED)


def get_round_number_box(_middle_frame):
    return Label(_middle_frame, bg=ROUND_NUMBER_BG_COLOR, fg=ROUND_NUMBER_TEXT_COLOR)


def change_round_number(_round_number_box, _round_number):
    _round_number_box.configure(text='Round number:' + str(_round_number))


def response_box(_window):
    return Entry(_window, width=10, borderwidth=2, relief='groove', bg=TEXT_INPUT_RESPONSE_BG_COLOR,
                 insertbackground=TEXT_INPUT_RESPONSE_CURSOR_COLOR, fg=TEXT_INPUT_RESPONSE_FG_COLOR)


def get_query_box(_middle_frame):
    return Label(_middle_frame, text='_ _ _ _ _ _ _ _ _ _', bg=QUERY_STRING_BG_COLOR, fg=QUERY_STRING_FG_COLOR,
                 font=(QUERY_STRING_FONT, QUERY_STRING_TEXT_SIZE))


def change_query(_query_label, query):
    _query = ''
    for c in query:
        _query += c + ' '
    _query_label.configure(text=_query)


def get_answer_box(_middle_frame):
    return Label(_middle_frame, bg=CORRECT_ANSWER_BG_COLOR, fg=CORRECT_ANSWER_FG_COLOR,
                 font=(CORRECT_ANSWER_FONT, CORRECT_ANSWER_TEXT_SIZE))


def show_correct_answer(_answer_label, answer):
    _answer_label.configure(text='Correct answer is: ' + answer)


def hide_answer_label(_answer_label):
    _answer_label.configure(text='')


def get_timer_box(_window):
    return Label(_window, text='10', font=('Times New Roman', 10, 'bold'), bg=TIMER_BG_COLOR, fg=TIMER_FG_COLOR)


# START
window = Tk()
window.title('LuckyVocab')
window.resizable(0, 0)
window.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
# Defining frames
left_frame = Frame(window, borderwidth=2, padx=20, pady=20, bg=FRAME1_BG_COLOR)
left_frame.pack(side="left", fill="y")
middle_frame = Frame(window, borderwidth=2, padx=20, pady=20, bg=FRAME2_BG_COLOR)
middle_frame.pack(side="left", fill="y")
right_frame = Frame(window, borderwidth=2, padx=10, pady=20, bg=FRAME3_BG_COLOR)
right_frame.pack(side="right", fill="y")

# left frame
add_client(left_frame, 'Pulkit', 55).pack()
add_client(left_frame, 'Prashant', 35).pack()
exit_button(left_frame).pack(side='bottom', anchor='sw')

# middle frame
round_number_box = get_round_number_box(middle_frame)
round_number_box.pack(anchor='nw')
change_round_number(round_number_box, 2)
query_label = get_query_box(middle_frame)
query_label.pack(pady=20)
change_query(query_label, 'Al__ga_or')
answer_label = get_answer_box(middle_frame)
answer_label.pack()
show_correct_answer(answer_label, 'Alligator')
response_box(middle_frame).pack(side='bottom', pady=10)

# right frame
timer_box = get_timer_box(right_frame).pack(side='top', anchor='ne')

# run GUI
window.mainloop()
