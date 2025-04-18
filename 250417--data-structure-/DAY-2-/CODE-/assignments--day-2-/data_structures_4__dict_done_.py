


# <!-- ASSINGMENT (6) -->

# ATM Cash Dispenser
# Given an amount, use the least number of ₹2000, ₹500, ₹200, ₹100 notes to dispense cash. Handle invalid inputs.
[2000,500,200,100]

# 300



print("----------------------")

###---------------------------------------------------
## EXTRA ---NOT RELATED TO TODAY'S CHAPTER OR TOPIC 

#PRACTICE ---  EMPTY SET, EMPTY TUPLE, 
myset = {}
print(myset)

myset = set()
print(myset)

myset.add(1)
print(myset)
myset.remove(1)
print(myset)

mytuple = ()
print(type(mytuple))
print(mytuple)
mytuple = (1, 2, 2)
print(type(mytuple))
print(mytuple)

###---------------------------------------------------


def main():

    print("==================================")
    print("==================================")
    amount = 3100

    #### to void hierarchy of functions , use "list" data structure and loop (loop to reuse a function), and a variable to store "remaining amount" ((rsn= ))
    def count_currency_in_least_note(amount):
        notes = [2000, 500, 200, 100]
        note_count = {}

        for note in notes:
            if amount // note > 0:
                note_count[note] = amount // note
                amount = amount % note
                print(note_count, amount)

    
    count_currency_in_least_note(amount)

    print("==================================")
    print("==================================")
    ###### geek for geek solution

    def countCurrency(amount):    
        notes = [2000, 500, 200, 100]
        notesCount = {}
        
        for note in notes:
            if amount >= note:
                notesCount[note] = amount//note
                amount = amount % note
                
        print ("Currency Count ->")
        for key, val in notesCount.items():
            print(f"{key} : {val}")

    # Driver code
    amount = 868
    countCurrency(amount)
    print("==================================")
    print("==================================")

    ######## solution using hierarchy of functions  (( xxx LONG METHOD xxx))
        
    need_cash = 2800
    print("need cash :" , need_cash)

    # if int(need_cash / 2000) > 0: 
    #     greater_than_2000_note(need_cash) # ERROR : UnboundLocalError: cannot access local variable 'greater_than_2000_note' where it is not associated with a value

    def cash_dispense(money):
        pass

    def greater_than_2000_note(money):
        print(f' 1 * 2000 = 2000')
        # greater_five_hun(money - 2000)

    def greater_five_hun(money):

        if money > 500:
            # 1000 to 500
            num_of_notes__five = int(money /500)
            five_hun = num_of_notes__five * 500

            remaining = money- five_hun
            
            # output_from_two = greater_two_hun(remaining)
            print("----------------------")
            print("calculating for  number of 500 notes ")

            print(f'{num_of_notes__five} * 500 = {five_hun}')
            return {"500":num_of_notes__five, }
        
    def greater_two_hun(money):
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
    

    
    if int(need_cash / 2000) > 0: 
        greater_than_2000_note(need_cash)
        note_2000 = int(need_cash/2000)
        total_note_2000 = note_2000 * 2000

        print("---------------------")
        print(f'{note_2000} * 2000 = {total_note_2000}')

        remaining_under_2000 = need_cash - total_note_2000
        print(remaining_under_2000, "remaining")

        if int(remaining_under_2000 / 500) > 0: 
            greater_five_hun(remaining_under_2000)
            note_500 = int(remaining_under_2000/500)
            total_note_500 = note_500 * 500

            print("---------------------")
            print(f'{note_500} * 500 = {total_note_500}')

            remaining_under_500 = remaining_under_2000 - total_note_500
            print(remaining_under_500, "remaining")
        elif True:
            print("elif")

    



    print("==================================")
    cash_dispense(need_cash)
    print("==================================")
    print("==================================")
    



main()