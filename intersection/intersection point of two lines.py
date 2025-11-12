import math


def ToRadians(angle: float) -> float:
    return angle * (math.pi / 180)


def GetSecondPoint(point: list[float],
                    angle: float) -> list[float]:
    adjacent = 5
    opposite = adjacent * math.tan(ToRadians(90 - abs(angle)))

    # this depends on if angle is negative or not. negative = - , positive = +
    if angle > 0:
        x = point[0] + 5
    else:
        x = point[0] - 5
    y = point[1] + round(opposite, 1)
    print([x, y])
    return [x, y]


def GetGradient(point1: list[float], point2: list[float]) -> float:
    return ((point1[1] - point2[1]) / (point1[0] - point2[0]))


def GetLineEquation(point, gradient):
    y_intercept = point[1] - (gradient * point[0])
    equation = f'y = {gradient}x + {y_intercept}'
    return equation

def Main(first, second, firstAngle, secondAngle):
    firstLineStart = first
    firstLineEnd = GetSecondPoint(firstLineStart, firstAngle)
    firstGradient = GetGradient(firstLineStart, firstLineEnd)
    eq_1 = GetLineEquation(firstLineStart, firstGradient)

    secondLineStart = second
    secondLineEnd = GetSecondPoint(secondLineStart, secondAngle)
    secondGradient = GetGradient(secondLineStart, secondLineEnd)
    eq_2 = GetLineEquation(secondLineStart, secondGradient)

    simeq = eq_1[4:] + " = " + eq_2[4:]
    simeq_split = simeq.split()
    first_side = [simeq_split[0], simeq_split[1] + simeq_split[2]]
    second_side = [simeq_split[4], simeq_split[5] + simeq_split[6]]
    number = eval(first_side[1] + "-" + second_side[1])
    x = eval(second_side[0][:-1] + "-" + first_side[0][:-1])

    x = number / x
    y = eval("("+''.join(eq_1.split()[2:]).replace("x", "*"+str(x)+")"))

    print(f'x = {x}, y = {y}')
    print(f'x = {round(x, 2)}, y = {round(y, 2)}')
    print(f'({x}, {y})')


Main([10,10], [20,5], 6.34019174591, -4.763641690726)
