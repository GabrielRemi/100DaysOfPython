from card_deck import Card, CardDeck


def calculate_card_values(cards: list[Card]) -> int:
    result = sum(map(lambda x: x.value, cards))
    ace_count = len(list(filter(lambda x: x.name == "Ace", cards)))

    while result > 21:
        if ace_count == 0:
            break

        ace_count -= 1
        result -= 10

    return result


def cards_str(name: str, cards: list[Card]) -> str:
    text = f"{name} cards: "
    for card in cards:
        text += f" {card}"
    text += "\n"
    return text


def print_cards(name: str, cards: list[Card]) -> None:
    print(f"{cards_str(name, cards)} -> {calculate_card_values(cards)}")


def loose():
    global end_of_game
    end_of_game = True
    print("\nYou lost!\n")


def win():
    global end_of_game
    end_of_game = True
    print("\nYou Won!\n")


end_of_game = False


def play_game():
    global end_of_game
    end_of_game = False

    player_cards: list[Card] = []
    dealer_cards: list[Card] = []
    print("New Round!")

    deck = CardDeck()
    deck.shuffle()

    dealer_cards.append(deck.take_from_top())
    player_cards.append(deck.take_from_top())
    dealer_cards.append(deck.take_from_top())
    player_cards.append(deck.take_from_top())

    while True:
        print(f"Dealer's cards: {dealer_cards[0]}")
        print_cards("player", player_cards)

        if input("Take another Card? (y/n) ").lower() == "n":
            break

        player_cards.append(deck.take_from_top())

        if calculate_card_values(player_cards) > 21:
            break


    print_cards("dealer", dealer_cards)
    print_cards("player", player_cards)
    print("\n\n")

    dealer_value = calculate_card_values(dealer_cards)
    player_value = calculate_card_values(player_cards)
    if player_value < dealer_value or player_value > 21:
        loose()
    else:
        win()


def main():
    print("Welcome to Black Jack!")

    while True:
        play_game()
        if input("Another Round? (y/n) ").lower() == "n":
            break


if __name__ == '__main__':
    main()
