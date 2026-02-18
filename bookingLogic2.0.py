import html


def get_secure_bb_variants():
    return {
        "Standard": {"price": 80, "available": True},
        "Deluxe": {"price": 120, "available": True},
        "Suite": {"price": 200, "available": True},
        "Single": {"price": 50, "available": True}
    }


def process_user_booking(room_selection, stay_days):
    try:
        days = int(stay_days)
        if days <= 0:
            return "Error: Invalid stay duration."
    except ValueError:
        return "Error: Please enter a valid number for days."

    clean_selection = html.escape(str(room_selection)).strip().title()
    variants = get_secure_bb_variants()

    if clean_selection not in variants:
        return "Security Alert: Unauthorized access or room not found."

    selected_room = variants[clean_selection]

    if not selected_room["available"]:
        return f"Sorry, the {clean_selection} room is currently unavailable."

    total_price = selected_room["price"] * days
    return f"Confirmed: {clean_selection}. Total: {total_price} Euro."


if __name__ == "__main__":
    print("--- B&B Booking System (Kira Edition) ---")
    scelta = input("Inserisci il tipo di stanza (Standard, Deluxe, Suite, Single): ")
    giorni = input("Per quanti giorni vuoi soggiornare? ")

    risultato = process_user_booking(scelta, giorni)
    print("\n" + risultato)