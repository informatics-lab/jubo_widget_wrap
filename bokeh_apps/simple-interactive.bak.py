from jubo import interact
from jubo import widgets
import math

ops = ["square", "root", "factorial"]


def calc(num, op, msg=""):
    result = "NaN"
    if op == "square":
        result = str(num * num)
    elif op == "root":
        result = str(math.sqrt(num))if num > 0 else "NaN"
    elif op == "factorial":
        result = str(math.factorial(num)) if num >= 1 else "NaN"

    msg = "%s %s" % (msg, result)
    return msg.strip()


interact(calc,
         msg="Your result is",
         num=widgets.IntSlider(min=-10, max=30, step=1, value=10),
         op=widgets.Dropdown(description="Function:", options=ops, value=ops[0]))
