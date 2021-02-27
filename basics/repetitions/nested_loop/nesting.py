# ask user for seq and marker
print("please enter a seq:")
seq = input()
print("\nplease enter a the character for the marker:")
marker = input()

#find markers
m1_p = -1
m2_p = -1

for p in range(0, len(seq), 1):
  l = seq[p]

  if (l == marker):
    if (m1_p == -1):
        m1_p = p
    else:
      m2_p = p

print(f"The distance between the markers is {m2_p - m1_p - 1}.")