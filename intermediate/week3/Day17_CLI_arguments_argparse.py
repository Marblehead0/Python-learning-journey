import argparse

def calc(a: float, b:float, op:str) -> float:
    if op == "add": return a + b
    if op == "sub": return a - b
    if op == "mul": return a * b
    if op == "div": return a / b
    raise ValueError("Uknown OP")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="CLI calc")
    p.add_argument("a",type=float)
    p.add_argument("b",type=float)
    p.add_argument("--op",choices=["add","sub","mul","div"], default="add")
    args = p.parse_args()
    print(calc(args.a,args.b, args.op))