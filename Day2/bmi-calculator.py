#Ask user to input height in m
height = float(input("enter your height in m: ")) #eg. 1.65
#Ask user to input weight in kg
weight = float(input("enter your weight in kg: ")) #eg. 84


#Calculate BMI by dividing weight by height and multiplying by 2

#weight divided by height then sqaue the result
bmi = weight/(height**2)

print(bmi)#correct answer but with too many decimal places
print(int(bmi))#flooring occurs where decimal point are simply removed
print(round(bmi, 2))#the round function will round to 2 decimal places 30.85
print(round(bmi, 5))#rouns to 5 decimal places 30.85399
