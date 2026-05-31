from playwright.sync_api import sync_playwright
import os

SESSION_FOLDER = "naukri_session"

def upload_resume():

    with sync_playwright() as p:

        context = p.chromium.launch_persistent_context(
            user_data_dir=SESSION_FOLDER,
            headless=False
        )

        page = context.new_page()

        print("Opening profile page...")

        # DIRECT PROFILE PAGE
        page.goto("https://www.naukri.com/mnjuser/profile")

        page.wait_for_timeout(5000)

        current_url = page.url

        # FIRST TIME LOGIN ONLY
        if "login" in current_url:

            print("Login required!")

            input(
                "\nComplete login manually.\n"
                "After login press ENTER...\n"
            )

            page.goto("https://www.naukri.com/mnjuser/profile")

            page.wait_for_timeout(5000)

        print("Uploading resume...")

        page.locator("#attachCV").set_input_files(
            "resumes/modified_resume.pdf"
        )

        print("Resume uploaded successfully!")

        page.wait_for_timeout(5000)

        context.close()


