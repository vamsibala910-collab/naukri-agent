from resume_modifier import modify_resume
from pdf_converter import convert_to_pdf
from uploader import upload_resume

print("Step 1: Modifying resume...")
modify_resume()

print("Step 2: Converting to PDF...")
convert_to_pdf()

print("Step 3: Uploading to Naukri...")
upload_resume()

print("All steps completed!")