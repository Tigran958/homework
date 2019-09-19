# Variables
fridge_item_type = "vegetables"
fridge_item_type_2 = "fruits"
fridge_items = "vegetables,fruits"
firdge_juce = "juce"
electricity = "on"
first_print = "Is it true, that I should empty the fridge? "
market_print = "Should I go to the market for some juce?"
p_break = " "
text_first = "We have no electricity, and there are vegetables in the fridge, but no juce. So "
# Actions
check_fridge = str(electricity in "on" and fridge_items != "")
check_if_fridge = check_fridge == "True" and (fridge_item_type_2 == "fruits" or fridge_item_type == "vegetables")
check_if_items = str(check_fridge == "True" and firdge_juce not in fridge_items)

print(text_first)
print(first_print + p_break + str(check_if_fridge))
print(market_print + p_break + check_if_items)

input(p_break)
###########Second one###########

# Variables
txt_1 = "Hello"
first_print = "Let's order somthing to eat, for example qyabab "
first_quest = "what kind of bread would you like? (lavash/boqon) "
second_quest = "what kind of meat would you like? (chicken/beef) "
third_quest = "ketchup/nothing ? "
amount = "How many do you want? "
bread = "lavash"
bread_2 = "boqon"
meat = "chicken"
meat_2 = "beef"
additional = "ketchup"
additional_2 = "nothing"
pb = " "
price_amount = "You should pay: "
input(txt_1)
print(first_print)

# Input values
order_answer_first = input(first_quest)
order_answer_second = input(second_quest)
order_answer_third = input(third_quest)
order_amout = input(amount)
int_amount = int(order_amout)

# Amounts
price_lavash_chicken_ketchup = 1100 * int_amount
price_lavash_beef_ketchup = 1200 * int_amount
price_boqon_chicken_ketchup = 1300 * int_amount
price_boqon_beef_ketchup = 1400 * int_amount
price_lavash_chicken_nothing = 1000 * int_amount
price_lavash_beef_nothing = 1100 * int_amount
price_boqon_chicken_nothing = 1200 * int_amount
price_boqon_beef_nothing = 1300 * int_amount

# Checkings
lck_or_lbn = ((order_answer_first == bread) and (order_answer_second == meat) and (order_answer_third == additional)) or ((order_answer_first == bread) and (order_answer_second == meat_2) and (order_answer_third == additional_2))
lbk_or_bcn = ((order_answer_first == bread) and (order_answer_second == meat_2) and (order_answer_third == additional)) or ((order_answer_first == bread_2) and (order_answer_second == meat) and (order_answer_third == additional_2))
bck_or_bbn = ((order_answer_first == bread_2) and (order_answer_second == meat) and (order_answer_third == additional)) or ((order_answer_first == bread_2) and (order_answer_second == meat_2) and (order_answer_third == additional_2))
bbk = (order_answer_first == bread_2) and (order_answer_second == meat_2) and (order_answer_third == additional)
#lcn = not bbk 
lcn = (order_answer_first == bread) and (order_answer_second == meat) and (order_answer_third == additional_2)

# Action
print("You've ordered " + order_amout + pb + order_answer_second + pb + "qyabab with " + order_answer_third + pb + "in " + order_answer_first)
print(price_amount + str())
print(str(price_lavash_chicken_ketchup) + pb + str(lck_or_lbn))
print(str(price_lavash_beef_ketchup) + pb + str(lbk_or_bcn))
print(str(price_boqon_chicken_ketchup) + pb + str(bck_or_bbn))
print(str(price_boqon_beef_ketchup) + pb + str(bbk))
print(str(price_lavash_chicken_nothing) + pb + str(lcn))








