rahul = 0
aman = 0
priya = 0

print("===== Voting System =====")

voters = int(input("Enter number of voters: "))

for i in range(voters):

    print(f"\nVoter {i+1}")

    print("1. Rahul")
    print("2. Aman")
    print("3. Priya")

    vote = input("Cast your vote (1-3): ")

    if vote == "1":
        rahul += 1
        print("Vote recorded successfully!")

    elif vote == "2":
        aman += 1
        print("Vote recorded successfully!")

    elif vote == "3":
        priya += 1
        print("Vote recorded successfully!")

    else:
        print("Invalid vote!")

print("\n===== Election Result =====")

print(f"Rahul : {rahul} Vote(s)")
print(f"Aman  : {aman} Vote(s)")
print(f"Priya : {priya} Vote(s)")

if rahul > aman and rahul > priya:
    print("\nWinner: Rahul")

elif aman > rahul and aman > priya:
    print("\nWinner: Aman")

elif priya > rahul and priya > aman:
    print("\nWinner: Priya")

else:
    print("\nResult: Tie")