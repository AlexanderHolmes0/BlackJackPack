import pandas as pd
import itertools


def generate_deck():
    """Create a deck of cards

    :return: A list of dictionaries representing the cards in the deck
    """

    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    # Use itertools.product to create all possible combinations of ranks and suits
    deck = [
        {"rank": rank, "suit": suit} for rank, suit in itertools.product(ranks, suits)
    ]
    return deck


def draw_card(deck):
    """Draw a card from the deck

    :param deck: The deck of cards
    :return: A dictionary representing the card drawn from the deck
    """

    # Check if the deck is empty
    if not deck:
        print("The deck is empty.")
        return None

    # Draw the top card from the deck
    drawn_card = deck.pop(0)
    return drawn_card


def draw_hand(deck, hand_size):
    """Draw a hand from the deck

    :param deck: The deck of cards
    :param hand_size: The number of cards to draw
    :return: A list of dictionaries representing the cards drawn from the deck
    """

    # Check if the deck is empty
    if not deck:
        print("The deck is empty.")
        return None

    # Check if the deck has enough cards for the hand
    if len(deck) < hand_size:
        print("The deck does not have enough cards.")
        return None

    # Draw a hand from the deck
    hand = [draw_card(deck) for _ in range(hand_size)]
    return hand
