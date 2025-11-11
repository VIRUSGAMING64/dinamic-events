import os
x=os.system("bash ./clean.sh")
if x != 0 and x != 256:
    raise Exception(f"error exit code:{[x]}")