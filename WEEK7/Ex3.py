import sys

if len(sys.argv) != 3:
    print("Usage: python3 Ex3.py <in> <out>")
    sys.exit(1)

in_file = sys.argv[1]
out_file = sys.argv[2]

products = []

try:
    with open(in_file, "r") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            if len(parts) != 2:
                raise ValueError
            product = parts[0].strip()
            price = parts[1].strip()

            try:
                price = float(price)
            except ValueError:
                raise ValueError

            if price >= 10:
                products.append((product, price))
except FileNotFoundError:
    print(f"File {in_file} not found")
    sys.exit(1)
except ValueError:
    print(f"Invalid price in line {line_num}")
    sys.exit(1)


products.sort(key=lambda x: x[0])

with open(out_file, "w") as f:
    for product, price in products:
        f.write(f"{product}: {price}\n")