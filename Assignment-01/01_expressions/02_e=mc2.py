

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))


    C: int = 299792458  # The speed of light in m/s
    # Calculate energy
    # equivalently energy = mass * (C ** 2)
    # using the ** operator to raise C to the power of 2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display work to the user easily
    print("Calculation")
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    
    print(str(energy_in_joules) + " joules of energy!")

if __name__ == '__main__':
    main()