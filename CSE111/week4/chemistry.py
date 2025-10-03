from formula import parse_formula   # provided function
from collections import defaultdict

# Periodic Table (symbol → [name, atomic_mass, atomic_number])
def make_periodic_table():
    table = {
        "H": ["Hydrogen", 1.00794, 1],
        "He": ["Helium", 4.002602, 2],
        "Li": ["Lithium", 6.941, 3],
        "Be": ["Beryllium", 9.012182, 4],
        "B": ["Boron", 10.811, 5],
        "C": ["Carbon", 12.0107, 6],
        "N": ["Nitrogen", 14.0067, 7],
        "O": ["Oxygen", 15.9994, 8],
        "F": ["Fluorine", 18.9984032, 9],
        "Na": ["Sodium", 22.98976928, 11],
        "Mg": ["Magnesium", 24.305, 12],
        "Al": ["Aluminum", 26.9815386, 13],
        "Si": ["Silicon", 28.0855, 14],
        "P": ["Phosphorus", 30.973762, 15],
        "S": ["Sulfur", 32.065, 16],
        "Cl": ["Chlorine", 35.453, 17],
        "K": ["Potassium", 39.0983, 19],
        "Ca": ["Calcium", 40.078, 20],
        "Fe": ["Iron", 55.845, 26],
        "Cu": ["Copper", 63.546, 29],
        "Zn": ["Zinc", 65.38, 30],
        "Ag": ["Silver", 107.8682, 47],
        "I": ["Iodine", 126.90447, 53],
        "Au": ["Gold", 196.966569, 79],
        "Hg": ["Mercury", 200.59, 80],
        "Pb": ["Lead", 207.2, 82]
        # Add more as needed
    }
    return table


def compute_molar_mass(symbol_quantity_list, periodic_table):
    """Compute total molar mass for a molecule."""
    total_mass = 0.0
    for symbol, qty in symbol_quantity_list:
        if symbol not in periodic_table:
            raise ValueError(f"Unknown element: {symbol}")
        atomic_mass = periodic_table[symbol][1]
        total_mass += atomic_mass * qty
    return total_mass


def compute_protons(symbol_quantity_list, periodic_table):
    """Compute total number of protons in the molecule."""
    total_protons = 0
    for symbol, qty in symbol_quantity_list:
        atomic_number = periodic_table[symbol][2]
        total_protons += atomic_number * qty
    return total_protons


def main():
    # Known formulas dictionary (for extra credit)
    known_formulas = {
        "H2O": "Water",
        "CO2": "Carbon Dioxide",
        "O2": "Oxygen Gas",
        "NaCl": "Table Salt",
        "C6H12O6": "Glucose"
    }

    # Get user input
    formula = input("Enter the chemical formula of the sample: ")
    mass = float(input("Enter the mass of the sample in grams: "))

    # Build periodic table
    periodic_table = make_periodic_table()

    # Parse formula into element counts
    symbol_quantity_list = parse_formula(formula, periodic_table)

    # Compute molar mass
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

    # Compute number of moles
    moles = mass / molar_mass

    # Print results
    print(f"\nResults for {formula}:")
    print(f"Molar mass: {molar_mass:.5f} g/mol")
    print(f"Number of moles in {mass} g: {moles:.5f} mol")

    # Extra: check if formula is in known list
    if formula in known_formulas:
        print(f"This compound is commonly known as: {known_formulas[formula]}")

    # Extra: compute number of protons
    total_protons = compute_protons(symbol_quantity_list, periodic_table)
    print(f"Total number of protons in one molecule: {total_protons}")


# Run only if executed directly
if __name__ == "__main__":
    main()