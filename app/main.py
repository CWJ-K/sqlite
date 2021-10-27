import datetime
from database import create_table, add_entry, get_entries


def prompt_new_entry():
    entry_date = datetime.date.today()
    entry_vocabulary = input('What have you learned today?  ')
    entry_sentence = input('How to use it?  ')
    add_entry(entry_date, entry_vocabulary, entry_sentence)

def view_new_entry():
    entries = get_entries()
    for entry in entries:
        print(f"Date: {entry['date']}\n{entry['vocabulary']}\nSentence: {entry['sentence']}\n")


create_table()

menu = '''
    Hello! Check your current learning progress of English Vocabulary!
    1) Add new vocabulary
    2) View the list of vocabulary
    3) Finish. See you tomorrow!

    Your turn: '''

welcome = 'Welcome to learnig English Vocabulary!'

print(welcome)

while (user_input := input(menu)) != '3':
    if user_input == '1':
        prompt_new_entry()
    elif user_input == '2':
        view_new_entry()
    else:
        print('Are you ok? You type an invalid option.')
    