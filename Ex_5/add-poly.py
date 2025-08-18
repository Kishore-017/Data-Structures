class TermNode:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next_term = None

class LinkedPolynomial:
    def __init__(self):
        self.start = None

    def add_term(self, coefficient, exponent):
        if coefficient == 0:
            return
        new_term = TermNode(coefficient, exponent)
        if not self.start or self.start.exponent < exponent:
            new_term.next_term = self.start
            self.start = new_term
        else:
            current = self.start
            previous = None
            while current and current.exponent >= exponent:
                if current.exponent == exponent:
                    current.coefficient += coefficient
                    return
                previous = current
                current = current.next_term
            new_term.next_term = current
            previous.next_term = new_term

    def add_polynomial(self, other_poly):
        result_poly = LinkedPolynomial()
        p1 = self.start
        p2 = other_poly.start

        while p1 and p2:
            if p1.exponent == p2.exponent:
                result_poly.add_term(p1.coefficient + p2.coefficient, p1.exponent)
                p1 = p1.next_term
                p2 = p2.next_term
            elif p1.exponent > p2.exponent:
                result_poly.add_term(p1.coefficient, p1.exponent)
                p1 = p1.next_term
            else:
                result_poly.add_term(p2.coefficient, p2.exponent)
                p2 = p2.next_term

        while p1:
            result_poly.add_term(p1.coefficient, p1.exponent)
            p1 = p1.next_term

        while p2:
            result_poly.add_term(p2.coefficient, p2.exponent)
            p2 = p2.next_term

        return result_poly

    def show_polynomial(self):
        current = self.start
        if not current:
            print("0")
            return
        parts = []
        while current:
            if current.coefficient != 0:
                part = (f"{current.coefficient}x^{current.exponent}" if current.exponent != 0 
                        else f"{current.coefficient}")
                parts.append(part)
            current = current.next_term
        print(" + ".join(parts))

def get_polynomial_from_user():
    poly = LinkedPolynomial()
    term_count = int(input("Number of terms you want to enter: "))
    print("Input each term as: coefficient exponent")
    for _ in range(term_count):
        coef, exp = map(int, input("Term: ").split())
        poly.add_term(coef, exp)
    return poly

print("Create first polynomial:")
first_poly = get_polynomial_from_user()

print("\nCreate second polynomial:")
second_poly = get_polynomial_from_user()

print("\nFirst polynomial:")
first_poly.show_polynomial()
print("Second polynomial:")
second_poly.show_polynomial()

sum_poly = first_poly.add_polynomial(second_poly)
print("Sum of the two polynomials:")
sum_poly.show_polynomial()
