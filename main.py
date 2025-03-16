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

print("\n(Mark Managbanag) What is the remainder of 5 × 5 % 6?")
print("a) 0               b) 2")
print("c) 1               d) 3")

answer = input("Enter your answer: ")

if answer.upper() == "C":
    total_score += 1
    print("Great Job!")
else: 
    print(f"{answer} is incorrect. The correct answer is C.")

print("\n(Angella Jane Raymundo) What do plants need for photosynthesis?")
print("a) Oxygen              b) Sunlight")
print("c) Rocks               d) Iron")

answer = input("Enter your answer: ")

if answer.upper() == 'B':
    total_score += 1
    print("You got it! The answer is B.")
else:
    print(f"{answer} is incorrect. The correct answer is B.")

# TODO(Espinola): Add fifth question and print total score 