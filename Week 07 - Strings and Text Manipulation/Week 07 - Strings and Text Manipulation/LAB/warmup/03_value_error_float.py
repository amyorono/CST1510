# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

raw_line = "srv-01,used=unknown,total=100"
hostname_part, rest = raw_line.split(",", 1)

for piece in rest:
    key, value = piece.split("=", 1)
    print(key, float(value))
