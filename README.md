# wanderly-Elite-Project-using-only-python
# ✈️ Wanderly – Luxury Travel & Tour Management System

<p align="center">

### 🌍 Explore • Discover • Book • Travel

**A modern Python-based desktop application for managing tour packages, customer bookings, travel details, and digital tickets.**

</p>

---

## 📌 Project Overview

**Wanderly – Luxury Travel & Tour Management System** is a Python-based desktop application designed to provide a simple, attractive, and efficient platform for managing travel and tour bookings.

The application allows users to explore different travel packages, search and filter destinations, select a package, enter customer details, calculate the total booking price automatically, generate digital tickets, and manage existing bookings.

The system uses **Python Tkinter** for the graphical user interface and **SQLite** for storing booking information.

The project was developed as a practical Python project demonstrating GUI development, database connectivity, CRUD operations, event handling, form validation, and application design.

---

## ✨ Key Features

### 🏠 Dashboard

- Attractive application dashboard
- Quick access to major features
- Tour package overview
- Travel management interface

### 🌎 Tour Packages

Wanderly provides multiple predefined travel packages, including:

- 🏔️ Manali Adventure
- 🏖️ Goa Beach Escape
- 🏰 Rajasthan Royal Tour
- 🌴 Kerala Paradise
- 🏔️ Ladakh Expedition
- ❄️ Kashmir Dream
- 🏝️ Andaman Escape
- 👑 Udaipur Royal Escape

---

## 🗂️ Travel Categories

Tour packages are organized into different categories:

| Category | Description |
|---|---|
| 🏔️ Adventure | Exciting and adventurous destinations |
| 🏖️ Beach | Relaxing coastal destinations |
| 🌿 Nature | Natural and scenic destinations |
| 🏰 Heritage | Historical and cultural destinations |

---

## 🔎 Search & Filtering

Users can easily find suitable packages using:

- Package search
- Category filtering
- Sorting options
- Destination-based browsing
- Package information

This makes it easier to locate a suitable tour without manually searching through every package.

---

## 📝 Booking System

Users can create a new booking by entering details such as:

- Customer Name
- Phone Number
- Email Address
- Selected Package
- Travel Category
- Travel Date
- Number of Travelers

The application automatically calculates the total price based on the selected package and number of travelers.

---

## 🎫 Digital Ticket

After completing a booking, Wanderly provides a digital ticket containing important booking information.

The ticket can include:

- Booking ID
- Customer Name
- Package Name
- Travel Date
- Number of Travelers
- Total Price
- Booking Status

This provides users with an easy way to view their booking information.

---

## 📋 Booking Management

The application provides a booking management system where users can:

- View bookings
- Search bookings
- Check booking information
- Manage existing reservations
- Cancel bookings

---

## ❌ Booking Cancellation

Users can cancel an existing booking through the booking management interface.

The booking status can be updated accordingly instead of requiring the user to manually remove booking information.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| 🖥️ Tkinter | Graphical User Interface |
| 🗄️ SQLite | Database management |
| 🔗 sqlite3 | Python database connectivity |
| 📅 Date/Time | Travel and booking date management |
| 💻 Visual Studio Code | Development environment |

---

# 🏗️ System Architecture

```text
                   ┌─────────────────────────┐
                   │       Wanderly GUI       │
                   │        Tkinter           │
                   └────────────┬────────────┘
                                │
                                ▼
                   ┌─────────────────────────┐
                   │    Application Logic    │
                   │        Python           │
                   └────────────┬────────────┘
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
             ▼                  ▼                  ▼
      ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
      │   Packages  │   │  Bookings   │   │   Tickets   │
      └─────────────┘   └──────┬──────┘   └─────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ SQLite Database │
                       │  wanderly.db   │
                       └─────────────────┘
```

---

# 🗄️ Database

Wanderly uses **SQLite** as its database.

The database file is:

```text
wanderly.db
```

The main booking table is:

```text
bookings
```

The booking database contains information such as:

```text
booking_id
customer_name
phone
email
package
category
travel_date
travelers
total_price
booking_date
status
```

SQLite was selected because it is lightweight, easy to integrate with Python, and does not require a separate database server.

---

# 📂 Project Structure

A typical project structure is:

