import csv
import copy
import re 
import sys 
from substrateinterface import SubstrateInterface


def update_csv_file():
    description = sys.argv[1]
    issue_rating = int(sys.argv[2])
    onchain_id = ""
    onchain_address = ""
    print(description)
    for x in description.splitlines():
        if "onchainaddress" in x:
            onchain_address = x.split(":")[1]

    substrate = SubstrateInterface(
        url="wss://mainnet.polkadex.trade"
    )
    if onchain_address[0] == '{':
        size = len(onchain_address)
        onchain_address = onchain_address[1:size-1]
    
    try:
        result = substrate.query(
            module='Identity', 
            storage_function='IdentityOf', 
            params=[onchain_address]
        )
        onchain_id = result.value['info']['display']['Raw']
    except: 
        print("An exception occured")

    print(onchain_id)
    
    

    file = open("reward_cycle_two.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)

    print(rows)
    
    if len(rows) == 0:
        print("New CSV")
        rows.append([onchain_id,"0","0","0","0"])

        if issue_rating == 3: 
            rows[0][1] = int(rows[0][1]) + 1 
            rows[0][4] = 1

        elif issue_rating == 2: 
            rows[0][2] = int(rows[0][2]) + 1 
            rows[0][4] = 1 
           
        elif issue_rating == 1: 
            rows[0][3] = int(rows[0][3]) + 1
            rows[0][4] = 1 
           

        filename = 'reward_cycle_two.csv'
        with open(filename, 'w', newline="") as file:
            csvwriter = csv.writer(file) 
            csvwriter.writerow(header)
            csvwriter.writerows(rows) 

        return

    flag = True 
    for x in rows:
        if x[0] == onchain_id:
            if issue_rating == 3: 
                x[1] = int(x[1]) + 1 
            elif issue_rating == 2: 
                x[2] = int(x[2]) + 1 
            elif issue_rating == 1: 
                x[3] = int(x[3]) + 1 
            flag = False
    
    # If first time     
    if flag == True:
        new_tester = copy.copy(rows[0]) 
        new_tester[0] = onchain_id
        new_tester[1] = 0
        new_tester[2] = 0 
        new_tester[3] = 0 
        if issue_rating == 3: 
            new_tester[1] = int(new_tester[1]) + 1 
        elif issue_rating == 2: 
            new_tester[2] = int(new_tester[2]) + 1 
        elif issue_rating == 1: 
            new_tester[3] = int(new_tester[3]) + 1 
        rows.append(new_tester)

    for x in rows: 
        x[4] = int(x[1]) + int(x[2]) + int(x[3])
    
    filename = 'reward_cycle_two.csv'
    with open(filename, 'w', newline="") as file:
        csvwriter = csv.writer(file) 
        csvwriter.writerow(header)
        csvwriter.writerows(rows) 




update_csv_file()
