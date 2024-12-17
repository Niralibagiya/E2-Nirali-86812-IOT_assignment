def comp_int(principle,rate,time):
    amount = principle*(pow((1+rate/100),time))
    CI = amount-principle
    print(f"Compound interest = {CI}")

comp_int(10000,10,5)
