print("===== STUDENT UTILITY TOOLKIT =====")

while True:

    print("""
1. Find Largest Number
2. Check Pass/Fail
3. Spam Message Detector
4. Name Checker
5. Grade Calculator
6. Personality Checker
7. Username Validator
8. Exit
""")

    choice = input("Enter your choice: ")

    # 1. Largest Number
    if choice == "1":

        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        n3 = int(input("Enter third number: "))
        n4 = int(input("Enter fourth number: "))

        largest = max(n1, n2, n3, n4)

        print("Largest number is:", largest)

    # 2. Pass/Fail Checker
    elif choice == "2":

        n1 = int(input("Enter marks of subject 1: "))
        n2 = int(input("Enter marks of subject 2: "))
        n3 = int(input("Enter marks of subject 3: "))

        average = (n1 + n2 + n3) / 3

        print("Average Marks:", average)

        if n1 >= 33 and n2 >= 33 and n3 >= 33 and average >= 40:
            print("✅ You Passed")
        else:
            print("❌ You Failed")

    # 3. Spam Detector
    elif choice == "3":

        spam_words = ["make a lot of money", "buy now", "subscribe this", "click this"]

        message = input("Enter message: ").lower()

        is_spam = False

        for word in spam_words:
            if word in message:
                is_spam = True

        if is_spam:
            print("⚠️ Spam Message Detected")
        else:
            print("✅ Safe Message")

    # 4. Name Checker
    elif choice == "4":

        names = [
            "Rahul Sharma",
            "Ananya Verma",
            "David Johnson",
            "Priya Kapoor",
            "Michael Lee"
        ]

        name = input("Enter name: ")

        if name in names:
            print("✅ Name Found")
        else:
            print("❌ Name Not Found")

    # 5. Grade Calculator
    elif choice == "5":

        marks = int(input("Enter your marks: "))

        if 90 <= marks <= 100:
            print("Grade: EX")
        elif 80 <= marks < 90:
            print("Grade: A")
        elif 70 <= marks < 80:
            print("Grade: B")
        elif 60 <= marks < 70:
            print("Grade: C")
        elif 50 <= marks < 60:
            print("Grade: D")
        else:
            print("Grade: F")

    # 6. Personality Checker
    elif choice == "6":

        qualities = {
            "muskan",
            "brahmin",
            "sant",
            "punjabi",
            "tech"
        }

        message = input("Enter message: ").lower()

        found = False

        for value in qualities:
            if value in message:
                found = True

        if found:
            print("🔥 Personality Matched")
        else:
            print("❌ No Match Found")

    # 7. Username Validator
    elif choice == "7":

        user = input("Enter username: ")

        if len(user) < 10:
            print("✅ Valid Username")
        else:
            print("❌ Username should be less than 10 characters")

    # 8. Exit
    elif choice == "8":

        print("👋 Exiting Program...")
        break

    else:
        print("❌ Invalid Choice")
