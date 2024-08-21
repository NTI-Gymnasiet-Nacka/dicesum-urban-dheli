# Dice sum probability calculator
# Författare: Alfred Lundström
# Datum: 2024-08-21

def main():
    user_input = input().split(" ")
    sums = {}
    
    for i in range(1, int(user_input[0]) + 1):
        for j in range(1, int(user_input[1]) + 1):
            if i+j in sums:
                sums[i+j] += 1
            else:
                sums[i+j] = 1
                
    max_value = max(sums.values())
    for i in sums:
        if sums[i] == max_value:
            print(i)
          
if __name__ == "__main__":
    main()