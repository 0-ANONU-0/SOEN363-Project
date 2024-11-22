with open('jobsadzunaUS(new).txt', 'r', encoding="UTF-8") as istr:
    with open('jobsUS.txt', 'w', encoding="UTF-8") as ostr:
        for line in istr:
            line = line.rstrip('\n') + '!!!'
            print(line, file=ostr)

with open('jobsadzunaCA(new).txt', 'r', encoding="UTF-8") as istr:
    with open('jobsCA.txt', 'w', encoding="UTF-8") as ostr:
        for line in istr:
            line = line.rstrip('\n') + '!!!'
            print(line, file=ostr)

with open('jobsadzunaAU(new).txt', 'r', encoding="UTF-8") as istr:
    with open('jobsAU.txt', 'w', encoding="UTF-8") as ostr:
        for line in istr:
            line = line.rstrip('\n') + '!!!'
            print(line, file=ostr)

with open('jobsReed.txt', 'r', encoding="UTF-8") as istr:
    with open('jobsR.txt', 'w', encoding="UTF-8") as ostr:
        for line in istr:
            line = line.rstrip('\n') + '!!!'
            print(line, file=ostr)

print("Done")

#Changed the size of split array to 13 as newline became teh last element 