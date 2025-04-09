# 6. Return a Function – Multiplier
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply