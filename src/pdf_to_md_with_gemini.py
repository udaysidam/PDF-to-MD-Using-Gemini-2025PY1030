import os
import fitz  # PyMuPDF
import inquirer
import google.generativeai as genai
from dotenv import load_dotenv   # ✅ load dotenv

load_dotenv()  # ✅ loads .env file into environment
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))  

# Set API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# ✅ Set your PDF directory path
pdf_directory = r"C:/Users/ANOOP/Downloads/gitrepo/PDF-to-MD-Using-Gemini-2025PY1030/src"

def list_pdf_files():
    # list all PDFs in the directory
    return [f for f in os.listdir(pdf_directory) if f.lower().endswith(".pdf")]

def select_files(files):
    if not files:
        print("No PDF files found.")
        return []
    questions = [
        inquirer.Checkbox(
            "choices",
            message="Select PDF files to convert",
            choices=files,
        )
    ]
    answers = inquirer.prompt(questions)
    return answers["choices"] if answers else []

def create_output_folder():
    folder = os.path.basename(os.getcwd()) + "_converted-md"
    os.makedirs(folder, exist_ok=True)
    return folder

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    content = ""
    for page in doc:
        content += page.get_text()
    return content.strip()

def convert_text_to_md(text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Convert the following text into Markdown format:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text

def save_markdown(filename, content, folder):
    name = os.path.splitext(filename)[0] + ".md"
    path = os.path.join(folder, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Saved: {path}")

def main():
    pdfs = list_pdf_files()
    selected = select_files(pdfs)

    if not selected:
        print("No files selected.")
        return

    output_dir = create_output_folder()

    for pdf in selected:
        full_path = os.path.join(pdf_directory, pdf)
        pdf_text = extract_text_from_pdf(full_path)
        if not pdf_text:
            print(f"No text found in {pdf}, skipping.")
            continue
        md_content = convert_text_to_md(pdf_text)
        save_markdown(pdf, md_content, output_dir)

    print(f"\n🎉 All files converted and stored in: {output_dir}")

if __name__ == "__main__":
    main()
