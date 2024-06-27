"""
Functions necessary for running a virtual cookie shop.
See README.md for instructions.
Do not run this file directly.  Rather, run main.py instead.
"""


def bake_cookies(filepath):
    """
    Opens up the CSV data file from the path specified as an argument.
    - Each line in the file, except the first, is assumed to contain comma-separated information about one cookie.
    - Creates a dictionary with the data from each line.
    - Adds each dictionary to a list of all cookies that is returned.

    :param filepath: The path to the data file.
    :returns: A list of all cookie data, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    cookies = []
    with open(filepath, 'r') as cooky:
        next(cooky)
        for each_line in cooky:
            parameter = each_line.split(',')
            each_cookie = {
                'id': int(parameter[0]),
                'title': parameter[1],
                'description': parameter[2],
                'price': float(parameter[3][1:][:-1]),
            }
            cookies.append(each_cookie)
    return cookies



def welcome():
    """
    Prints a welcome message to the customer in the format:

      Welcome to the Python Cookie Shop!
      We feed each according to their need.

    """
    # write your code for this function below this line
    print("""Welcome to the Python Cookie Shop!
We feed each according to their need.""")
    nuts = input("""We'd hate to trigger an allergic reaction in your body. So please answer the following questions:

Are you allergic to nuts? """)
    gluten = input("Are you allergic to gluten? ")
    sugar = input("Do you suffer from diabetes? ")
    x="1"
    y="0"
    if nuts.lower() == "yes":
        f = open('data/restrictions.txt', 'a')
        f.write(x+"\n")
        f.close()
    else:
        f = open('data/restrictions.txt', 'a')
        f.write(y+"\n")
        f.close()
    if gluten.lower() == "yes":
        f = open('data/restrictions.txt', 'a')
        f.write(x+"\n")
        f.close()
    else:
        f = open('data/restrictions.txt', 'a')
        f.write(y+"\n")
        f.close()
    if sugar.lower() == "yes":
        f = open('data/restrictions.txt', 'a')
        f.write(x+"\n")
        f.close()
    else:
        f = open('data/restrictions.txt', 'a')
        f.write(y+"\n")
        f.close()


def display_cookies(cookies):
    """
    Prints a list of all cookies in the shop to the user.
    - Sample output - we show only two cookies here, but imagine the output continues for all cookiese:
        Here are the cookies we have in the shop for you:

          #1 - Basboosa Semolina Cake
          This is a This is a traditional Middle Eastern dessert made with semolina and yogurt then soaked in a rose water syrup.
          Price: $3.99

          #2 - Vanilla Chai Cookie
          Crisp with a smooth inside. Rich vanilla pairs perfectly with its Chai partner a combination of cinnamon ands ginger and cloves. Can you think of a better way to have your coffee AND your Vanilla Chai in the morning?
          Price: $5.50

    - If doing the extra credit version, ask the user for their dietary restrictions first, and only print those cookies that are suitable for the customer.

    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below this line
    print("Here are the cookies we have in the shop for you:\n")
    for cookie in cookies:
        print(f"#{cookie['id']} - {cookie['title']}")
        print(f"{cookie['description']}")
        print(f"Price: {cookie['price']}")



    




def get_cookie_from_dict(id, cookies):

    """
    Finds the cookie that matches the given id from the full list of cookies.

    :param id: the id of the cookie to look for
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: the matching cookie, as a dictionary
    """
    # write your code for this function below this line
    for cooky in cookies:
        if cooky['id'] == id:
            return cooky
    return 

#get_cookie_from_dict(3,bake_cookies("data/cookies.csv"))
    


def solicit_quantity(id, cookies):
    """
    Asks the user how many of the given cookie they would like to order.
    - Validates the response.
    - Uses the get_cookie_from_dict function to get the full information about the cookie whose id is passed as an argument, including its title and price.
    - Displays the subtotal for the given quantity of this cookie, formatted to two decimal places.
    - Follows the format (with sample responses from the user):

        My favorite! How many Animal Cupcakes would you like? 5
        Your subtotal for 5 Animal Cupcake is $4.95.

    :param id: the id of the cookie to ask about
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: The quantity the user entered, as an integer.
    """
    # write your code for this function below this line

    while True:
        try:
            question = input(f"How many {get_cookie_from_dict(id, cookies)['title']} would you like? ")
            if question.lower() in ["finished", "done", "quit", "exit"]:
                return None
            quantity = int(question)
            if quantity < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid quantity. Please enter a positive integer.")
    cookie = get_cookie_from_dict(id, cookies)
    subtotal = quantity * cookie['price']

    print(f"Your subtotal for {quantity} {cookie['title']} is ${subtotal:.2f}.")
    return quantity

#solicit_quantity(3,bake_cookies("data/cookies.csv"))

def solicit_order(cookies):
    """
    Takes the complete order from the customer.
    - Asks over-and-over again for the user to enter the id of a cookie they want to order until they enter 'finished', 'done', 'quit', or 'exit'.
    - Validates the id the user enters.
    - For every id the user enters, determines the quantity they want by calling the solicit_quantity function.
    - Places the id and quantity of each cookie the user wants into a dictionary with the format
        {'id': 5, 'quantity': 10}
    - Returns a list of all sub-orders, in the format:
        [
          {'id': 5, 'quantity': 10},
          {'id': 1, 'quantity': 3}
        ]

    :returns: A list of the ids and quantities of each cookies the user wants to order.
    """
    # write your code for this function below this line
    order = {}
    list = []
    while True:
        list.append(order)
        cook1 = input("Enter the number of the cookie you would like to order: ")
        if cook1 in ["done","finished","quit","exit"]:
            break
        cook2 = int(cook1)
        amount = solicit_quantity(cook2,bake_cookies("data/cookies.csv"))
        order.update({'id':cook2, 'quantity': amount})
    return list




def display_order_total(order, cookies):
    """
    Prints a summary of the user's complete order.
    - Includes a breakdown of the title and quantity of each cookie the user ordereed.
    - Includes the total cost of the complete order, formatted to two decimal places.
    - Follows the format:

        Thank you for your order. You have ordered:

        -8 Animal Cupcake
        -1 Basboosa Semolina Cake

        Your total is $11.91.
        Please pay with Bitcoin before picking-up.

        Thank you!
        -The Python Cookie Shop Robot.

    """
    # write your code for this function below this line
    total_price = 0
    print("\nThank you for your order. You have ordered:")
    for cookie_id, quantity in order:
        cookie_info = get_cookie_from_dict(cookie_id, cookies)
        if not cookie_info:
            print(f"Error: Cookie with ID {cookie_id} not found.")
            continue
        total_price += quantity * cookie_info['price']
        print(f"- {quantity} {cookie_info['title']}")
    print(f"\nYour total is ${total_price:.2f}.\nPlease pay with Bitcoin before picking-up.")
    print("""Thank you!
          -The Python Cookie Shop Robot.""")


def run_shop(cookies):
    """
    Executes the cookie shop program, following requirements in the README.md file.
    - This function definition is given to you.
    - Do not modify it!

    :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    welcome()
    display_cookies(cookies)
    order = solicit_order(cookies)
    display_order_total(order, cookies)
