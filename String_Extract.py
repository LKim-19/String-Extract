text = "X-DSPAM-Confidence:    0.8475"

# Helps find where it starts. 23 for 0 and 28 for 5
x = text.find("0")
y = text.find("5")

# Splits 0.8475 for position 23 (0) to the end
a = float(text[x:y+1])
print(a)