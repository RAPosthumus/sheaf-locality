#!/usr/bin/env python3
import argparse, math, sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

def debruijn_count(q,n):
    return (math.factorial(q) ** (q ** (n-1))) // (q ** n)

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--q", type=int, default=2)
    p.add_argument("--n", type=int, default=6)
    args=p.parse_args()
    print(debruijn_count(args.q,args.n))
