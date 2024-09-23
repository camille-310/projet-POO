#!/bin/env python3
import sys, re, Module

def tri(l):
    """
    Cette fonction rÃ©cursive tri la liste passÃ©e en argument.
    """
    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)


if __name__=="__main__":
    # programme principal
    l = Module.module()
    tri(l)
    print(f"{l=}")
