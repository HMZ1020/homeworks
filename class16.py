file_path = "C:\\Users\\hmzba\\Desktop\\test_file.txt"

with open(file_path, "x") as file:
     file.write("my name is hamza \ni am good player")


with open(file_path, "a") as file:
    file.write("\nmy name is hamza ")


with open(file_path, "r") as file:
     text = file.read()


print(text)