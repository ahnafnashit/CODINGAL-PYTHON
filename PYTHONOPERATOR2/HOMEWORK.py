def check_if_alphabet(char):
  
   
    is_lower_case = (char >= 'a') and (char <= 'z')

   
    is_upper_case = (char >= 'A') and (char <= 'Z')


    if is_lower_case or is_upper_case:
        return True
    else:
        return False


user_input = input("Enter a single character to check: ")


if len(user_input) != 1:
    print("Please enter only a single character.")
else:
    char_to_check = user_input[0]
    

    if check_if_alphabet(char_to_check):
        print(f"'{char_to_check}' is an **alphabet**.")
    else:
        print(f"'{char_to_check}' is **not** an alphabet.")