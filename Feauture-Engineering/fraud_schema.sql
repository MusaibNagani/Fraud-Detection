CREATE DATABASE FraudDetection;
GO
USE FraudDetection;
GO 

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY NOT NULL,
    CustomerName VARCHAR(100),
    Region VARCHAR(50),
    AccountOpenDate DATE,
    AccountType VARCHAR(20)
);

CREATE TABLE TRANSACTIONS(
    TransactionID INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    CustomerID INT,
    Amount Decimal(10,2),
    TransactionDate DATETIME,
    Channel VARCHAR(20),
    Merchant VARCHAR(100),
    Location VARCHAR(100),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE Login (
    LoginID INT IDENTITY(1, 1) PRIMARY KEY NOT NULL,
    CustomerID INT,
    LoginTime DATETIME,
    IPAddress VARCHAR(100),
    DeviceID VARCHAR(100),
    Loaction VARCHAR(100),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

