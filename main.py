from fibonacci import fib
from generator import sum_profit, generator_numbers

if __name__ == "__main__":
    print(fib(10))  # Run Task1
    print(fib(15))  # Run Task1

    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."  # Run Task2
    total_income = sum_profit(text, generator_numbers)  # Run Task2
    print(f"Загальний дохід: {total_income}")  # Run Task2
