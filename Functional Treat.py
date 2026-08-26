def main():
    print("\nWelcome to the Data Analyzer and Transformer Program")

    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice=input("Please enter your choice: ")
        if choice=="1":
            input_data()
        elif choice=="2":
            display_summary()
        elif choice=="3":
            num = int(input("\nEnter a number to calculate its factorial: "))
            print(f"Factorial of {num} is: {factorial(num)}")
        elif choice=="4":
            filter_data()
        elif choice=="5":
            sort_data()
        elif choice=="6":
            display_stats()
        elif choice=="7":
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


def input_data():
    global data
    raw=input("\nEnter data for a 1D array (separated by spaces): ")
    data=[int(x) for x in raw.split()]
    print("Data has been stored successfully!")

def show_args(*args):
    print("Values received:",args)

def print_summary(**kwargs):
    for key, value in kwargs.items():
        print(f"-{key}:{value}")

def display_summary():
    global summary_count
    summary_count=len(data)
    print("\nData Summary:")
    print_summary(
        Total_elements=len(data),
        Minimum_value=min(data),
        Maximum_value=max(data),
        Sum_of_all_values=sum(data),
        Average_value=round(sum(data) / len(data), 2))

def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n - 1)

def filter_data():
    threshold=int(input("\nEnter a threshold value to filter out data above this value: "))
    filtered=list(filter(lambda x:x>=threshold,data))
    print(f"Filtered Data (values>={threshold}):")
    print(", ".join(map(str, filtered)))

def sort_data():
    print("\nChoose sorting option:")
    print("1. Ascending Order")
    print("2. Descending Order")

    sort_choice=input("Enter your choice: ")
    if sort_choice=="1":
        sorted_data=sorted(data)
        print("Sorted Data (Ascending):")
        print(sorted_data)
    elif sort_choice=="2":
        sorted_data=sorted(data, reverse=True)
        print("Sorted Data (Descending):")
        print(sorted_data)
    else:
        print("Invalid sorting choice.")

def calculate_stats(numbers):
    minimum=min(numbers)
    maximum=max(numbers)
    total=sum(numbers)
    avg=total/len(numbers)
    return minimum, maximum, total, avg

def display_stats():
    mini, maxi, total, avg = calculate_stats(data)
    print("\nDataset Statistics:")
    print(f"- Minimum value: {mini}")
    print(f"- Maximum value: {maxi}")
    print(f"- Sum of all values: {total}")
    print(f"- Average value: {avg:.2f}")
if __name__ == "__main__":
    main()