import statistics as st
import sys

def main():
    type = input("action")

    if type.lower() == "conversion":
        convert = input("from")
        to = input("to")
        if convert.lower() == "inches" and to.lower() == "centimeters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*2.54,2)
                print(f"{val} inches is {result}cm")
        elif convert.lower() == "centimeters" and to.lower() == "inches":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/2.54,2)
                print(f"{val}cm is {result} inches")
        elif convert.lower() == "meters" and to.lower() == "centimeters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*100,2)
                print(f"{val} meters is {result} centimeters")
        
        elif convert.lower() == "centimeters" and to.lower() == "meters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/100,2)
                print(f"{val} centimeters is {result} meters")
        
        elif convert.lower() == "centimeters" and to.lower() == "kilometers":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/100000,10)
                print(f"{val} centimeters is {result} kilometers")

        elif convert.lower() == "kilometers" and to.lower() == "centimeters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*100000,2)
                print(f"{val} kilometers is {result} centimeters")
        
        elif convert.lower() == "centimeters" and to.lower() == "millimeters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*10,2)
                print(f"{val} centimeters is {result} millimeters")
        
        elif convert.lower() == "millimeters" and to.lower() == "centimeters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/10,2)
                print(f"{val} millimeters is {result} centimeters")
        
        elif convert.lower() == "millimeters" and to.lower() == "meters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/1000,2)
                print(f"{val} millimeters is {result} meters")
                
        elif convert.lower() == "meters" and to.lower() == "millimeters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*1000,2)
                print(f"{val} meters is {result} millimeters")

        elif convert.lower() == "millimeters" and to.lower() == "kilometers":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/1000000,5)
                print(f"{val} millimeters is {result} kilometers")

        elif convert.lower() == "kilometers" and to.lower() == "millimeters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*1000000,2)
                print(f"{val} millimeters is {result} meters")

        elif convert.lower() == "centimeters" and to.lower() == "feet":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*0.0328084,2)
                print(f"{val} centimeters is {result} feet")
        
        elif convert.lower() == "feet" and to.lower() == "centimeters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*30.48,2)
                print(f"{val} feet is {result} centimeters")

        elif convert.lower() == "centimeters" and to.lower() == "yards":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*0.0109361,5)
                print(f"{val} centimeters is {result} yards")

        elif convert.lower() == "yards" and to.lower() == "centimeters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*91.44,5)
                print(f"{val} yards is {result} centimeters")
        
        elif convert.lower() == "centimeters" and to.lower() == "miles":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/160934,5)
                print(f"{val} centimeters is {result} miles")
        
        elif convert.lower() == "miles" and to.lower() == "centimeters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*160934,5)
                print(f"{val} miles is {result} centimeters")
        
        elif convert.lower() == "meters" and to.lower() == "inches":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*39.3701,2)
                print(f"{val} yards is {result} centimeters")
        
        elif convert.lower() == "inches" and to.lower() == "meters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/39.3701,5)
                print(f"{val} inches is {result} meters")

        elif convert.lower() == "meters" and to.lower() == "yards":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*1.09361,5)
                print(f"{val} meters is {result} yards")
        
        elif convert.lower() == "yards" and to.lower() == "meters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/1.09361,5)
                print(f"{val} yards is {result} meters")

        elif convert.lower() == "meters" and to.lower() == "miles":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/1609,5)
                print(f"{val} meters is {result} miles")

        elif convert.lower() == "miles" and to.lower() == "meters":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*1609,5)
                print(f"{val} miles is {result} meters")

        elif convert.lower() == "kilometers" and to.lower() == "inches":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*39370.1,5)
                print(f"{val} kilometers is {result} inches")
        
        elif convert.lower() == "inches" and to.lower() == "kilometers":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/39370.1,5)
                print(f"{val} inches is {result} kilometers")
        
        elif convert.lower() == "kilometers" and to.lower() == "yards":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*1093.61,2)
                print(f"{val} kilometers is {result} yards")

        elif convert.lower() == "yards" and to.lower() == "kilometers":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/1093.61,5)
                print(f"{val} yards is {result} kilometers")

        elif convert.lower() == "kilometers" and to.lower() == "miles":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/1.609,5)
                print(f"{val} kilometers is {result} miles")

        elif convert.lower() == "miles" and to.lower() == "kilometers":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*1.609,5)
                print(f"{val} miles is {result} kilometers")

        elif convert.lower() == "inches" and to.lower() == "feet":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/12,2)
                print(f"{val} inches is {result} feet")
        
        elif convert.lower() == "feet" and to.lower() == "inches":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*12,2)
                print(f"{val} feet is {result} inches")

        elif convert.lower() == "inches" and to.lower() == "yards":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/36,2)
                print(f"{val} inches is {result} yards")

        elif convert.lower() == "yards" and to.lower() == "inches":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*36,2)
                print(f"{val} yards is {result} inches")

        elif convert.lower() == "inches" and to.lower() == "miles":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/63360,5)
                print(f"{val} inches is {result} miles")
        
        elif convert.lower() == "miles" and to.lower() == "inches":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*63360,2)
                print(f"{val} miles is {result} inches")

        elif convert.lower() == "feet" and to.lower() == "yards":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/3,2)
                print(f"{val} feet is {result} yards")
        
        elif convert.lower() == "yards" and to.lower() == "feet":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*3,2)
                print(f"{val} yards is {result} feet")

        elif convert.lower() == "feet" and to.lower() == "miles":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/5280,5)
                print(f"{val} yards is {result} centimeters")

        elif convert.lower() == "miles" and to.lower() == "feet":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*5280,5)
                print(f"{val} miles is {result} feet")

        elif convert.lower() == "yards" and to.lower() == "miles":
            val = float(input("value"))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val/1760,5)
                print(f"{val} yards is {result} miles")

        elif convert.lower() == "miles" and to.lower() == "yards":
            val = float(float(input("value")))
            if isinstance(val,bool) == True or isinstance(val, str) == True or isinstance(val,list) == True:
                print("Invalid value")
                sys.exit()
            else:
                result = round(val*1760,5)
                print(f"{val} miles is {result} yards")
    
    elif type.lower() == "ratio to percentage":
        
        '''
        values = int(input("how many values?"))
        if values > 1:
            numbers = []
            for i in range(values):
                number = int(input("enter your number"))
                numbers.append(number)
            total = 0
            for i in numbers:
                total = total + i
            percentage = 0
            percentages = []
            for i in numbers:
                percentage = round(i/total * 100, 3)
                percentages.append(percentage)
            print("percentages:", percentages)
        else:
            sys.exit()
            '''
        ratio = input("enter the ratio")
        values = ratio.split(':')
        values = list(map(float, values))
        total = 0
        for num in values:
            total = total + num
        percentage = 0
        percentages = []
        for percent in values:
            percentage = round(percent/total * 100, 3)
            percentages.append(percentage)
        print("percentages:", percentages)
    
    elif type.lower() == "lcm and gcf":
        num1 = int(input("first number"))
        num2 = int(input("second number"))
        print("The lcm is", find_lcm(num1,num2))
        print("The gcf is", find_gcf(num1,num2))
    
    elif type.lower() == "triangle":
        s1 = float(input("length of the first side of the triangle"))
        s2 = float(input("length of the second side of the triangle"))
        s3 = float(input("length of the third side of the triangle"))

        perimeter = s1+s2+s3
        s = perimeter/2
        t_area = (s * (s-s1) * (s-s2)*(s-s3))**0.5

        print(f"area: {t_area}\nperimeter: {perimeter}")
    
    elif type.lower() == "angle":
        angle = float(input("enter the angle"))
        if angle >= 180:
            print("try something lower")
            sys.exit()
        else:
            which = input("do you want to find the complement or suplement?")
            if which.lower() == "complement":
                complement = 90 - angle
                print(f"the complementary angle to {angle}° is {complement}°")
            if which.lower() == "supplement":
                supplement = 180 - angle
                print(f"the supplementary angle to {angle}° is {supplement}°")

    elif type.lower() == "circle":
        radius = float(input("enter the radius of the circle"))
        circumference = round(2*radius*3.14159265359, 5)
        c_area = 3.14159265359*(radius**2)
        print(f"The circumference of this circle is: {circumference}\nThe area of this circle is: {c_area}")

def find_lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

def find_gcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcf = i 
    return gcf

main()
                

