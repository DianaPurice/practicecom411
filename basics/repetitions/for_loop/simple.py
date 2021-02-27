# ask user for a number of mountains
print("How many mountains should I display?")
mountains = int(input())

# display mountains
print("\nDisplaying...")

for mountain in range(mountains):
  print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\
  """)