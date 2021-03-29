"""Solving a system of non-linear ... with Newton method"""
import numpy as np
import sympy as sym


class NewtonIterative:

    def __init__(self, vars, eq):
        self.eq = eq
        self.vars = vars
        self.t = type(eq)

    def cul_function(self, val1, val2):
        x1 = val1
        x2 = val2
        temp = []
        temp.append(eval(self.eq[0]))
        temp.append(eval(self.eq[1]))
        return temp

    @property
    def Jacobian(self):
        vars = sym.symbols(self.vars)
        f = sym.sympify(self.eq)
        J = sym.zeros(len(f), len(vars))
        for i, fi in enumerate(f):
            for j, s in enumerate(vars):
                J[i, j] = sym.diff(fi, s)
        return J

    def calculate_jacobian(self, val1, val2):
        arr = []
        x1 = val1
        x2 = val2
        for i in range(len(self.Jacobian)):
            arr.append(eval(str(self.Jacobian[i])))
        for i in range(4):
            arr[i] *= -1

        arr1 = np.array(arr)
        return np.reshape(arr1, (2, 2))

    @staticmethod
    def x_delta_by_gauss(J, b):
        return np.linalg.solve(J, b)

    @staticmethod
    def x_plus_1(x_delta, x_previous):
        x_next = x_previous + x_delta

        return x_next

    def newton_method(self, x_init):
        first = x_init[0]

        second = x_init[1]

        jacobian = self.calculate_jacobian(first, second)

        vector_b_f_output = self.cul_function(first, second)

        x_delta = self.x_delta_by_gauss(jacobian, vector_b_f_output)

        x_plus_1 = x_delta + x_init

        return x_plus_1

    def iterative_newton(self, x_init):
        counter = 0

        x_old = x_init
        print("x_old", x_old)
        x_new = self.newton_method(x_old)
        print("x_new", x_new)

        diff = np.linalg.norm(x_old - x_new)

        while diff > 0.0001:
            counter += 1

            print("x_old", x_old)
            x_new = self.newton_method(x_old)
            print("x_new", x_new)

            diff = np.linalg.norm(x_old - x_new)
            print(diff)

            x_old = x_new

        convergent_val = x_new
        print(counter)

        return convergent_val


if __name__ == '__main__':

    n_i = NewtonIterative('x1 x2',
                          ['(-1) * (x2 ** 2 - x1 ** 2 - 0.52)', '(-1) * (0.1 * x2 ** 2 + 4 * x2 + x2 * x1 ** 2 - 8.1)'])
    print(n_i.iterative_newton([1, 1]))


