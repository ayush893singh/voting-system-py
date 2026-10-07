Ravi = 0
Aman = 0
Ayush = 0

print("===== Voting System =====")

voters = int(input("Enter number of voters: "))

for i in range(voters):

    print(f"\nVoter {i+1}")

    print("1. Ravi")
    print("2. Aman")
    print("3. Ayush")

    vote = input("Cast your vote (1-3): ")

    if vote == "1":
        Ravi += 1
        print("Vote recorded successfully!")

    elif vote == "2":
        Aman += 1
        print("Vote recorded successfully!")

    elif vote == "3":
        Ayush += 1
        print("Vote recorded successfully!")

    else:
        print("Invalid vote!")

print("\n===== Election Result =====")

print(f"Ravi : {Ravi} Vote(s)")
print(f"Aman  : {Aman} Vote(s)")
print(f"Ayush : {Ayush} Vote(s)")

if Ravi > Aman and Ravi > Ayush:
    print("\nWinner: Ravi")

elif Aman > Ravi and Aman > Ayush:
    print("\nWinner: Aman")

elif Ayush > Ravi and Ayush > Aman:
    print("\nWinner: Ayush")

else:
    print("\nResult: Tie")
