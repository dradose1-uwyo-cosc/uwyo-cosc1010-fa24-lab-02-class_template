#Name : Rikart Yeimo
#Lab Section : Homework 4
#Submission Date : 11/12/2024
#Helped by : Ryan Zafft

from pathlib import Path

inputPath = Path("prompt.txt")
bacth = inputPath.read_text()
bacth = bacth.splitlines()

result = ""

for line in bacth:
    pair = line.split("\t")
    for item in pair:
        x = item.split(":")
        if x[0] == "w":
            result += int(x[1])  * " "
        
        if x[0] == "*":
            result += int(x[1]) * "*"

    result += "\n"








outputpath = Path("out.txt")
outputpath.write_text(result)
