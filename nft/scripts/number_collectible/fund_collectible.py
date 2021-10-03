#!/usr/bin/python3
from brownie import NumberCollectible
from scripts.helpful_scripts import fund_with_link


def main():
    number_collectible = NumberCollectible[len(NumberCollectible) - 1]
    fund_with_link(number_collectible.address)
