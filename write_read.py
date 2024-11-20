path = '/workspaces/lab-02-Rikartyeimo/write,Read.py'
enter_text = input("Enter some sentence -----")

with open(path, 'a') as opened_file:
    opened_file.write(enter_text)

with open(path, 'r') as opened_file:
    for line in opened_file:
        print(line.split('\t'), end='')