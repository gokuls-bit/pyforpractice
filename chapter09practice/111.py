# f = open(poem.txt)
# c = f.read()
# if ("twinkle" in content ):
#     print("yeah baby")

# else: 
#     p    
# f.close()

# import random

# def game():
#     print("You are playing")
#     score = random.randint(1, 62)

#     try:
#         with open("hiscore.txt", "r") as f:
#             hiscore_str = f.read().strip()
#             hiscore = int(hiscore_str) if hiscore_str else 0
#     except FileNotFoundError:
#         hiscore = 0

#     print(f"Your score: {score}")
    
#     if score > hiscore:
#         print("New high score!")
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))
#     else:
#         print(f"High score remains: {hiscore}")
    
#     return score

# game()

# import os

# def generate_table(n): # Renamed function for clarity and consistency
#     """
#     Generates a multiplication table for a given number 'n'
#     and saves it to a file in the 'tables' directory.
#     """
#     table_content = ""
#     for i in range(1, 11):
#         table_content += f"{n} * {i} = {n * i}\n"

#     # Ensure the 'tables' directory exists
#     os.makedirs("tables", exist_ok=True)

#     # Open the file in write mode ('w')
#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table_content)

# # Generate tables for numbers 2 to 20
# for i in range(2, 21):
#     generate_table(i)

# print("Multiplication tables generated successfully in the 'tables' directory!")

word = "donkey"

with open("file.txt","r")as f:
    content=f.read()

contentNew = content.replace( word ,"fuck")
with open("file.txt" ,"w") as f:
    f.write(contentNew)