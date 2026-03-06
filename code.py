import re
import sys

def highlight_keywords(text, keywords):
    pattern = r'\b(' + '|'.join(re.escape(k) for k in keywords) + r')\b'
    return re.sub(pattern, r'**\1**', text, flags=re.IGNORECASE)

def process_file(input_file, output_file, keywords):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.read()
    result = highlight_keywords(data, keywords)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python highlighter.py input.txt output.txt keyword1 keyword2")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        keywords = sys.argv[3:]
        process_file(input_file, output_file, keywords)
