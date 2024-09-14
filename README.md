**MarketBillingApp**

**Supermarket Invoice Generating Application in Python**

**Overview:**

MarketBillingApp is a Python-based application designed to streamline the process of generating, managing, and printing supermarket invoices. With a user-friendly interface, this application enables you to input customer details, add products, generate a detailed bill, save or retrieve the bill later using the bill number, and print the invoice directly from the app.

**Features:**

- **Intuitive Interface:** Easily input customer information and product details.
- **Bill Generation:** Automatically generates a detailed bill that is displayed in the interface.
- **Save Bills:** Saves each bill as a `.txt` file in the `bills` folder with the bill number as the filename.
- **Retrieve Bills:** Searches for a specific bill by bill number to view the details from the saved `.txt` files.
- **Print Invoice:** Prints the generated bill directly from the application.
- **Persistent Storage:** All bills are saved in the `bills` folder for future access.

**How to Use:**

1. **Run the Application:** Execute the Python script to open the application interface.
2. **Fill in Customer Details:** Input the customer's name and relevant details.
3. **Add Products:** One by one, add the products that the customer purchased along with the product details.
4. **Generate Bill:** Click on 'Generate Bill' to display the generated bill on the right-hand side of the interface.
5. **Save the Bill:** After reviewing, click 'Save Bill' to store the bill as a `.txt` file in the `bills` folder. The bill will be saved with the bill number as the file name.
6. **Print Invoice:** Use the 'Print Invoice' option to print the bill directly from the app.
7. **Search Bill:** To view a previously saved bill, enter the bill number and the application will fetch and display the details from the `bills` folder.

**Note:** Do not delete the `bills` folder, as it stores all generated bills.

**Requirements:**

1. **Python 3.x:** The application is developed using Python, so a Python 3.x installation is required.
2. **Tkinter:** This built-in Python library is used for the graphical user interface (GUI). It handles the creation of windows, buttons, labels, and text fields.
3. **Datetime:** The `datetime` module is used to capture and display the current date and time on each bill.
4. **OS Module:** The `os` module is used to handle file system operations such as saving and printing bills. Ensure the system allows writing and reading `.txt` files.
5. **File System:** A folder named `bills` should exist in the application's directory, as all saved bills will be stored here. Ensure the folder is not deleted, as it contains the saved bill data.
6. **Printer Access:** The application allows the printing of bills via the `os.startfile` command. The system running the application must have access to a connected printer or print service for this function to work.

**Additional Notes:**

1. Ensure the bills folder exists in the project directory before running the application, as it is necessary for saving and printing invoices.
2. The print functionality relies on the operating system's built-in print service, so it may behave differently depending on the OS (e.g., Windows or Linux).

**By:**
Adithya Sai Srinivas
