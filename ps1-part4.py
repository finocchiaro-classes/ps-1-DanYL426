priors = int(input("Prior arrests: "))
priors_local_ord = input("Prior arrests for local ordinance (Y/N): ")
release_age = int(input("Age at release: "))

point_total = 0
if priors >= 2:
    point_total += 1
if priors >= 5:
    point_total += 1
if priors_local_ord == "Y":
    point_total += 1
if release_age >= 18 and release_age <= 24:
    point_total += 1
if release_age >= 40:
    point_total -= 1
    
print(f"The recidivism risk score is {point_total}")
