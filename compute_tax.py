status = eval(input("1: for single, 2: for married jointly, 3: married separately, 4: head of household: "))
income = eval(input("enter you income: "))
tax = 0
if status == 1:
    if income <= 8350:
        tax = income * 0.10
    elif tax <= 33950:
        tax = (8350 * 0.10) + ((income - 8350) * 0.15)
    elif tax <= 82550:
        tax = (8350 * 0.10) + ((33950 - 8350) * 0.15) + ((income - 33950) * 0.25)
    elif tax <= 171550:
        tax = (8350 * 0.10) + ((33950 - 8350) * 0.15) + ((82550 - 33950) * 0.25) + ((income - 82550) * 0.28)
    elif tax <= 372950:
        tax = (8350 * 0.10) + ((33950 - 8350) * 0.15) + ((82550 - 33950) * 0.25) - ((171550 - 82550) * 0.28) + ((income - 171550) * 0.33)
    else:
        tax = (8350 * 0.10) + ((33950 - 8350) * 0.15) + ((82550 - 33950) * 0.25) - ((171550 - 82550) * 0.28) + (
                    (372950 - 171550) * 0.33) + ((income - 372950) * 0.35)
elif status == 2:
    if income <= 16700:
        tax = 16700 * 0.10
    elif income <= 67900:
        tax = (16700 * 0.10) + ((income - 16700) * 0.15)
    elif income <= 137050:
        tax = (16700 * 0.10) + (67900 * 0.15) + ((income - 67900) * 0.25)
    elif income <= 137050:
        tax = (16700 * 0.10) + (67900 * 0.15) + (137900 * 0.25) + ((income - 137050) * 0.28)
    elif income <= 208850:
        tax = (16700 * 0.10) + (67900 * 0.15) + (137900 * 0.25) + (137050 * 0.28) + ((income - 137050) * 0.33)
    elif income <= 372950:
        tax = (16700 * 0.10) + (67900 * 0.15) + (137900 * 0.25) + (137050 * 0.28) + (372950 * 0.33) + ((income - 208850) * 0.35)
    else:
        tax = (16700 * 0.10) + (67900 * 0.15) + (137900 * 0.25) + (137050 * 0.28) + (372950 * 0.33) + \
              (208850 * 0.35) + ((income - 372050) * 0.35)

elif status == 3:
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = (8350 * 0.10) + ((income - 8350) * 0.15)
    elif income <= 68525:
        tax = (8350 * 0.10) + (33950 * 0.15) + ((income - 33950) * 0.25)
    elif income <= 104425:
        tax = (8350 * 0.10) + (33950 * 0.15) + (33950 * 0.25) + ((income - 33950) * 0.28)
    elif income <= 186475:
        tax = (8350 * 0.10) + (33950 * 0.15) + (33950 * 0.25) + (33950 * 0.28) + ((income - 33950) * 0.33)
    else:
        tax = (8350 * 0.10) + (33950 * 0.15) + (33950 * 0.25) + (33950 * 0.28) + (186475 * 0.35) + ((income - 186475) * 0.10)

elif status == 4:
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = (11950 * 0.10) + ((income - 11950) * 0.15)
    elif income <= 117450:
        tax = (11950 * 0.10) + (45500 * 0.15) + ((income - 45500) * 0.20)
    elif income <= 190200:
        tax = (11950 * 0.10) + (45500 * 0.15) + (117450 * 0.20) + ((income - 117450) * 0.33)
    elif income <= 372950:
        tax = (11950 * 0.10) + (45500 * 0.15) + (117450 * 0.20) + (190200 * 0.25) + ((income - 190200) * 0.33)
    else:
        tax = (11950 * 0.10) + (45500 * 0.15) + (117450 * 0.20) + (190200 * 0.25) + (372950 * 0.33) + ((income - 372950) * 0.35)
print(tax)