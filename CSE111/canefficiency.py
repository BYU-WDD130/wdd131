import math

# -----------------------------
# Functions
# -----------------------------

# Compute the volume of a cylinder
def compute_volume(radius, height):
    """
    Calculate the volume of a cylinder.
    V = π * r^2 * h
    """
    return math.pi * radius**2 * height

# Compute the surface area of a cylinder
def compute_surface_area(radius, height):
    """
    Calculate the surface area of a cylinder.
    A = 2 * π * r * (r + h)
    """
    return 2 * math.pi * radius * (radius + height)

# Compute storage efficiency (volume / surface area)
def compute_storage_efficiency(radius, height):
    """
    Calculate storage efficiency of a cylinder.
    efficiency = volume / surface_area
    """
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    return volume / surface_area

# Compute cost efficiency (volume / cost)
def compute_cost_efficiency(radius, height, cost):
    """
    Calculate cost efficiency of a cylinder.
    cost_efficiency = volume / cost
    """
    volume = compute_volume(radius, height)
    return volume / cost

# -----------------------------
# List of steel cans: (Name, radius, height, cost)
# -----------------------------
cans = [
    ("#1 Picnic", 6.83, 10.16, 0.28),
    ("#1 Tall", 7.78, 11.91, 0.43),
    ("#2", 8.73, 11.59, 0.45),
    ("#2.5", 10.32, 11.91, 0.61),
    ("#3 Cylinder", 10.79, 17.78, 0.86),
    ("#5", 13.02, 14.29, 0.83),
    ("#6Z", 5.40, 8.89, 0.22),
    ("#8Z short", 6.83, 7.62, 0.26),
    ("#10", 15.72, 17.78, 1.53),
    ("#211", 6.83, 12.38, 0.34),
    ("#300", 7.62, 11.27, 0.38),
    ("#303", 8.10, 11.11, 0.42)
]

# -----------------------------
# Main program
# -----------------------------

print(f"{'Can':<12} {'Volume':>10} {'Surface':>12} {'Storage Eff.':>14} {'Cost Eff.':>12}")
print("-"*70)

best_storage_can = ""
best_storage_value = 0

best_cost_can = ""
best_cost_value = 0

# Loop through each can
for name, r, h, cost in cans:
    volume = compute_volume(r, h)
    surface_area = compute_surface_area(r, h)
    storage_eff = compute_storage_efficiency(r, h)
    cost_eff = compute_cost_efficiency(r, h, cost)
    
    print(f"{name:<12} {volume:10.2f} {surface_area:12.2f} {storage_eff:14.2f} {cost_eff:12.2f}")
    
    # Track best storage efficiency
    if storage_eff > best_storage_value:
        best_storage_value = storage_eff
        best_storage_can = name
    
    # Track best cost efficiency
    if cost_eff > best_cost_value:
        best_cost_value = cost_eff
        best_cost_can = name

print("\nCan with the highest storage efficiency:", best_storage_can)
print("Can with the highest cost efficiency:", best_cost_can)