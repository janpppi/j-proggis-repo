class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"{self.name}, {self.category}, {self.amount} euros"
    

def main():
    #ask expense info from the user

    name = input("Enter expense name: ")
    amount = input("Enter expense amount (€): ")
    category = input("Select expense category: "+ 
                     "\n1. Food" +
                     "\n2. Home" +
                     "\n3. Work" +
                     "\n4. Fun" +
                     "\n5. Misc: ")
    
    expense = Expense(name, category, amount)

    #create an empty file, if it doesn't exist
    try:
        #attempt to open file
        f = open("myexpenses.csv", "a")
    except FileNotFoundError:
        print("The file doesn't exist")

    #save individual expenses into a .csv-file
    f.write("\n"+expense.__str__())
    f.close()

    f = open("myexpenses.csv", "r")
    print(f.read())

main()

