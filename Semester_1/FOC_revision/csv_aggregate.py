import csv
def csv_aggregate(infile, outfile):
    fpout = open(outfile, 'w')
    prev_docid = None
    pos = total = 0
    for row in csv.DictReader(open(infile)):
        print(f'previous docid is {prev_docid}, {pos} is pos, {total} is total, {row["docid"]}')
        if row['docid'] != prev_docid:
            if prev_docid != None:
                fpout.write("{},{}\n".format(prev_docid,pos/total))    
            prev_docid = row['docid']
            pos = total = 0
        if row['pos'] == '1':
            pos += 1
        total +=1
    if prev_docid != None:
        fpout.write("{},{}\n".format(prev_docid,pos/total)) 
    fpout.close()
csv_aggregate('rating.csv', 'some.csv')
        

    