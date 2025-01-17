


def derivative(list):
    derivatives = {
        "exp" : exponent,
        "cons" : constant
    }
    
    ans = 0
    cache = []
    for i in list:
        if i in derivatives.keys():
            if i == "exp":
                ans += derivatives[i](cache[0], cache[1])
                cache.pop(0)
                cache.pop(0)
            else:
                ans += derivatives[i](cache[0])
                cache.pop(0)
        else:
            cache.append(i)
    return ans

def constant (val):
    return 0

def exponent(val, exp):
    return exp* (val ** (exp-1))

print(derivative([2,3,"exp"]))





 