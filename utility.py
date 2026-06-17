from dotenv import load_dotenv
load_dotenv(override = True)

import os

my_password = os.getenv("my_password")
email = os.getenv("my_email")


def read_file(file_path: str):
    with open(file_path, "r", encoding = "utf-8") as f:
        output = f.read()
    return output


def modify(output: str, name: str, your_name: str):
    new_output = output.replace("{name}", name).replace("[Your Name]", your_name)
    
    return new_output