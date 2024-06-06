# Payment Arrangements System

The aim of this project is to develop a system that automates and manages the functionality of a payment arrangements system used by financial services companies. The primary goal is to calculate all planned payments, including the last payment date and amount, for each customer based on the provided data.

## Company Overview

- **Company Name:** Credit Management Company
- **Location:** London, UK
- **Industry:** Financial Services
- **Values:** Empathy, Ethics, Dedication & Solutions

These values reflect the company's ability to find solutions that best suit our customers and clients. One instance is when our agents create payment arrangements for customers. An arrangement is an agreement between the company and a customer to pay for their arrears, either in whole or in manageable frequencies that the customer can adhere to.

## Case Study: Payment Arrangements

The company's values—empathy, ethics, dedication, and solutions—point to our ability to find solutions that best suit our customers and clients. One such instance is when our agents create payment arrangements for our customers. An arrangement is an agreement between Intrum and a customer to pay for their arrears, either in whole or in manageable frequencies to which the customer can adhere.

### Problem Statement

The dataset [CaseStudy Data.csv](data/CaseStudy%20Data.csv) provided contains core information for anonymized arrangements for some customers. The company's in-house system uses the same information in this file to calculate all dates and payments expected from each arrangement.

### Deliverables

1. **Replicate the System's Functionality**: Produce all planned payments (from the date of the first payment) for every single arrangement in the file provided.
2. **Last Payment Details**: Provide the last payment date and amount, as they are crucial for the company's system.
3. **Documentation**: Document the thought process and solution.

## Impact

This project aims to:

- **Improve Customer Satisfaction**: By accurately calculating payment schedules, customers can adhere to manageable payment plans, improving their financial stability.
- **Enhance Operational Efficiency**: Automating the calculation of payment schedules reduces manual errors and saves time for Intrum's agents.
- **Support Data-Driven Decisions**: The detailed payment schedules provide valuable insights into customer behavior and payment patterns, aiding in better decision-making.

## Functionality

The system performs the following tasks:

1. **Data Extraction**: Connects to an on-premise SQL server to extract the dataset.
2. **Date Calculation**: Calculates all payment dates based on the frequency and number of payments.
3. **Last Payment Details**: Determines the last payment date and amount for each arrangement.
4. **Output Generation**: Exports the calculated payment schedules and processed data to Excel files for presentation.

## Streamlit Application

