MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1500,
    "milk": 1000,
    "coffee": 500,
}

money=0
is_on=True

def enough_ingredients(item):
    is_enough=True
    for key in item:
        if item[key]>=resources[key]:
            print(f"sorry there is not enough {key}")
            is_enough= False
    return is_enough

def inserted_money():
    print("how much money do you have")
    total=int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennes?: ")) * 0.01
    return total

def transation_successful(money_received,drink_cost):
    if money_received>drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"here is ${change} in change")
        global money
        money+=drink_cost
        return True
    else:
        print("you don't inserted enough money")
        return False

def order(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here is your {drink_name} enjoy ☕")

while is_on:
  choice=input("what would you like? (espresso/latte/cappuccino)")

  if choice=="off":
      is_on=False
  elif choice=="report":
    print(f"water:{resources['water']}ml\nmilk:{resources['milk']}ml\ncoffee:{resources['coffee']}ml\nmoney:${money}")
  else:
      drink=MENU[choice]
      if enough_ingredients(drink['ingredients']):
          payment= inserted_money()
          if transation_successful(payment,drink['cost']):
              order(choice,drink["ingredients"])

