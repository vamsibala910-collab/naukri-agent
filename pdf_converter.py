from docx2pdf import convert


def convert_to_pdf():

    print("Converting DOCX to PDF...")

    convert(
        "resumes/modified_resume.docx",
        "resumes/modified_resume.pdf"
    )

    print("PDF created successfully!")