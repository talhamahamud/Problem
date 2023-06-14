def compound_interest(p, t, r, n):
    return p*((1 + (r/n))**(n*t))

print(compound_interest(10000, 10, 0.06, 12))