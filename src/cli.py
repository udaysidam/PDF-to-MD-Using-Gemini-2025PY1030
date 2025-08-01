import os 
import 

def list_pdf_files():
    """List all PDF files in the current directory."""
    return [f for f in os.listdir() if f.endswith("PDF-to-MD-Using-Gemini-2025PY1030/sam/sample.pdf")]

def select_pdfs(pdf_files):
    """CLI UI to select PDF files using inquirer."""
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return []

    questions = [
        inquirer.Checkbox(
            'selected',
            message="Select PDF files to convert",
            choices=pdf_files,
        )
    ]

    answers = inquirer.prompt(questions)
    return answers.get("selected", [])

    def create_output_dir():
    """Create a new directory named <current-folder>_converted-md."""
    current_dir = os.path.basename(os.getcwd())
    output_dir = f"{current_dir}_converted-md"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

    def convert_pdf_to_md(selected_pdfs, output_dir):
    """Simulate conversion from PDF to Markdown and save to output_dir."""
    for pdf in selected_pdfs:
        md_filename = os.path.splitext(pdf)[0] + ".md"
        md_path = os.path.join(output_dir, md_filename)

        # Simulated conversion: You can replace this with real content
        with open(md_path, "w") as f:
            f.write(f"# Converted Markdown from {pdf}\n\n(Placeholder content)")

        print(f" Converted: {pdf} -> {md_filename}")

def main():
    pdf_files = list_pdf_files()
    selected_pdfs = select_pdfs(pdf_files)
    
    if selected_pdfs:
        print("\n You selected:")
        for f in selected_pdfs:
            print(f" - {f}")    
    else:
        print(" No PDF files selected.")

if __name__ == "__main__":
    main()
