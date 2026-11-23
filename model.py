# GitHub collaboration demo


def pump_capacity(capacity_m3s, operation_factor):
    # Available capacity = rated capacity * operating factor.
    return capacity_m3s * operation_factor


# The following function is maintained independently.
# Keeping changes separate makes them easier to review.


def vulnerable_population(elderly_count, children_count):
    # Elderly and children are separate age groups in this demo.
    return elderly_count + children_count


if __name__ == "__main__":
    print("Pump capacity (m3/s):", pump_capacity(10, 0.8))
    print("Vulnerable population:", vulnerable_population(100, 50))
