# AREA OF SQUARE
def area_of_square():
  print("THIS IS THE PROGRAMM FOR CALCUALTE \"AREA OF SQUARE\"")
  print("1.cm(Centimeter)")
  print("2.m(Meter)")
  choose_unit=str(input("Choose Your Unit From Above(In number):"))
  side_for_square=eval(input("Enter Side :"))
  area_of_square=side_for_square*side_for_square
  if choose_unit=="1":
    print("Area of square = ",area_of_square,"sq.cm")
  elif choose_unit=="2":
    print("Area of Square = ",area_of_square,"sq.m")
  else:
    print("Invalid !\n")
    print("\n")
area_of_square()


# HERE AREA OF RECTANGLE
def area_of_rectangle():
  print("THIS IS THE PROGRAMM FOR CALCUALTE \"AREA OF RECTANGLE\"")
  print("1.cm(Centimeter)")
  print("2.m(Meter)")
  choose_units=str(input("choose Your Units from above(in number): "))
  if choose_units=="1":
    length=eval(input("Length : "))
    Breadth=eval(input("Breadth : "))
    rectangle_area=length*Breadth
    print("Area of Rectanle : ",rectangle_area,"sq.cm")
  elif choose_units=="2":
    length=eval(input("Length : "))
    Breadth=eval(input("Breadth : "))
    rectangle_area=length*Breadth
    print("Area of Rectanle : ",rectangle_area,"sq.m")
  else:
    print(" Invalid !\n")
area_of_rectangle()

# here the AREA OF CIRCLE
def area_of_circle():
  print("THIS IS THE PROGRAMM FOR CALCUALTE \"AREA OF CIRCLE\"")
  print("1.cm(Centimeter)")
  print("2.m(Meter)")
  choose_units=str(input("choose Your Units from above(in number): "))
  """area= π*r^2"""
  if choose_units=="1":
    radius=eval(input("Enter Radius :"))
    circle_area=22/7*radius*radius
    print("Area of Circle = ",circle_area,"sq.cm")
  elif choose_units=="2":
    radius=eval(input("Enter Radius :"))
    circle_area=22/7*radius*radius
    print("Area of Circle = ",circle_area,"sq.m")
  else:
    print("Invalid !")
area_of_circle()

# HERE THE AREA OF TRIANGLE
def area_of_triangle():
  print("THIS IS THE PROGRAMM FOR CALCUALTE \"AREA OF TRIANGLE\"")
  print("1.cm(Centimeter)")
  print("2.m(Meter)")
  choose_unit_for_triangle=str(input("choose Your Units from above(in number): "))
  if choose_unit_for_triangle=="1":
    base=eval(input("Your Base :"))
    height=eval(input("Height(Perpendicular distance): "))
    area_for_triangle= 1/2*base*height
    print("Area of Triangle = ",area_for_triangle,"sq.cm")
  elif choose_unit_for_triangle=="2" :
    base=eval(input("Your Base :"))
    height=eval(input("Height(Perpendicular distance): "))
    area_for_triangle= 1/2*base*height
    print("Area of Triangle = ",area_for_triangle,"sq.cm")
  else:
    print("Invalid !")
area_of_triangle() 

