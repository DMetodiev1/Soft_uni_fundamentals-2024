flag = False

for h in range(24):
    for m in range(60):
        if h == 5 and m == 31:
            flag = True # вместо това може и exit()
            break # вместо това може и exit()
        print(F"{h}:{m:02d}")

    if flag:
        break
