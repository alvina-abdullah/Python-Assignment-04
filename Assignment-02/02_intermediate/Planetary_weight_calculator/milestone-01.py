
# enter their Earth weight
earth_weight = float(input("Enter a weight on Earth: "))

# Calculate Mars weight using the given factor (37.8%)
mars_weight = earth_weight * 0.378

# Round the result to 2 decimal places
rounded_mars_weight = round(mars_weight, 2)

# Print the result
print(f"The equivalent on Mars:", rounded_mars_weight)


if __name__ == "__main__":
    main()