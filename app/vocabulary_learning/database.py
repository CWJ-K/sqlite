
entries = []


def add_entry(entry_vocabulary, entry_sentence, entry_date):
    entries.append({
        'vocabulary': entry_vocabulary,
        'sentence': entry_sentence,
        'date': entry_date
    })


def get_entries():
    for entry in entries:
        print(f"Date: {entry['date']}\n{entry['vocabulary']}\nSentence: {entry['sentence']}")