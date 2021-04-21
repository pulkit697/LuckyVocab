from tkinter import *
from Constants import *

def initialize_window():
    # START
    _window = Tk()
    _window.title('LuckyVocab')
    _window.resizable(0, 0)
    _window.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
    # Defining frames
    _left_frame = Frame(_window, borderwidth=2, padx=20, pady=20, bg=FRAME1_BG_COLOR)
    _left_frame.pack(side="left", fill="y")
    _middle_frame = Frame(_window, borderwidth=2, padx=20, pady=20, bg=FRAME2_BG_COLOR)
    _middle_frame.pack(side="left", fill="y")
    _right_frame = Frame(_window, borderwidth=2, padx=10, pady=20, bg=FRAME3_BG_COLOR)
    _right_frame.pack(side="right", fill="y")
    return _window,_left_frame,_middle_frame,_right_frame
def initialize_gui():
    round_number_box = get_round_number_box(middle_frame)
    query_box = get_query_box(middle_frame)
    answer_box = get_answer_box(middle_frame)
    response_box = get_response_box(middle_frame)
    timer_box = get_timer_box(right_frame)
    return round_number_box, query_box, answer_box, response_box, timer_box

def add_client(_window, _name):
    name = ''
    if len(_name) > 10:
        for i in range(7):
            name += _name[i]
        name += '...'
    else:
        name += _name
    return Label(_window, text=name,
                 padx=10, pady=5, borderwidth=2, relief="groove", width=10,
                 bg=PARTICIPANTS_BG_COLOR)
def get_exit_button(_window):
    button = Button(_window, text='EXIT GAME', bg=EXIT_BUTTON_BG_COLOR, fg=EXIT_BUTTON_FG_COLOR, padx=2, pady=2,
                  activebackground=EXIT_BUTTON_BG_COLOR_ACTIVATED, relief='ridge',
                  activeforeground=EXIT_BUTTON_FG_COLOR_ACTIVATED)
    button.pack(side='bottom', anchor='sw')
    return button
def get_round_number_box(_middle_frame):
    _box = Label(_middle_frame, bg=ROUND_NUMBER_BG_COLOR, fg=ROUND_NUMBER_TEXT_COLOR)
    _box.pack(anchor='nw')
    return _box
def change_round_number(_round_number_box, _round_number):
    _round_number_box.configure(text='Round number:' + str(_round_number))
def get_response_box(_window):
    _box = Entry(_window, width=12, borderwidth=2, relief='groove', bg=TEXT_INPUT_RESPONSE_BG_COLOR,
                 insertbackground=TEXT_INPUT_RESPONSE_CURSOR_COLOR, fg=TEXT_INPUT_RESPONSE_FG_COLOR,
                 font=(TEXT_INPUT_RESPONSE_FONT, TEXT_INPUT_RESPONSE_FONT_SIZE))
    _box.pack(side='bottom', pady=10)
    return _box
def get_query_box(_middle_frame):
    _box = Label(_middle_frame, text='_ _ _ _ _ _ _ _ _ _', bg=QUERY_STRING_BG_COLOR, fg=QUERY_STRING_FG_COLOR,
                 font=(QUERY_STRING_FONT, QUERY_STRING_TEXT_SIZE))
    _box.pack(pady=20)
    return _box
def change_query(_query_label, query):
    _query = ''
    for c in query:
        _query += c + ' '
    _query_label.configure(text=_query)
def get_answer_box(_middle_frame):
    _box = Label(_middle_frame, bg=CORRECT_ANSWER_BG_COLOR, fg=CORRECT_ANSWER_FG_COLOR,
                 font=(CORRECT_ANSWER_FONT, CORRECT_ANSWER_TEXT_SIZE))
    _box.pack()
    return _box
def show_correct_answer(_answer_label, answer):
    _answer_label.configure(text='Correct answer is: ' + answer)
def hide_answer_label(_answer_label):
    _answer_label.configure(text='')
def get_timer_box(_window):
    _box = Label(_window, text='10', font=('Times New Roman', 10, 'bold'), bg=TIMER_BG_COLOR, fg=TIMER_FG_COLOR)
    _box.pack(side='top', anchor='ne')
    return _box


# # start
# window,left_frame,middle_frame,right_frame = initialize_window()
# # left frame
# add_client(left_frame, 'Pulkit').pack()
# add_client(left_frame, 'Prashant').pack()
# get_exit_button(left_frame) <------------------- not yet

# middle frame
# round_number_box = get_round_number_box(middle_frame)
# change_round_number(round_number_box, 2) <-------- call on demand
# query_label = get_query_box(middle_frame)

# change_query(query_label, 'Al__ga_or') <----- call on demand
# answer_label = get_answer_box(middle_frame)
# show_correct_answer(answer_label, 'Alligator') <------- call on demand
# get_response_box(middle_frame)

# right frame
# timer_box = get_timer_box(right_frame)

# run GUI
window,left_frame,middle_frame,right_frame = initialize_window()
initialize_gui()
window.mainloop()
