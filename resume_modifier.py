from docx import Document
from datetime import date

def modify_resume():

    # Load master resume
    doc = Document("resumes/master_resume.docx")

    # Today's date
    today = date.today()

    # Odd day certification text
    odd_text = (
        "Node.js — NxtWave Intensive | REST APIs, Express.js, JWT Authentication, bcrypt"
    )

    # Even day certification text
    even_text = (
        "Node.js — NxtWave Intensive | Express.js, REST APIs, JWT Authentication, bcrypt"
    )

    # Modify certification line
    for para in doc.paragraphs:

        if "Node.js" in para.text:

            if today.day % 2 == 0:
                para.text = even_text
            else:
                para.text = odd_text

        # Update date
        if "Date:" in para.text:
            para.text = f"Date: {today.strftime('%d-%m-%Y')}"

    # Save modified resume
    doc.save("resumes/modified_resume.docx")

    print("Resume modified successfully!")