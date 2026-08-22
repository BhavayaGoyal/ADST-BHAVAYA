order_amount = float(input("Enter order amount: ₹"))
delivery_distance = float(input("Enter delivery distance (km):"))
customer_type = input("Enter customer type (New/Regular/Premium): ")
customer_rating = float(input("Enter customer rating (1-5): "))
restaurant_rating = float(input("Enter restaurant rating (1-5): "))
preparation_time = int(input("Enter preparation time (minutes): "))
payment_method = input("Enter payment method (Cash/UPI?Card): ")
weather = input("Enter weather condition (Normal/Rain/Severe): ")
demand_level = input("Enter demand level (Low/Medium/High/Extreme):")
peak_hour = input("Is it peak hour? (Yes/No): ")
previous_cancellations = int(input("Enter number of previous cancellations: "))

if delivery_distance <= 3:
    delivery_charge = 30
elif delivery_distance <=6:
    delivery_charge = 50
elif delivery_distance <= 10:
    delivery_charge = 80
else: 
    delivery_charge = 120

if weather == "Rain":
    delivery_charge+=20
elif weather == "Severe":
    delivery_charge+= 40

if peak_hour == "Yes":
    delivery_charge+= 20

if customer_type == "Premium":
    discount_percent = 20
elif customer_type == "Regular":
    discount_percent = 10
else:
    discount_percent = 5

if order_amount >= 1000:
    discount_percent+= 10

if discount_percent>30:
    discount_percent = 30

discount = order_amount * discount_percent / 100

if (delivery_distance > 15 or
    restaurant_rating < 2.5 or
    (weather == "Severe" and demand_level == "Extreme")):
    order_status = "REJECTED"

elif (delivery_distance > 10 or
      restaurant_rating <3.5 or
      previous_cancellations >= 3 or
      preparation_time > 45):
    order_status = "MANUAL REVIEW"

else: 
    order_status = "ACCEPTED"

risk_score = 0

if previous_cancellations >= 3:
    risk_score += 30
elif previous_cancellations >= 1:
    risk_score += 10

if delivery_distance > 10:
    risk_score += 20
elif delivery_distance > 6:
    risk_score +=10

if preparation_time > 45:
    risk_score += 20
elif preparation_time > 30:
    risk_score += 10

if weather == "Severe":
    risk_score += 25
elif weather == "Rain":
    risk_score += 10

if demand_level == "Extreme":
    risk_score += 15
elif demand_level == "High":
    risk_score += 10

if risk_score <= 30:
    cancellation_risk = "LOW"
elif risk_score <= 60:
    cancellation_risk = "MEDIUM"
else:
    cancellation_risk = "HIGH"

if restaurant_rating >= 4.5:
    restaurant_status = "EXCELLENT"
elif restaurant_rating >=4:
    restaurant_status = "GOOD"
elif restaurant_rating >= 3:
    restaurant_status = "AVERAGE"
else:
    restaurant_status = "POOR"

# Calculate final payable amount
if order_status == "REJECTED":
    final_amount = 0
else:
    final_amount = order_amount + delivery_charge - discount

if order_status == "REJECTED":
    order_category = "REJECTED ORDER"
elif order_status == "MANUAL REVIEW":
    order_category = "MANUAL REVIEW ORDER"
elif cancellation_risk == "HIGH":
    order_category = "HIGH RISK ORDER"
elif customer_type == "Premium" and risk_score <= 30:
    order_category = "PRIORITY ORDER"
else:
    order_category = "STANDARD ORDER"

print("\n========================================")
print("      FOOD DELIVERY ORDER REPORT")
print("=======================================")

print("Order Status       :", order_status)

if order_status == "REJECTED":
    print("Cancellation Risk  :", cancellation_risk)
    print("Restaurant Status  :", restaurant_status)
    print("Risk Score         :", risk_score)
    print("Manual Review      : NO")
    print("Order Category     :", order_category)
    print("Reason             : Order does not meet acceptance criteria")

else:
    print("Delivery Charge    : ₹", delivery_charge)
    print("Discount           : ₹", discount )
    print("Priority Delivery  :", "YES" if order_category == "PRIORITY ORDER" else "NO")
    print("Cancellation Risk  :", cancellation_risk)
    print("Restaurant Status  :", restaurant_status)
    print("Risk Score         :", risk_score)
    print("Manual Review      :", "YES" if order_status == "MANUAL REVIEW" else "NO")
    print("Order Category     :", order_category)

    print("----------------------------------------")
    print("Original Amount    :", order_amount)
    print("Final Payable      :₹", int(final_amount))
    print("----------------------------------------")