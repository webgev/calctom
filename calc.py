import helper

def calc(count: int, price: float, state: str) -> (float, float) :
    if not helper.valid_int(count):
       raise helper.ErrorCount("Введите правильное количество!")
    
    if not helper.valid_int(price):
       raise helper.ErrorPrice("Введите правильную цену!")
       
    if not state or str(state).lower() not in helper.STATE:
       raise helper.ErrorState("Выберите действующий штат!")
   
    count = int(count)
    price = float(price)
    total = price * count
    dicount = helper.MAX_DISCOUNTS
    
    for key, value in helper.DISCOUNTS.items():
        if total in key:
            dicount = value
            break
    
    dicount_total = total
    if dicount: 
        dicount_total -= dicount_total * dicount / 100
    total = dicount_total + (dicount_total * helper.STATE[state.lower()] / 100)
    return total, dicount_total