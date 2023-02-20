import re
import logging

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger()

def check_card_validity():
    """This code validates credit card numbers entered by the user

    :param number: prompts the user to enter the total number of credit card numbers they want to validate
    :param credit: iterates over the range of the entered number of cards, taking input of each credit card number from the user and stripping any leading or trailing whitespaces
    :Param credit_removed_hiphen:  removes any hyphens from the credit card number using the replace function and assigns it to a new variable credit_removed_hiphen
    :Param valid:The variable valid is initialized to True
    :Param length_16: checks if the credit card number is 16 digits long and starts with either 4, 5 or 6. If it matches, then the variable length_16 is assigned True
    :Param length_19: checks if the credit card number is 19 digits long and starts with either 4, 5 or 6. If it matches, then the variable length_19 is assigned True
    :Param consecutive:  checks if there are more than 4 consecutive repeating digits in the credit card number, after removing any hyphens. If it matches, then the variable consecutive is assigned True
    """

    # This line prompts the user to enter the number of credit cards they want to check
    N = int(input("Please enter the number credit card number to be checked: "))
    if  0 < N < 100:
        try:
            # This line sets up a loop that will iterate for the number of credit cards specified by the user
            for i in range(N):
                credit = input().strip()
                credit_removed_hiphen = credit.replace('-','') #This line takes the credit card number from the user and removes any hyphens from it
                
                # This line sets a variable valid to True at the beginning
                valid = True
                
                # These three lines use regular expressions to check whether the credit card number is valid
                length_16 = bool(re.match(r'^[4-6]\d{15}$',credit))  
                length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$',credit))  
                consecutive = bool(re.findall(r'(?=(\d)\1\1\1)',credit_removed_hiphen))
                
                # checking if the above regural expressions are true
                if length_16 == True or length_19 == True:
                    if consecutive == True:
                        valid=False
                else:
                    valid = False       
                if valid:
                    print('Valid')
                else:
                    print('Invalid')
        except Exception as error:
            logger.error(f"Your code has failed because of the following {error} ")
            return False
    else:
        print(f"The number of credrit card number you have chosen is out of range.\n Please choose a number between 0 and 100, and rerun the code.")    
    return True

if __name__ == "__main__":
    logger.info(f"Your function has started running.....")
    check_card_validity()
    logger.info(f"Your function has successfully run!!!")