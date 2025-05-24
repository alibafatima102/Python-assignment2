def main():
    counts = {}
    
    while True:
        value = input("Enter a number: ")
        if value == "":
            break
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    for key in counts:
        print(f"{key} appears {counts[key]} times.")

if __name__ == "__main__":
    main()
