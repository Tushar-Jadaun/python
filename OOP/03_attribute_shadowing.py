class Chai:
    temperature = "hot"
    strength = "strong"
    
cutting =  Chai()
print(cutting.temperature)

cutting.temperature = "mid"
cutting.cup = "small"

print(cutting.temperature)
print(Chai.temperature)

del cutting.temperature
print(cutting.temperature)