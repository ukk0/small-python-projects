import os
import datetime


# Renames all .txt files in the target folder to include current datetime.
# If already includes the date, removes it instead.

def add_date_to_txt_files(directory: str):
    today = str(datetime.date.today())
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            filepath = os.path.join(directory, file)
            name, ext = os.path.splitext(file)

            if name.endswith(f"-{today}"):
                new_name = name[:-(len(today) + 1)] + ext
                action = "removed"
            else:
                new_name = f"{name}-{today}{ext}"
                action = "added"

            new_path = os.path.join(directory, new_name)
            os.rename(filepath, new_path)
            print(f"Date {action} for file {file}. New name is {new_name}.")


if __name__ == "__main__":
    path = '../resources/text_files'
    add_date_to_txt_files(path)
