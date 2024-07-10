class PrimeFactor:
    def __init__(self):
        self.factors = []

    def of(self, number) -> []:
        self.factors.clear()
        self.dfs(number, 2)
        return self.factors

    def dfs(self, number, divisor):
        if number == 1:
            return
        if number % divisor == 0:
            self.factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
        self.dfs(number, divisor)
