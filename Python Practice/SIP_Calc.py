def calculate_sip(monthly_investment, interest_rate, investment_period):
    monthly_rate = interest_rate / 1200 
    sip_data = []
    total_invested = 0.0

    for month in range(1, investment_period + 1):
        principal = monthly_investment
        interest_earned = 0.0
        if month > 1:
            interest_earned = sip_data[month - 2][3] * monthly_rate  

        total_investment_so_far = principal + (sip_data[month - 2][3] if month > 1 else 0)
        future_value = total_investment_so_far + interest_earned

        sip_data.append((month, principal, interest_earned, future_value))
        total_invested += principal

    return sip_data, total_invested


def display_sip_data(sip_data, total_invested):
    """Displays SIP data."""
    headers = ("Month", "Investment", "Interest", "Total Value")
    separator_length = 15 * len(headers)
    print("-" * separator_length)
    print("{:^5} {:^15} {:^15} {:^15}".format(*headers))
    print("-" * separator_length)

    for month, investment, interest, total_value in sip_data:
        print("{:^5} {:^15.2f} {:^15.2f} {:^15.2f}".format(
            month, round(investment, 2), round(interest, 2), round(total_value, 2)
        ))
    print("-" * separator_length)

    total_returns = round(sip_data[-1][3] - total_invested, 2) if sip_data else 0
    print(f"Total Invested Amount: Rs. {round(total_invested, 2):.2f}")
    print(f"Total Returns: Rs. {total_returns:.2f}")
    print(f"Final Value: Rs. {round(sip_data[-1][3], 2):.2f}")


def get_user_input():
    while True:
        try:
            monthly_investment = float(input("Enter the monthly investment amount (Rs.): "))
            if monthly_investment <= 0:
                raise ValueError("Investment must be positive")
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive number.")

    while True:
        try:
            interest_rate = float(input("Enter the annual interest rate (%): "))
            if interest_rate <= 0:
                raise ValueError("Interest rate must be positive")
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive number.")

    while True:
        try:
            investment_period = int(input("Enter the investment period (in months): "))
            if investment_period <= 0:
                raise ValueError("Investment period must be positive")
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
    return monthly_investment, interest_rate, investment_period


if __name__ == "__main__":
    monthly_investment, interest_rate, investment_period = get_user_input()
    sip_data, total_invested = calculate_sip(monthly_investment, interest_rate, investment_period)
    display_sip_data(sip_data, total_invested)