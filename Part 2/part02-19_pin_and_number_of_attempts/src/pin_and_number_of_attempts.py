correct_pin = 4321
attempts = 1

while True:
    pin = int(input("PIN: "))
    
    if pin == correct_pin:
        break
    else:
        print("Wrong")
        attempts += 1

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")