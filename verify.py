from substrateinterface import SubstrateInterface 
import sys

def verify_address():
    description = sys.argv[1]
    # issue_rating = int(sys.argv[2])
    onchain_id = ""
    onchain_address = ""
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
        #print(result)
        onchain_id = result.value['info']['display']['Raw']
        if result.value['judgements'][0][1] == 'Reasonable':
            return 0 
    except: 
        print("An exception occured")
        sys.exit(1)

    # print(result)
    

verify_address()