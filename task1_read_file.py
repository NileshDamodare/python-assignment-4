try:
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        for index, line in enumerate(file, start=1):
            print(f"line {index}: {line.strip()}")
except FileNotFoundError:
    print("error: the file 'sample.txt' was not found")
