from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
class Translator:
    def __init__(self, root):
        # Encapsulation: Keeping the Tkinter root window as an attribute
        self.root = root
        self.root.title('Translator')
        self.root.geometry("880x300")

        # Dictionary of supported languages from Google Translate
        self.languages = googletrans.LANGUAGES
        self.language_list = list(self.languages.values())

        # Encapsulation: Creating and placing widgets within the class
        # Creating the original text input Text widget
        self.original_text = Text(self.root, height=10, width=40)
        self.original_text.grid(row=0, column=0, pady=20, padx=10)

        # Creating the Translate button with a specified font and binding it to the translate_it method
        self.translate_button = Button(self.root, text="Translate!", font=("Helvetica", 24), command=self.translate_it)
        self.translate_button.grid(row=0, column=1, padx=10)

        # Creating the translated text output Text widget
        self.translated_text = Text(self.root, height=10, width=40)
        self.translated_text.grid(row=0, column=2, pady=20, padx=10)

        # Creating the original language combo box with a default value
        self.original_combo = ttk.Combobox(self.root, width=50, values=self.language_list)
        self.original_combo.current(21)
        self.original_combo.grid(row=1, column=0)

        # Creating the translated language combo box with a default value
        self.translated_combo = ttk.Combobox(self.root, width=50, values=self.language_list)
        self.translated_combo.current(26)
        self.translated_combo.grid(row=1, column=2)

        # Creating the Clear button and binding it to the clear method
        self.clear_button = Button(self.root, text="Clear", command=self.clear)
        self.clear_button.grid(row=2, column=1)

    # Polymorphism: Overriding the translate_it method in the subclass
    def translate_it(self):
        # Clear the previous translated text
        self.translated_text.delete(1.0, END)

        try:
            # Extracting language keys for both original and translated languages
            from_language_key = self._get_language_key(self.original_combo.get())
            to_language_key = self._get_language_key(self.translated_combo.get())

            # Using the TextBlob library for text translation
            words = textblob.TextBlob(self.original_text.get(1.0, END))
            words = words.translate(from_lang=from_language_key, to=to_language_key)

            # Inserting the translated text into the appropriate Text widget
            self.translated_text.insert(1.0, words)
        except Exception as e:
            # Encapsulation: Handling exceptions within the class and showing error messages
            messagebox.showerror("Translator", e)

    # Encapsulation: Private method for fetching language key
    def _get_language_key(self, language):
        return [key for key, value in self.languages.items() if value == language][0]
    # Encapsulation: Method for clearing the input and output text widgets
    def clear(self):
        self.original_text.delete(1.0, END)
        self.translated_text.delete(1.0, END)
if __name__ == "__main__":
    # Creating the Tkinter root window outside the class
    root = Tk()
    # Composition: Creating an instance of the Translator class
    translator_app = Translator(root)
    # Running the main event loop
    root.mainloop()
