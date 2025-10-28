class OutOfIngredientsError(Exception):
    pass

def make_chai(milk,sugar):
    if milk==0 or sugar ==0:
        raise OutOfIngredientsError("Missing Milk or Sugar")
    print("chai is ready")

# make_chai(0,0)
make_chai(0,1)    