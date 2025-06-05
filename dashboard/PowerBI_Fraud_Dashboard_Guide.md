# Power BI Dashboard Guide – Fraud Detection

This guide walks you through building a fully functional Power BI dashboard using `final_features.csv` which contains engineered features related to transaction velocity, behavioral changes, and dormancy.

---

##  Dataset Used

**File:** `final_features.csv` (from outputs/ folder)

**Fields Available:**
- `CustomerID`
- `TransactionDate`
- `TransactionCountUnder30Minutes`
- `TransactionratePerHour`
- `TransactionBurstScore`
- `DaysSinceLastTransaction`
- `GapBeforeHighTransaction`
- `IsDormantThenUsed`
- `DormancyPeriodLength`
- `RecentIPChange`
- `RecentDeviceChange`
- `Amount`

---

## 🧠 Step-by-Step Dashboard Creation

### 1. **Import Data**
- In Power BI Desktop → Home → **Get Data → CSV**
- Load `final_features.csv`

---

### 2. **Create Relationships**
No need for relationships; everything is pre-joined.

---

## Visuals

### 🔹 A. Transactions by top 10 Customers
**Visual Type:** Bar Chart  
**Axis:** `CustomerID`  
**Value:** Count of `TransactionDate`
**Filter:** `CustomerID` by N top 10 
**Purpose:** See which customers are most active

---

### 🔹 B. Risk Score per Customer (DAX Measure)
**Create a new column:**
```DAX
RiskScore = 
'final_features'[GapBeforeHighTransaction] +
'final_features'[IsDormantThenUsed] +
'final_features'[RecentIPChange] +
'final_features'[RecentDeviceChange] +
IF('final_features'[TransactionBurstScore] >= 2, 1, 0)
```
**Visual Type:** Clustered Bar Chart  
**Axis:** `CustomerID`  
**Value:** `RiskScore`  
**Purpose:** Highlights customers with more risk signals

---

### 🔹 C. Line Chart: Transaction Rate Over Time
**Visual Type:** Line Chart  
**Axis:** `TransactionDate`  
**Value:** Average of `TransactionratePerHour`  
**Legend (optional):** `CustomerID` or region  
**Purpose:** Spot transaction surges over time

---

### 🔹 D. Scatter Plot: Burst Score vs Dormancy
**Visual Type:** Scatter Chart  
**X Axis:** `TransactionBurstScore`  
**Y Axis:** `DormancyPeriodLength`  
**Details or Tooltip:** `CustomerID`, `Amount`  
**Purpose:** Identify behavior like reactivation after long gaps

---

### 🔹 E. Risk Flag Breakdown (DAX Flag)
**Create another column:**
```DAX
RiskFlag = 
IF(
    'final_features'[GapBeforeHighTransaction] = 1 || 
    'final_features'[RecentIPChange] = 1 || 
    'final_features'[TransactionBurstScore] >= 3,
    1, 0
)
```
**Visual Type:** Pie Chart or KPI  
**Value:** Count of `RiskFlag`  
**Purpose:** See total risky transactions

---

### 🔹 F. Slicer Controls
- Add slicers for:  
  - `TransactionDate` (date range)  
  - `CustomerID` (to drill down on one customer)  
  - `IsDormantThenUsed` (yes/no)

---

## 📁 Layout 

Split the dashboard into **3 sections**:

### 🔸 Top Row – Filters
- Date Slicer
- Customer Slicer

### 🔸 Middle Row – Summary KPIs
- Total Transactions
- Total Risky Transactions
- Avg Risk Score

### 🔸 Bottom Row – Detailed Charts
- Bar chart: Transactions per Customer
- Line chart: TransactionRate over time
- Scatter: BurstScore vs Dormancy
- Pie chart: RiskFlag distribution

---
