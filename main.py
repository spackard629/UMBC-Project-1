#Introduction 

print()
print("==========")
print("Welcome to Steve's Cars")
print("Automated Car Ordering System")
print("==========")
print()

#Input Make and Model 

print()
print("1. ~Please Select Make and Model~")
print("  a. Honda CRV")
print("  b. Ford Explorer")
print("  c. Chevy Silverado")
print("  d. Kia Rio")
print()
makeModel = input("please enter a - d: ")
print()

#Input Sun Roof Option 

print()
print("2. ~Would you like a Sun Roof?~")
sunRoof = input("please enter YES or NO: ")
print()

#Input Car Paint Color

print()
print("3. ~What color would you like?")
paintJob = input("please enter a color: ")
print()

#Input Heated Seat Option

print()
print("4. ~Would you like heated seats?")
heatedSeats = input("please enter YES or NO: ")
print()

#Input Seat Material 

print()
print("5. ~What material would you like the upholstery to be?~")
print("  a. Leather")
print("  b. Plastic")
print("  c. Fabric")
seatMaterial = input("please enter a - c: ")
print()

#Input Insurance Option

print()
print("6. ~Would you like to purchase our added insruance policy?~")
insurancePolicy = input("please enter YES or NO: ")
print()

#Display Results

print()
print("~Summary~")
print(f"Model: {makeModel}")
print(f"Sun Roof: {sunRoof}")
print(f"Paint Color: {paintJob}")
print(f"Heated Seats: {heatedSeats}")
print(f"Upholstery: {seatMaterial}")
print(f"Insurance Plan: {insurancePolicy}")
print()
