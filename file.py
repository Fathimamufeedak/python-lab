file_name=input("enter the file name:")
if "." in file_name:
    extension=file_name.split(".")[-1]
    print(f"the extension of the file is :{extension}")
else:
    print("the entered file does not have an extension.")
