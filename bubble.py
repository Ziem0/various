

numbers_list = []
with open(, "r") as f:
        input_file = f.readlines()
        for line in input_file:
            numbers_list.append(int(line.strip()))
            