```text
Wanderly/
│
├── wanderly.py
│
├── wanderly.db
│
├── README.md
│
└── screenshots/
    ├── dashboard.png
    ├── packages.png
    ├── booking.png
    ├── ticket.png
    └── bookings.png
```

> **Note:** The exact Python filename can be changed according to the filename used in your project.

---

# 🚀 Installation & Setup

## 1️⃣ Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/YOUR-USERNAME/wanderly.git
```

Then enter the project directory:

```bash
cd wanderly
```

---

## 2️⃣ Check Python Installation

Make sure Python is installed on your computer.

Check the installed version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## 3️⃣ Run the Project

Run the Python program:

```bash
python wanderly.py
```

The Wanderly application should open in a new desktop window.

---

# 💻 Running in Visual Studio Code

You can also run the project using **Visual Studio Code**.

### Step 1

Open Visual Studio Code.

### Step 2

Open the Wanderly project folder.

### Step 3

Open the main Python file.

### Step 4

Run:

```text
Run Python File
```

or use the terminal:

```bash
python wanderly.py
```

---

# 📦 Required Libraries

The project primarily uses Python's built-in libraries.

The major modules include:

```python
import tkinter
import sqlite3
```

Additional standard Python modules may be used depending on the implementation.

Because SQLite and Tkinter are generally included with standard Python installations, no separate database server is required.

---

# 🎯 Project Objectives

The main objectives of Wanderly are:

1. To develop a user-friendly travel management application.
2. To provide an attractive graphical interface.
3. To display different tour packages.
4. To organize packages into categories.
5. To provide search and filtering functionality.
6. To simplify the travel booking process.
7. To automatically calculate booking prices.
8. To store customer booking information securely in a database.
9. To provide digital booking tickets.
10. To manage and cancel existing bookings.
11. To demonstrate Python GUI programming.
12. To demonstrate SQLite database connectivity.

---

# 🔄 Application Workflow

The basic workflow of the application is:

```text
Start Application
       │
       ▼
   Dashboard
       │
       ▼
 Browse Packages
       │
       ▼
Search / Filter Package
       │
       ▼
 Select Package
       │
       ▼
 Enter Customer Details
       │
       ▼
 Select Travel Date
       │
       ▼
 Enter Number of Travelers
       │
       ▼
 Calculate Total Price
       │
       ▼
 Confirm Booking
       │
       ▼
 Generate Digital Ticket
       │
       ▼
 Store Booking in SQLite
       │
       ▼
 Manage / Cancel Booking
