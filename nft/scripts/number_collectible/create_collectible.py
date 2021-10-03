#!/usr/bin/python3
from brownie import NumberCollectible, accounts, config
from scripts.helpful_scripts import get_number, fund_with_link
import time


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    number_collectible = NumberCollectible[len(NumberCollectible) - 1]
    fund_with_link(number_collectible.address)
    transaction = number_collectible.createCollectible("None", {"from": dev})
    print("Waiting on second transaction...")
    # wait for the 2nd transaction
    transaction.wait(10)
    time.sleep(35)
    requestId = transaction.events["requestedCollectible"]["requestId"]
    token_id = number_collectible.requestIdToTokenId(requestId)
    breed = get_number(number_collectible.tokenIdTooddOrEven(token_id))
    print("Dog breed of tokenId {} is {}".format(token_id, breed))
