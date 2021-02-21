# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight/height ** 2
result = int(bmi)
final_result = round(result)

if final_result < 18.5:
  print(f"You BMI is {final_result}, you are underweight")
elif final_result > 18.5 and final_result < 25:
  print(f"You BMI is {final_result}, you are normal weight")
elif final_result > 25 and final_result < 30:
  print(f"You BMI is {final_result}, you are overweight")
elif final_result > 30 and final_result < 35:
  print(f"You BMI is {final_result}, you are obese")
elif final_result > 35:
  print(f"You BMI is {final_result}, you are clinically obese")

