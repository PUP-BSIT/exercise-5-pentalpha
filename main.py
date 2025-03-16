total_score = 0

print("(John Matthew Bautista) What is the center of the earth called?")
print("a) Core                  b) Mantle")
print("c) Moho                  d) Crust")

answer = input("Enter your answer: ")

if answer.upper() == 'A':
    total_score += 1
    print("Correct!, the answer is A.")
else:
    print(f"{answer} is incorrect. The correct answer is A.")

print("\n(Gabrielle Banzali) What is the capital of France?")
print("a) Madrid                b) London")
print("c) Berlin                d) Paris")

answer = input("Enter your answer: ")

if answer.upper() == "D":
    total_score += 1
    print("Well done! The answer is D.")
else: 
    print(f"{answer} is incorrect. The correct answer is D.")

# TODO(Managbanag): Add third question

# TODO(Raymundo): Add fourth question

# TODO(Espinola): Add fifth question and print total score