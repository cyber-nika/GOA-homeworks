try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        if denominator == 0:
            raise ValueError("You cannot divide by zero.")

        result = numerator / denominator
        print(f"Result: {result}")

except ValueError as Error:
        print(f" Error: {Error}")
except Exception:
        print(" Error: Please enter valid numeric inputs.")
finally:
        print(" Operation complete.")
