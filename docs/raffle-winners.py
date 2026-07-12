from pyscript import document
from numpy import random


def by_id(element_id):
    return document.getElementById(element_id)


def set_text(element_id, text):
    el = by_id(element_id)
    if el is not None:
        el.textContent = text


def set_button_busy(is_busy):
    button = by_id("get-winners-button")
    if button is not None:
        button.disabled = is_busy
        button.textContent = "Computing..." if is_busy else "Get winners"


def calculate_winners(n_entries, n_winners):
    if n_entries <= 0:
        raise ValueError("Number of entries must be greater than 0.")
    if n_winners < 0:
        raise ValueError("Number of winners cannot be negative.")
    if n_winners > n_entries:
        raise ValueError("Number of winners cannot exceed number of entries.")
    winners_list = random.choice(n_entries, size=n_winners, replace=False)
    return [int(winner) + 1 for winner in winners_list]


def get_winners(event=None):
    set_button_busy(True)
    try:
        n_entries = int(by_id("entries-input").value)
        n_winners = int(by_id("number-winners-input").value)
        winners_list = calculate_winners(n_entries, n_winners)
        set_text("result-output", str(winners_list))
    except Exception as e:
        set_text("result-output", f"Error: {e}")
    finally:
        set_button_busy(False)
