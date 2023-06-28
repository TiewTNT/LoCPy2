# ========= IMPORTANT =========
#
#   USE PYTHON VERSION >=3.11
#       CODE CONTAINS :=
#

class Monomial:
    def __init__(self, abs_cooefficient: int | float, degrees: list):
        self.abs_coefficient = abs_cooefficient
        self.degrees = degrees

    def is_monomial(self):
        for i in self.degrees:
            if i < 0 or int(i) != i:
                return False
            
        return True

    def get_max_degrees(self):
        return max(self.degrees)
    
    def is_constant(self):
        return all([x == 0 for x in self.degrees])
    
    def number_of_degrees(self):
        return len(self.degrees)
    
    def __str__(self):
        if self.is_constant():
            return str(self.abs_coefficient)
        
        return str(self.abs_coefficient) + ''.join(['x_' + str(i) +
                ('^' + str(self.degrees[i])).replace('^1', '') for i in range(len(self.degrees))])
    

def is_similar(mon1: Monomial, mon2: Monomial):
    return len(mon1.degrees) == len(mon2.degrees)

def combine_monomials(mon1: Monomial, mon2: Monomial):
    if not is_similar(mon1, mon2):
        return None
    return Monomial(mon1.abs_coefficient + mon2.abs_coefficient,
                    [x + y for x, y in zip(mon1.degrees, mon2.degrees)])

def product_monomials(mon1: Monomial, mon2: Monomial):
    for _ in range(diff := (max(len(mon1.degrees), len(mon2.degrees)) -
                            min(len(mon1.degrees), len(mon2.degrees)))):
        (minmon := min([mon1.degrees, mon2.degrees], key=len)).append(0)

    mul_degrees = []

    for x, y in zip(mon1.degrees, mon2.degrees):
        mul_degrees.append((x + y))

    for _ in range(diff):
        minmon.pop()

    return Monomial(mon1.abs_coefficient * mon2.abs_coefficient, mul_degrees)

def smallest_multiple_for_perfect_square(n):
    for i in range(2, int(n ** 0.5) + 1):
        if (n * i) ** 0.5 % 1 == 0:
            return i
    return n


print(product_monomials(Monomial(-0.5, [1, 2, 5, 9 , 5 , 7 , 4]), Monomial(-0.5, [7, 1])))
print(smallest_multiple_for_perfect_square(32))