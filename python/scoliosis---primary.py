# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"7J44111","system":"readv2"},{"code":"N373500","system":"readv2"},{"code":"N373z00","system":"readv2"},{"code":"N374A00","system":"readv2"},{"code":"N374B00","system":"readv2"},{"code":"N374C00","system":"readv2"},{"code":"N374D00","system":"readv2"},{"code":"11620.0","system":"med"},{"code":"12549.0","system":"med"},{"code":"14790.0","system":"med"},{"code":"22657.0","system":"med"},{"code":"28717.0","system":"med"},{"code":"3059.0","system":"med"},{"code":"36682.0","system":"med"},{"code":"3705.0","system":"med"},{"code":"40041.0","system":"med"},{"code":"42901.0","system":"med"},{"code":"43192.0","system":"med"},{"code":"4330.0","system":"med"},{"code":"45232.0","system":"med"},{"code":"45554.0","system":"med"},{"code":"53874.0","system":"med"},{"code":"56368.0","system":"med"},{"code":"64218.0","system":"med"},{"code":"67445.0","system":"med"},{"code":"7136.0","system":"med"},{"code":"714.0","system":"med"},{"code":"72582.0","system":"med"},{"code":"755.0","system":"med"},{"code":"9567.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('scoliosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["scoliosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["scoliosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["scoliosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
