Choice = input (int("(Press 1 for Fahrenheit to Celsius) or (Press 2 for Celsius to Fahrenheit.)"))

if Choice == 1:
    Fahrenheit= input("What is the temprature in fahrenheit?")
    Fmath = float((Fahrenheit - 32) * 5/9)
    Celcius = (Fmath,1)
    print(str(Fahrenheit) + "in Celcius is " + Celcius)

