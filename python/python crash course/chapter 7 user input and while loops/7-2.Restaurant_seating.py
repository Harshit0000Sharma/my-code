dinner_people=input(print("\nhow many people are in your group for dinner")) 
dinner_people=int(dinner_people)
if dinner_people>8:
    print("\nyou will have to wait for a table")
elif dinner_people<=8:
    print("\nyour table is ready")