The project includes a Streamlit application that provides an interactive interface for users to explore and interact with the payment arrangements data.
[see Application >>](https://payment-arrangements-system-replication-5eqnd6gemqryvumntnh4eb.streamlit.app/)

### Features

- **Upload Data**: Users can upload their dataset in CSV format.
- **View Calculations**: Users can view the calculated payment schedules and last payment details.
- **Download Results**: Users can download the results in Excel format.

### Running the Application Locally

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Baci-Ak/Payment-Arrangements-System-Replication.git
    cd Payment-Arrangements-System-Replication
    ```

2. **Set up a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

5. **Access the application**:
    Open your web browser and go to `http://localhost:8501`.

## Data Files

### `CaseStudy Data.csv`

This CSV file contains the core information for anonymized arrangements for some customers, including:
- `CustomerReference`: Unique identifier for the customer.
- `TotalToPay`: Total amount to be paid by the customer.
- `FirstPayment`: Amount of the first payment.
- `FirstPaymentDate`: Date of the first payment.
- `NumberOfPayments`: Total number of payments.
- `InstalmentAmount`: Amount of each installment.
- `Frequency`: Frequency of the payments (e.g., single, monthly).
- `FrequencyType`: Type of frequency (e.g., days, weeks, months).
- `FrequencyNumber`: Number associated with the frequency type.

![Screenshot 2024-05-24 at 5 54 08 PM](https://github.com/Baci-Ak/Payment-Arrangements-System-Replication/assets/134199508/f661ffea-6829-4144-8174-767bfdd62121)

### `Payment_Schedule.xlsx`

This Excel file is generated by the system and contains the detailed payment schedule for each customer, including:
- `CustomerReference`: Unique identifier for the customer.
- `PaymentDate`: Date of each planned payment.
- `PaymentAmount`: Amount of each planned payment.

### `Processed_Data.xlsx`

This Excel file is generated by the system and contains the processed data with additional details, including:
- `CustomerReference`: Unique identifier for the customer.
- `TotalToPay`: Total amount to be paid by the customer.
- `FirstPayment`: Amount of the first payment.
- `FirstPaymentDate`: Date of the first payment.
- `NumberOfPayments`: Total number of payments.
- `InstalmentAmount`: Amount of each installment.
- `Frequency`: Frequency of the payments (e.g., single, monthly).
- `FrequencyType`: Type of frequency (e.g., days, weeks, months).
- `FrequencyNumber`: Number associated with the frequency type.
- `PaymentDates`: List of all planned payment dates.
- `LastPaymentDate`: Date of the last payment.
- `LastPaymentAmount`: Amount of the last payment.

## Project Structure

The project repository includes the following key files and directories:

- **`data/`**: Contains the data files.
  - `CaseStudy Data.csv`: The source dataset containing anonymized arrangements.
  - `Payment_Schedule.xlsx`: The generated payment schedule.
  - `Processed_Data.xlsx`: The processed data with additional details.
- **`payment_arrangements.R`**: The R script that contains the code to process the data and generate the payment schedules.
- **`app.py`**: The Streamlit application script.
- **`requirements.txt`**: A list of required Python packages for running the Streamlit application.

## Code and Implementation

The code to process the data and generate the payment schedules is provided in the `payment_arrangements.R` file. This script includes the following key steps:

1. **Connecting to the SQL Server**: Establishes a connection to the on-premise SQL server and loads the data.
2. **Calculating Payment Dates**: Uses a custom function to generate all payment dates based on the provided frequency and number of payments.
3. **Processing the Data**: Adds additional columns for the last payment date and amount.
4. **Exporting the Data**: Exports the processed data and payment schedules to Excel files.

### Running the Code

1. **Ensure necessary packages are installed**:
    - `readr`
    - `dplyr`
    - `lubridate`
    - `tidyr`
    - `openxlsx`
    - `DBI`
    - `odbc`

2. **Run the R script**:
    - Open the `payment_arrangements.R` file in your R environment (e.g., RStudio).
    - Execute the script to process the data and generate the output files.

## Thought Process

### Introduction to the Problem

The problem involves calculating payment dates based on the provided frequency and number of payments. Important details include the start date, total amount, and installment amounts.

### Explanation of the Code

1. **Loading Libraries**: Essential libraries for reading data, manipulating data, handling dates, and exporting to Excel.
2. **Connecting to the SQL Server**: Establishing a connection to the on-premise SQL server and extracting the dataset.
3. **Function Definition**: Creating a function to generate the payment dates based on the frequency and type of payments.
4. **Data Processing**: Using `mutate` to add new columns for payment dates (`PaymentDates`), last payment date (`LastPaymentDate`), and last payment amount (`LastPaymentAmount`).
5. **Unnesting and Exporting Data**: Flattening the list of payment dates using `unnest` and exporting the results to Excel files.

### Caveats

- Ensuring that the dates are consistently of type `Date`.
- Handling edge cases such as single payments correctly.

### Output

The processed data and payment schedule are saved as Excel files in the [Data](data) folder.

## Screenshots

![Screenshot 2024-05-24 at 5 55 23 PM](https://github.com/Baci-Ak/Payment-Arrangements-System-Replication/assets/134199508/75d0846b-0886-4fd0-9e94-26bb2742133f)

![Screenshot 2024-05-24 at 5 59 28 PM](https://github.com/Baci-Ak/Payment-Arrangements-System-Replication/assets/134199508/9ea924f7-6a07-492e-8296-3b3985fde339)

## Conclusion

This project demonstrates the integration of data manipulation, date handling, and file exporting techniques to replicate the payment arrangements system. It highlights the ability to handle complex datasets and perform detailed calculations to produce meaningful outputs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