```

---

# 🧩 Main Modules

## 1. Dashboard Module

The dashboard acts as the main entry point of the application.

It provides navigation to:

- Tour Packages
- Booking
- Booking Management
- About

---

## 2. Tour Package Module

This module displays available travel packages.

Each package contains information such as:

- Destination
- Category
- Price
- Package details

---

## 3. Search & Filter Module

This module allows users to search and organize packages according to their requirements.

Users can search for destinations and filter packages based on categories.

---

## 4. Booking Module

The booking module collects customer information and travel details.

Example:

```text
Customer Name
Phone
Email
Package
Category
Travel Date
Travelers
```

---

## 5. Price Calculation Module

The system calculates the total cost according to the selected package and number of travelers.

Conceptually:

```text
Total Price = Package Price × Number of Travelers
```

---

## 6. Database Module

The database module connects the Python application with SQLite.

It handles operations such as:

- INSERT
- SELECT
- UPDATE
- DELETE

This allows the application to maintain booking records.

---

## 7. Digital Ticket Module

After successful booking, the application generates a digital representation of the booking details.

This allows the customer to easily view their travel information.

---

## 8. Booking Management Module

This module allows the user to view and manage existing bookings.

It can be used to:

- View booking records
- Search booking information
- Check booking status
- Cancel bookings

---

# 🧪 Testing

The project can be tested using different scenarios.

| Test Case | Expected Result |
|---|---|
| Open application | Dashboard appears |
| View packages | Available packages displayed |
| Search package | Matching package displayed |
| Filter category | Packages filtered |
| Enter booking details | Details accepted |
| Select travelers | Price calculated |
| Confirm booking | Booking stored |
| Generate ticket | Ticket information displayed |
| View bookings | Existing bookings displayed |
| Cancel booking | Booking status updated |

---

# 🔐 Data Management

The application stores booking-related information in the local SQLite database.

The database makes it possible to preserve booking information even after the application is closed and reopened.

The project is intended primarily as an academic/demo application, so production-level security features such as encrypted databases, authentication, and cloud backups are not included by default.

---

# 🌟 Advantages

Wanderly provides several advantages:

- Easy-to-use interface
- Simple booking process
- Attractive GUI
- Fast package searching
- Category-based organization
- Automatic price calculation
- Local database storage
- Digital ticket generation
- Booking management
- Booking cancellation
- No external database server required
- Suitable for academic demonstration

---

# ⚠️ Limitations

The current version has some limitations:

- It is primarily a desktop application.
- SQLite is a local database.
- Online payment functionality is not included.
- Live hotel/flight availability is not included.
- Real-time travel APIs are not included.
- User authentication may not be available.
- Cloud synchronization is not included.
- Production-grade security is outside the current scope.

---

# 🚀 Future Scope

Wanderly can be further improved by adding:

### 🌐 Web Version

Convert the desktop application into a web-based travel platform using technologies such as:

```text
HTML
CSS
JavaScript
Python
Flask / Django
```

### 📱 Mobile Application

Develop Android and iOS applications for mobile booking.

### 💳 Online Payment

Integrate payment gateways for online transactions.

### 👤 User Authentication

Add:

- User registration
- Login
- Password management
- User profiles

### ☁️ Cloud Database

Move the local SQLite database to a cloud database for multi-user access.

### 🗺️ Maps Integration

Add interactive maps and destination locations.

### 🤖 AI Travel Assistant

An AI-powered assistant could recommend packages based on:

- Budget
- Destination
- Number of travelers
- Travel duration
- Interests

### 📧 Email Confirmation

Automatically send booking confirmations and digital tickets through email.

### 🌤️ Live Weather

Display current weather conditions for selected destinations.

### ⭐ Reviews & Ratings

Allow customers to rate packages and provide reviews.

---

# 📸 Screenshots

Add your project screenshots inside a `screenshots` folder.

Example:

```text
screenshots/
│
├── dashboard.png
├── packages.png
├── booking.png
├── ticket.png
└── booking-management.png
```

Then add them to this README:

```markdown
## 📸 Screenshots

### 🏠 Dashboard

![Dashboard](screenshots/dashboard.png)

### 🌎 Tour Packages

![Tour Packages](screenshots/packages.png)

### 📝 Booking

![Booking](screenshots/booking.png)

### 🎫 Digital Ticket

![Digital Ticket](screenshots/ticket.png)

### 📋 Booking Management

![Booking Management](screenshots/booking-management.png)
```

---

# 🎓 Academic Project

This project was developed as an academic/practical project to demonstrate the implementation of:

- Python programming
- GUI development
- Object-oriented programming concepts
- Event-driven programming
- SQLite database connectivity
- CRUD operations
- Form handling
- Data validation
- Application design

---

# 📚 Learning Outcomes

Through this project, the developer gained practical experience in:

- Python programming
- Tkinter GUI development
- SQLite database management
- SQL queries
- CRUD operations
- GUI event handling
- Form validation
- Data processing
- Software project development
- User interface design
- Project documentation

---

# 👨‍💻 Developer

### **Mohd Sahil**

**BCA Student**

Developed using:

```text
Python + Tkinter + SQLite
```

---

# 📄 License

This project is created for educational and academic purposes.

You are free to study, modify, and improve the project for learning purposes.

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ star on GitHub.

---

# ❤️ Thank You

Thank you for checking out **Wanderly – Luxury Travel & Tour Management System**.

```text
        ✈️ WANDERLY ✈️

   Explore the World.
   Discover New Places.
   Create New Memories.

        🌍 Happy Travelling! 🌍
```

---

## 🔖 GitHub Topics

You can add these topics to your GitHub repository:

```text
python
tkinter
sqlite
sqlite3
python-project
travel-management-system
tour-management
travel-booking
tour-booking
desktop-application
gui-application
python-gui
database-project
student-project
bca-project
wanderly
travel-management
```
