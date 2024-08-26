def order_food(min_order, *args): # Variable with arguments
    print(f"You have ordered {min_order}")
    print("Your Order will be delivered in 30 mins:")
    print(args)
    for items in args:
        print(f"You have ordered {items}")
    print("Your Order will be delivered in 30 mins:")
    print("Enjoy your meal")
order_food("Salad","Pizza","Biryani","Juice")

#kw arg
time-activity(10,20,30,40, hobby="Reading", sport="Boxing", fun="Driving", work="Devops", hangout="Friends")

