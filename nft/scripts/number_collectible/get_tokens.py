#!/usr/bin/python3
from brownie import SimpleCollectible, NumberCollectible, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import get_number


def main():
    print("Working on " + network.show_active())
    number_collectible = NumberCollectible[len(SimpleCollectible) - 1]
    breakpoint()
    number_of_number_collectibles = number_collectible.tokenCounter()
    print(number_of_number_collectibles)
