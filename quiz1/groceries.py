def checkout(cash: float, list: dict) -> float:
    """
    build a function that sums up the value of the grocery list and subtracts that
    from the cash passed into the function.
    return the "change" from the cash minus the total groceries value.
    """
    # values = list.values()
    total = sum(list.values())
    change = cash - total
    return change

    # pass  # implement me
# groc_dict = {
#             'oatmeal': 4.59,
#             'beefroast': 12.56,
#             'cottagecheese': 3.99,
#             'yogurt': 3.19,
#             'nuts': 15.99,
#             'bread': 4.99,
#         }
# checkout(100, groc_dict)