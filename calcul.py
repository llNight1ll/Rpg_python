
base_health = 10
a = base_health
i = 2
while i < 20 :
    #a = round(( (2 * base_health)* (i + 1) )/100 + i*5 + 10 + base_health)
    a += round(i/(i-1) * base_health/4 + i)
    print(a, i)
    i += 1

