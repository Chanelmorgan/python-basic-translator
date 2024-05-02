from googletrans import Translator

def translate_text(text, source_language='auto', target_language='en'):
    translator = Translator()
    translation = translator.translate(text, src=source_language, dest=target_language)
    return translation.text

def main():
    print("Welcome to the Language Translator App!")
    while True:
        text = input("Enter the text you want to translate (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Exiting the app. Goodbye!")
            break
        target_language = input("Enter the target language (e.g., 'fr' for French, 'es' for Spanish): ")
        translated_text = translate_text(text, target_language=target_language)
        print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()
