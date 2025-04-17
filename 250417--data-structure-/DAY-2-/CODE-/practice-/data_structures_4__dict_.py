


# <!-- ASSINGMENT (6) -->

# ATM Cash Dispenser
# Given an amount, use the least number of ₹2000, ₹500, ₹200, ₹100 notes to dispense cash. Handle invalid inputs.



need_cash = 700

def cash_dispense( money):
    if money > 500:
        # 1000 to 500
        num_of_notes__five = int(money /500)
        five_hun = num_of_notes__five * 500

        remaining = money- five_hun
        
        output_from_two = gr_two_hun(remaining)
        print(output_from_two)
        print("----------------------")


        # num_of_notes__one = 0
        # if remaining > 0:
        #     num_of_notes__one = 1

        print(f'{num_of_notes__five} * 500 = {five_hun}')
        # print(f'{num_of_notes__one} * 200 = {remaining}')
        # print(f'{num_of_notes__one} * 100 = {remaining}')
        # print ("cash", (num_of_notes__five + num_of_notes__one))

        # return {"500":num_of_notes__five, "100":num_of_notes__one }
        return {"500":num_of_notes__five, }
    
    # if money > 200:
    #     # two_hun
    #     num_of_notes__two = int(money /200)
    #     two_hun = num_of_notes__two * 200

    #     one_hun = money- two_hun

    #     num_of_notes__one = 0
    #     if one_hun > 0:
    #         num_of_notes__one = 1

    #     print(f'{num_of_notes__two} * 200 = {two_hun}')
    #     print(f'{num_of_notes__one} * 100 = {one_hun}')
    #     print ("cash", (num_of_notes__two + num_of_notes__one))

    #     return {"200":num_of_notes__two, "100":num_of_notes__one }


def gr_two_hun(money):
        # 200 to 500
    print("calculating for cash less than 500 ")

    num_of_notes__two = int(money /200)
    two_hun = num_of_notes__two * 200

    one_hun = money- two_hun

    num_of_notes__one = 0
    if one_hun > 0:
        num_of_notes__one = 1

    print(f'{num_of_notes__two} * 200 = {two_hun}')
    print(f'{num_of_notes__one} * 100 = {one_hun}')
    print ("cash", (num_of_notes__two + num_of_notes__one))

    return {"200":num_of_notes__two, "100":num_of_notes__one }

cash_dispense(need_cash)
print(cash_dispense(need_cash))