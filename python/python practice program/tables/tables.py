for i in range (2,21):
    with open(f"table_of_{i}.txt",'w') as f:
        for t in range (1,11):
            f.write(f"\n{i}x{t}={i*t}")
