 calculation_of_electric_vehicles.py

print("ELECTRIC VEHICLE CALCULATOR")
print("---------------------------")

battery_voltage = float(input("Enter battery voltage (V): "))
battery_capacity = float(input("Enter battery capacity (Ah): "))
efficiency = float(input("Enter vehicle efficiency (%): "))
energy_consumption = float(input("Enter energy consumption (Wh/km): "))
charger_power = float(input("Enter charger power (kW): "))

 Battery energy in Wh
battery_energy = battery_voltage * battery_capacity

 Usable battery energy
usable_energy = battery_energy * (efficiency / 100)

Estimated driving range
range_km = usable_energy / energy_consumption

 Charging time in hours
charging_time = (battery_energy / 1000) / charger_power

print("\n--- EV Results ---")
print("Battery Energy =", round(battery_energy, 2), "Wh")
print("Usable Energy =", round(usable_energy, 2), "Wh")
print("Estimated Range =", round(range_km, 2), "km")
print("Charging Time =", round(charging_time, 2), "hours")
