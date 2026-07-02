#!/usr/bin/python3
import sys
from decimal import Decimal

ZERO = Decimal("0.0")

def main():
    if len(sys.argv) != 3:
        sys.exit(1)
    try:
        threshold = Decimal(sys.argv[1])
        limit = Decimal(sys.argv[2])
        total = ZERO
        outputs = []
        #Iterating over inputs
        for line in sys.stdin:
            remaining = limit - total
            #If we reach limit, return 0s quickly. No need for doing math
            if remaining == ZERO:
                output = ZERO
            else:    
                #Inputs will not have precision beyond the tenths place, so rounding should be unnecessary.
                input = Decimal(line)
                excess = max(ZERO, input - threshold)
                output = min(excess, remaining)
            outputs.append(output)
            total += output

        outputs.append(total)

        for output in outputs:
            #Decimal precision must be accurate to the tenths place
            print(str(output.quantize(Decimal("0.1"))))
    except Exception as e:
        #Just a way to not print anything else than numbers case of exceptions for improper input values
        sys.exit(1)

if __name__ == "__main__":
    main()
