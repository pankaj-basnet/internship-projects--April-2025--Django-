


# <!-- ASSINGMENT (6) -->

# ATM Cash Dispenser
# Given an amount, use the least number of ₹2000, ₹500, ₹200, ₹100 notes to dispense cash. Handle invalid inputs.


print("----------------------")

need_cash = 700
print("need cash :" , need_cash)

def cash_dispense( money):
    if money > 500:
        # 1000 to 500
        num_of_notes__five = int(money /500)
        five_hun = num_of_notes__five * 500

        remaining = money- five_hun
        
        output_from_two = gr_two_hun(remaining)
        print("----------------------")
        print("calculating for  number of 500 notes ")

        print(f'{num_of_notes__five} * 500 = {five_hun}')
        return {"500":num_of_notes__five, }
    
def gr_two_hun(money):
        # 200 to 500
    print("calculating for cash less than 500 ")
    print("----------------------")

    num_of_notes__two = int(money /200)
    two_hun = num_of_notes__two * 200

    one_hun = money- two_hun

    num_of_notes__one = 0
    if one_hun > 0:
        num_of_notes__one = 1

    print(f'{num_of_notes__two} * 200 = {two_hun}')
    print(f'{num_of_notes__one} * 100 = {one_hun}')
    return {"200":num_of_notes__two, "100":num_of_notes__one }


print("==================================")
cash_dispense(need_cash)
print("==================================")
