def cost_of_ground_shipping(weight):
  if weight <= 2:
    cost =+ (weight * 1.50) + 20
  elif weight > 2 and weight <= 6:
    cost =+ (weight * 3) + 20
  elif weight > 6 and weight <= 10:
    cost =+ (weight * 4) + 20
  elif weight > 10:
    cost =+ (weight * 4.75) + 20
  return cost

premium_ground_shipping = 125

print(cost_of_ground_shipping(8.4))

def cost_of_drone_shipping(weight):
  if weight <= 2:
    cost =+ (weight * 4.50)
  elif weight > 2 and weight <= 6:
    cost =+ (weight * 9)
  elif weight > 6 and weight <= 10:
    cost =+ (weight * 12)
  elif weight > 10:
    cost =+ (weight * 14.25)
  return cost

print(cost_of_drone_shipping(1.5))


def cheapest_shipping(weight):
  ground = cost_of_ground_shipping(weight)
  premium = premium_ground_shipping
  drone = cost_of_drone_shipping(weight)
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone
  print(
    "The cheapest option available is $%.f with %s shipping." % (cost, method)
  )
 
print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))

https://www.youtube.com/watch?time_continue=264&v=46_cL0O6xyQ&feature=emb_title