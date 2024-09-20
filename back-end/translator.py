from googletrans import Translator


def translate_text(text: str, target_lang: str = "en") -> str:
    # Initialize the translator object
    translator = Translator()

    # Try to translate the text
    try:
        translated_text = translator.translate(text, dest=target_lang)
        return f"{translated_text.text}"
    except Exception as e:
        return f"An error occurred during translation: {str(e)}"

if __name__ == '__main__':
    output = translate_text('how are you')
    print(output)