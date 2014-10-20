class Fraction():
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator
    def __str__(self):
        return "{} / {}".format(self.numerator, self.denumerator)

    def simplify_fraction(fraction):
        nominator = fraction.numerator
        denominator = fraction.denumerator
        r = 0
        mcd = 0
        while denominator != 0:
            r = nominator % denominator;
            nominator = denominator;
            denominator = r;
        mcd = nominator
        return Fraction(fraction.numerator / mcd,fraction.denumerator / mcd)


    def sum(f1, f2):
        denum = f1.denumerator*f2.denumerator
        numer = f1.denumerator*f2.denumerator*f1.numerator + f1.denumerator*f2.denumerator*f2.numerator
        return simplify_fraction (Fraction(numer,denum))





f1 = Fraction(3,9)
f2 = Fraction(1,3)

print (Fraction.sum(f1.f2))
