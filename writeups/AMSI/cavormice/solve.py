from itertools import product

to_get = [0x19, 0x08, 0x16, 0x07, 0x00, 0x11, 0x1e]

directions = {
  "U" : 0x55,
  "D" : 0x44,
  "R" : 0x52,
  "L" : 0x4C
}

xor_values = {}

for a,b in product(directions.values(), repeat=2):
	r = a^b 
	if r in to_get:
		pair = chr(a)+chr(b)
		xor_values[pair] = hex(r)

xor_values.pop("UU")
xor_values.pop("UR")
xor_values.pop("UD")

password = bytes.fromhex("191908160700191108161119001E0711")

result = ""

for val in password:
	if result == "":
		result += "UL"
		xor_values.pop("UL")
		continue
	
	for i in xor_values.items():
		if int(i[1], 16) == val:
			result += i[0]
			break

print(result)
