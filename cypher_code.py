# Cypher code messager.
# Leonardo L. Rapanan
# Final Project.
from tkinter import messagebox, simpledialog, Tk
# function to divide total number in message.
def is_even(number):
    return number % 2 == 0
# function to get even letters in the alphabet.
def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters
# function to get odd letters in the alphabete.
def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters
# function to swap the letters of user typing the message.
def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message
# function for user input on message to encrypt or decrypt message.
def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task
# function to enter encrypt message or decrypt message.
def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message
# tkinter main program.
root = Tk()
# while loop to restart program after user either encrypts or decrypts message.
while True:
    # function of task for user to choose to encrypt or decrypt message.
    task = get_task()
    # if/else statement when user chooses encrypt for window to pop up.
    if task == 'encrypt':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
    # if/else statement when user chooses decrypt for window to pop up.   
    elif task == 'decrypt':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('Plaintext of the secret message is:', decrypted)
    else:
        break
root.mainloop()

    
