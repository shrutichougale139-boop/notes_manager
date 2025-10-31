import datetime
from functools import reduce

def log_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"🗓️ [{datetime.datetime.now().strftime('%H:%M:%S')}] {func.__name__.capitalize()} executed.")
        return result
    return wrapper

notes = []

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created = datetime.date.today()
    def __str__(self):
        return f"{self.title} - {self.content[:30]}..."

@log_action
def add_note(title, content):
    notes.append(Note(title, content))
    print(f"✅ Note added: {title}")

@log_action
def delete_note(title):
    global notes
    notes = [n for n in notes if n.title != title]
    print(f"🗑️ Note deleted: {title}")

def show_notes():
    if not notes: return print("📭 No notes yet.")
    print("\n📝 All Notes:")
    [print(f" - {n.title} ({n.created})") for n in notes]

def find_notes(keyword):
    def match(note): return keyword.lower() in note.title.lower() or keyword.lower() in note.content.lower()
    result = list(filter(match, notes))
    if result:
        print(f"\n🔍 Found {len(result)} note(s):")
        [print(f" - {n.title}") for n in result]
    else: print("❌ No match found.")

def note_stats():
    if not notes: return print("📉 No stats available.")
    word_counts = list(map(lambda n: len(n.content.split()), notes))
    total_words = reduce(lambda a, b: a + b, word_counts)
    print(f"\n📊 Notes: {len(notes)} | Words: {total_words} | Avg: {total_words/len(notes):.1f}")
    countdown(3)

def countdown(n):
    if n <= 0: return print("💾 Notes saved successfully!")
    print(f"Saving in {n}..."); countdown(n - 1)

def bulk_add(*titles, **contents):
    for title, text in zip(titles, contents.values()):
        add_note(title, text)

if __name__ == "__main__":
    add_note("Python Decorators", "Decorators allow modifying functions easily.")
    add_note("Lambda and Map", "Use lambda with map/filter to simplify loops.")
    show_notes()
    find_notes("lambda")
    bulk_add("Todo", "Reminder", note1="Check mails", note2="Push to GitHub")
    note_stats()
    delete_note("Todo")
    show_notes()
