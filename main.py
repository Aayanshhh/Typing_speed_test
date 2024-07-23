from tkinter import *
import random


# Dummy function to simulate fetching words from an API
def fetch_words():
    return "The quick brown fox jumps over the lazy dog " * 10


# Initialize global variables
count = 0
total = 0
timer_id = None


def start_timer(duration):
    """Start a countdown timer."""

    def countdown(time_left):
        if time_left > 0:
            timer_label.config(text=f"{time_left}s")
            global timer_id
            timer_id = wn.after(1000, countdown, time_left - 1)
        else:
            word_field.config(state='disabled')
            timer_label.config(text="0s")

    countdown(duration)


def get_words():
    """Fetch words and start the test."""
    global count, total
    count = 0
    total = 0
    word_field.config(state='normal')
    word_field.focus()
    words = fetch_words()
    word_text.delete('1.0', END)
    word_text.insert(END, words)
    start_timer(60)


def check_word(event):
    """Check if the typed word matches the displayed word."""
    global count, total
    typed_word = word_field.get().strip()
    displayed_words = word_text.get('1.0', END).strip().split()

    if typed_word == displayed_words[0]:
        count += 1
    total += 1
    displayed_words.pop(0)

    word_text.delete('1.0', END)
    word_text.insert(END, ' '.join(displayed_words))
    count_label.config(text=f'Score: {count}/{total}')
    word_field.delete(0, END)


def stop_exit():
    """Stop the timer and exit the application."""
    if timer_id is not None:
        wn.after_cancel(timer_id)
    wn.quit()


# Set up the main window
wn = Tk()
wn.title("Typing Speed Test")
wn.configure(padx=20, pady=20, bg='#2c3e50')

# Widgets
title_label = Label(wn, text="Typing Speed Test", font=('Helvetica', 24, 'bold'), bg='#2c3e50', fg='#ecf0f1')
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

timer_label = Label(wn, text="60s", font=('Helvetica', 32, 'bold'), bg='#2c3e50', fg='#e74c3c')
timer_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

word_text = Text(wn, height=5, width=50, font=('Helvetica', 14), wrap=WORD, bg='#ecf0f1', padx=10, pady=10, bd=0,
                 relief=FLAT)
word_text.insert(END, "Press 'Start' to begin typing test")
word_text.grid(row=2, column=0, columnspan=2, pady=(0, 20))

word_field = Entry(wn, font=('Helvetica', 16), state='disabled', bd=0, relief=FLAT)
word_field.grid(row=3, column=0, columnspan=2, sticky='ew', pady=(0, 20))

count_label = Label(wn, text=f'Score: {count}/{total}', font=('Helvetica', 16), bg='#2c3e50', fg='#ecf0f1')
count_label.grid(row=4, column=0, columnspan=2, pady=(0, 20))

start_btn = Button(wn, text='Start', command=get_words, bg='#27ae60', fg='#ffffff', font=('Helvetica', 14), bd=0,
                   relief=RAISED)
start_btn.grid(row=5, column=0, sticky='ew', padx=5, pady=5)

exit_btn = Button(wn, text='Exit', command=stop_exit, bg='#c0392b', fg='#ffffff', font=('Helvetica', 14), bd=0,
                  relief=RAISED)
exit_btn.grid(row=5, column=1, sticky='ew', padx=5, pady=5)

# Event binding
wn.bind('<Return>', check_word)

wn.mainloop()
