#Intersections of 2 bed files. You can customize minimal length  of intersection area using len_intersect variable. 
def intersections (file1, file2, file3, len_intersect = 0):
    for line1 in file1:
        line1 = line1.strip('\n')
        line1 = line1.split('\t')
        x1 = int(line1[1])
        y1 = int(line1[2])
        c1=int(line1[0])
        for line2 in file2:
            line2 = line2.strip('\n')
            line2 = line2.split('\t')      
            x2 = int(line2[1])
            y2 = int(line2[2])
            c2 = int(line2[0])
            if c1 == c2:
#                print(c1)
                start = max(x1, x2)
                end = min(y1, y2)
                length = min(y1, y2) - max(x1, x2)
                if ((start < end) and (length > len_intersect)):
                    file3.write(str(c1) + '\t' + str(start) + '\t' + str(end) + '\t' + str(length) + '\n')
        file2.seek(0)
