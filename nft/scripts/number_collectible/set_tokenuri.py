#!/usr/bin/python3
from brownie import SimpleCollectible, NumberCollectible, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import get_number, OPENSEA_FORMAT


metadata_dic = {
    0:"https://ipfs.io/ipfs/QmdobKtyQvJvkiAZwmJzUatvdrfMuTvZBVKupCVvPRnTvS?filename=0-18.json",
    1: "https://ipfs.io/ipfs/QmS7i14fhUcpeDhu4vLTRN41NcRyF4CKjryEtWEZQBdJ8L?filename=1-6.json",
    2: "https://ipfs.io/ipfs/QmUYQQ4M3XX8jTU54ek5PhyHQnQ2QKGhDz99yMBRSjYMus?filename=2-64.json",
    3: "https://ipfs.io/ipfs/QmTU5wR1Gx9VunYef8kqRDBpZoajBxqbyGhyDcrvJvmVWU?filename=3-71.json",
    4: "https://ipfs.io/ipfs/QmS8tUut8gAYtskMCtueLbjPyGgtL4tJgibtj5K5LEAGJ3?filename=4-66.json",
    5: "https://ipfs.io/ipfs/QmePLx6TbF4tBGRhkMKmCoktfJ1keuCATtU2SiVoTRmAqF?filename=5-91.json",
    6: "https://ipfs.io/ipfs/QmRLMCRTjoDgDnwEFEwTm8VSM6tVJfs34dyLRos265uMmu?filename=6-56.json",
    7: "https://ipfs.io/ipfs/QmTU5wR1Gx9VunYef8kqRDBpZoajBxqbyGhyDcrvJvmVWU?filename=7-71.json",
    8: "https://ipfs.io/ipfs/QmRYBd391sF4ab2kiU6vwAMeHrSqW9BQCZp1b7mUp94c55?filename=8-31.json",
    9: "https://ipfs.io/ipfs/QmRU8D81wzHPNANiBXJVsFM3VwDX9gdCGJcSMeFN8c99Bz?filename=9-29.json"
}

def main():
    print("Working on " + network.show_active())
    number_collectible = NumberCollectible[len(NumberCollectible) - 1]
    number_of_number_collectibles = number_collectible.tokenCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_number_collectibles)
    )
    for token_id in range(number_of_number_collectibles):

        #breed = get_number(number_collectible.tokenIdTooddOrEven(token_id))
        if not number_collectible.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id, number_collectible,
                            metadata_dic[token_id])
        else:
            print("Skipping {}, we already set that tokenURI!".format(token_id))
            set_tokenURI(token_id, number_collectible,
                            metadata_dic[token_id])


def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(nft_contract.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
