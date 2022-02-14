word = "Hello World"
stack = []

for c in word:
  stack.append(c)

output = ""
while stack:
  output += stack.pop()
print(output)