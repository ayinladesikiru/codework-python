# amount = int(input("Enter amount: "))
# rate = int(input("Enter rate: "))
# years = int(input("Enter number of: "))


def invest(amount: int, rate: int, years: int):
    """
    function that calculate rate earning per year
    :param amount:
    :param rate:
    :param years:
    :return:
    """
    for i in range(years):
        rates = amount / 100 * rate
        amount += rates
        print(f"year {i}: earnings is {amount:.2f}")


print(invest(100, 5, 4))

