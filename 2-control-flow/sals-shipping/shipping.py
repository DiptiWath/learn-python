weight = 20

#"Ground Shipping"
if weight <= 2 :
  cost_ground = weight * 1.50 + 20
elif weight > 2 and weight <= 6 :
  cost_ground = weight * 3.00 + 20
elif weight > 6 and weight <= 10 :
  cost_ground = weight * 4.00 + 20
elif weight > 10 :
  cost_ground = weight * 4.75 + 20
print("Ground Shipping : $",cost_ground )

#"Ground Shipping Premium"
cost_ground_premium = 125.00
print("Ground Shipping Premium : $",cost_ground_premium )

#"Drone Shipping"
if weight <= 2 :
  cost_drone = weight * 4.50
elif weight > 2 and weight <= 6 :
  cost_drone = weight * 9.00
elif weight > 6 and weight <= 10 :
  cost_drone = weight * 12.00
elif weight > 10 :
  cost_drone = weight * 14.25
print("Drone Shipping : $",cost_drone )
