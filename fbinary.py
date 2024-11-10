import pickle

# File path for storing the binary data
BILL_FILE = "bills_reviews.dat"

# Function to load all bills and reviews from the binary file
def load_bills_reviews():
    try:
        with open(BILL_FILE, "rb") as file:
            return pickle.load(file)  # Load the entire dictionary
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist
    except Exception as e:
        print(f"Error loading data: {e}")
        return {}

# Function to save the dictionary of bills and reviews to the binary file
def save_bills_reviews(bills_reviews):
    try:
        with open(BILL_FILE, "wb") as file:
            pickle.dump(bills_reviews, file)  # Save the entire dictionary
    except Exception as e:
        print(f"Error saving data: {e}")

# Function to add a bill and review
def add_bill_review(billno = 0):
    # Load existing bills and reviews from file
    bills_reviews = load_bills_reviews()
    if billno = 0:
      bill_number = int(input("Enter the bill number: "))
    else:
      bill_number = billno
    review = input("Enter the review: ")

    # Add the bill and review to the dictionary
    bills_reviews[bill_number] = review

    # Save the updated dictionary back to the binary file
    save_bills_reviews(bills_reviews)
    print("Bill and review added successfully.")

# Function to display all bills and reviews
def display_bills_reviews():
    # Load the bills and reviews
    bills_reviews = load_bills_reviews()

    if bills_reviews:
        print("\nAll Bills and Reviews:")
        for bill_number, review in bills_reviews.items():
            print(f"Bill Number: {bill_number}, Review: {review}")
    else:
        print("No bills and reviews found.")

