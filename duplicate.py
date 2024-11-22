lines_seen = set() # holds lines already seen
outfile = open("jobsReed.txt", "w")
for line in open("jobsReedUK(new).txt", "r", encoding="UTF-8"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print("done!")
