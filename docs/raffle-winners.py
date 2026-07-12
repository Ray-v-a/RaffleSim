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
      
def already_won(winners_list,winner):
  if winner in winners_list:
    return True
  else:
    return False
    
def calculate_winners(n_entries,n_winners):
  winners_list=[]
  for i in range(n_winners):
    winner=random.randint(n_entries)
    already_won(winners_list,winner)
    while already_won(winners_list,winner):
      winner=random.randint(n_entries)
    winners_list.append((winner))
  return winners_list
    
  

def get_winners(event=None):
  set_button_busy(True)
  n_entries = int(by_id("entries-input").value)
  n_winners = int(by_id("number-winners-input").value)
  winners_list=calculate_winners(n_entries,n_winners)
  for i in range(len(winners_list)):
    winners_list[i]+=1
  set_text("result-output", str(winners_list))
  finally:
      set_button_busy(False)
