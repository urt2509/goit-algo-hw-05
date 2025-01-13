from fibonacci import fib
from generator import sum_profit, generator_numbers
from bot import bot_main


# Run Task_4
def bot_command():

    contacts_list = bot_main()
    return contacts_list


if __name__ == "__main__":

    # Run Task_1
    print(fib(10))  # Run Task1
    print(fib(15))  # Run Task1

    # Run Task_2
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."  # Run Task2
    total_income = sum_profit(text, generator_numbers)  # Run Task2
    print(f"Загальний дохід: {total_income}")  # Run Task2

    # Run Task4
    bot_command()
