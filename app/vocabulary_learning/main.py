import datetime
from database import add_entry, get_entries


def prompt_new_entry():
    entry_vocabulary = input('What have you learned today?  ')
    entry_sentence = input('How to use it?  ')
    entry_date = datetime.date.today()
    add_entry(entry_vocabulary, entry_sentence, entry_date)



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
        get_entries()
    else:
        print('Are you ok? You type an invalid option.')
    