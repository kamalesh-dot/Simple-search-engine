def search_in_file(file_path, keyword):
 try:
 with open(file_path, 'r') as file:
 lines = file.readlines()
 found = False
 for line_number, line in enumerate(lines, start=1):
 if keyword.lower() in line.lower():
 print(f"Line {line_number}: {line.strip()}")
 found = True
 if not found:
 print(f"No occurrences of '{keyword}' found in the file.")
 except FileNotFoundError:
 print(f"File '{file_path}' not found.")
 except Exception as e:
 print(f"An error occurred: {e}")
if _name_ == "_main_":
 file_path = input("Enter the path to the file: ").strip()
 keyword = input("Enter the keyword to search for: ").strip()
 search_in_file(file_path, keyword)
