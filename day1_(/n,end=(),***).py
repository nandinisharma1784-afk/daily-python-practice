q1.
for row in range(1, 4):         #outer loop (rows)
    for col in range(1, 4):      # Inner loop (Columns)
        
        # 1. 'f' injects the row and col numbers into the text
        # 2. end="\t" puts a tab space after it so columns line up cleanly
        print(f"({row},{col})",end=("\t"))
        
    # This empty print() runs ONLY after the inner loop finishes a row.
    # It has no custom 'end', so it uses the default end="\n" to press Enter.
    print()



q2for i in range(1,6):
  for j in range(2,6):
    print((f"({i}^{j})"),end=(" "))
  print() 
  print("*"*100)