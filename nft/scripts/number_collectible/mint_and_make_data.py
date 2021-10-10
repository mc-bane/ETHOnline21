#!/usr/bin/python3
from brownie import NumberCollectible, accounts, config
from scripts.helpful_scripts import get_number, fund_with_link
import time

#!/usr/bin/python3
from scripts.number_collectible.image_factory import factory
import os
import requests
import json
from brownie import NumberCollectible, network
from metadata import sample_metadata
from scripts.helpful_scripts import get_number
from pathlib import Path
from dotenv import load_dotenv

#!/usr/bin/python3
from brownie import SimpleCollectible, NumberCollectible, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import get_number, OPENSEA_FORMAT

load_dotenv()

d= {}
def main():
    dev = accounts.add(config["wallets"]["from_key"])
    number_collectible = NumberCollectible[len(NumberCollectible) - 1]
    fund_with_link(number_collectible.address)
    transaction = number_collectible.createCollectible("None", {"from": dev})
    print("Waiting on second transaction...")
    # wait for the 2nd transaction
    transaction.wait(2)
    time.sleep(35)
    requestId = transaction.events["requestedCollectible"]["requestId"]
    token_id = number_collectible.requestIdToTokenId(requestId)
    breed = get_number(number_collectible.tokenIdTooddOrEven(token_id))
    print("Generative NFT of tokenId {} is {}".format(token_id, breed))

    print("Working on " + network.show_active())
    number_collectible = NumberCollectible[len(NumberCollectible) - 1]
    number_of_number_collectibles = number_collectible.tokenCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_number_collectibles)
    )
    write_metadata(number_of_number_collectibles, number_collectible)
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
                            d[token_id])
        else:
            print("Skipping {}, we already set that tokenURI!".format(token_id))


def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(nft_contract.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')




def write_metadata(token_ids, nft_contract):
    for token_id in range(token_ids):
        #writes trait info
        collectible_metadata = sample_metadata.metadata_template

        breed = get_number(nft_contract.tokenIdTooddOrEven(token_id))
        value = nft_contract.tokenIdToValue(token_id)
        #make the number image!
        factory(value)


        metadata_file_name = (
            "./metadata/{}/".format(network.show_active())
            + str(token_id)
            + "-"
            + str(value)
            + ".json"
        )
        if Path(metadata_file_name).exists():
            print(
                "{} already found, delete it to overwrite!".format(
                    metadata_file_name)
            )
        else:
            print("Creating Metadata file: " + metadata_file_name)
            collectible_metadata["name"] = get_number(
                nft_contract.tokenIdTooddOrEven(token_id)
            )
            collectible_metadata["description"] = "An adorable {} pup!".format(
                collectible_metadata["name"]
            )
            image_to_upload = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_path = "./img/{}.png".format(
                    value)
                image_to_upload = upload_to_ipfs(image_path)
            #image_to_upload = (
            #   breed_to_image_uri[breed] if not image_to_upload else image_to_upload
            #)
            collectible_metadata["image"] = image_to_upload
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                d[token_id]=upload_to_ipfs(metadata_file_name)

# curl -X POST -F file=@metadata/rinkeby/0-SHIBA_INU.json http://localhost:5001/api/v0/add


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = (
            os.getenv("IPFS_URL")
            if os.getenv("IPFS_URL")
            else "http://localhost:5001"
        )
        response = requests.post(ipfs_url + "/api/v0/add",
                                 files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = "https://ipfs.io/ipfs/{}?filename={}".format(
            ipfs_hash, filename)
        print(image_uri)
    return image_uri
