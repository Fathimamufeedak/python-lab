file_path="exp1c3.py"
lines_list=[]
try:
    with open(file_path,'r') as file:
        lines_list=file.readlines()
    print("files contents stored in list:")
    for line in lines_list:
        print(line.strip())
except FileNotFoundError:
    print(f"error:the file'{file_path}'was not found.")
except Exception as e:
    print(f"An unexcepted error occurred:{e}")
