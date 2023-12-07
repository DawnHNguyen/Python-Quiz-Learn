from docx import Document

def extract_qa_pairs(doc_path):
    doc = Document(doc_path)
    qa_pairs = []
    current_question_block = ''
    current_answer = ''
    capturing_question = False

    for para in doc.paragraphs:
        if para.text.startswith('Câu'):
            if capturing_question:
                qa_pairs.append(f'{current_question_block}-----{current_answer.strip()}\n\n\n')
            current_question_block = para.text
            current_answer = ''
            capturing_question = True
        elif capturing_question:
            current_question_block += '\n' + para.text
            for run in para.runs:
                # If your answer is underline/bold, change if needed
                if run.bold:
                    current_answer += run.text

    if capturing_question:
        qa_pairs.append(f'{current_question_block}-----{current_answer.strip()}\n\n\n')

    return ''.join(qa_pairs)

# Path to your .docx file
doc_path = 'Your-file.docx'

# Extract Q&A pairs
qa_pairs = extract_qa_pairs(doc_path)

# Write to a file
with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(qa_pairs)

print("Extraction complete. The results are saved in 'result.txt'.")