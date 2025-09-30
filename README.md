# Car Rental Management System

## Overview

A Python-based car rental management system that implements object-oriented programming principles to handle car rentals, inventory management, and customer interactions. The system supports both regular customers and VIP customers with differentiated pricing structures and service levels.

## Project Description

This project demonstrates the application of object-oriented design patterns, inheritance, and encapsulation to create a functional car rental business management system. The application provides a command-line interface for customers to interact with the rental service, including browsing available vehicles, making reservations, and returning rented cars.

### System Architecture

The system is built using a modular design with four main Python classes:

1. **CarRentalShop**: Core business logic class managing inventory and pricing
2. **Customer**: Base class for regular customers with standard rental capabilities
3. **VipCustomer**: Inherits from Customer class with special pricing and privileges
4. **Main**: Application entry point providing user interface and navigation

### Key Features

- **Inventory Management**: Real-time tracking of available vehicles by type
- **Dynamic Pricing**: Different rates based on rental duration and customer status
- **Customer Segmentation**: Separate pricing tiers for regular and VIP customers
- **Interactive Interface**: Menu-driven system with input validation and error handling
- **Rental Processing**: Complete rental lifecycle from booking to return with billing

## System Components

### CarRentalShop Class
- Manages inventory for three vehicle types: Hatchback, Sedan, SUV
- Implements dynamic pricing based on rental duration
- Handles rental processing and vehicle returns
- Maintains separate pricing structures for regular and VIP customers

### Customer Classes
- **Customer**: Base class with standard rental functionality
- **VipCustomer**: Inherits from Customer with access to special VIP rates
- Both classes provide methods for inquiring, renting, and returning vehicles

### Pricing Structure

**Regular Customer Rates:**
- Hatchback: $30/day (<7 days), $25/day (≥7 days)
- Sedan: $50/day (<7 days), $40/day (≥7 days)
- SUV: $100/day (<7 days), $90/day (≥7 days)

**VIP Customer Rates:**
- Hatchback: $20/day (flat rate)
- Sedan: $35/day (flat rate)
- SUV: $80/day (flat rate)

## Key Deliverables

### 1. Functional Software System
- Complete car rental management application
- Working command-line interface with menu navigation
- Error handling and input validation throughout the system

### 2. Object-Oriented Design Implementation
- Proper class hierarchy with inheritance between Customer and VipCustomer
- Encapsulation of business logic within appropriate classes
- Method overriding to implement VIP-specific functionality

### 3. Business Logic Features
- **Inventory Tracking**: Real-time stock management with automatic updates
- **Pricing Engine**: Dynamic pricing based on customer type and rental duration
- **Rental Processing**: Complete transaction handling from booking to billing
- **Customer Management**: Support for different customer tiers with appropriate privileges

### 4. User Experience Components
- Interactive menu system with clear navigation options
- Comprehensive input validation and error messages
- Professional billing system with detailed rental summaries
- Graceful handling of edge cases (no inventory, invalid inputs, etc.)

## Technical Implementation

### Design Patterns Used
- **Inheritance**: VipCustomer extends Customer functionality
- **Encapsulation**: Private data members and public interface methods
- **Polymorphism**: Method overriding for VIP-specific behavior

### Code Structure
- **Modular Design**: Separate files for each class promoting maintainability
- **Clean Architecture**: Clear separation between data, business logic, and presentation
- **Error Handling**: Comprehensive validation and user-friendly error messages

## Results and Conclusions

### Technical Achievements

1. **Successful OOP Implementation**: The project demonstrates proper object-oriented design principles with clear class hierarchies and appropriate use of inheritance.

2. **Robust Business Logic**: The system successfully handles complex pricing scenarios, inventory management, and customer segmentation.

3. **User-Friendly Interface**: Despite being a command-line application, the system provides an intuitive user experience with clear menus and helpful feedback.

4. **Scalable Architecture**: The modular design allows for easy extension to add new vehicle types, customer categories, or pricing models.

### Business Value

- **Operational Efficiency**: Automates rental process reducing manual errors and processing time
- **Revenue Optimization**: Dynamic pricing structure maximizes revenue based on rental duration
- **Customer Retention**: VIP program encourages customer loyalty through preferential pricing
- **Inventory Management**: Real-time stock tracking prevents overbooking and optimizes fleet utilization

### Educational Outcomes

The project successfully demonstrates:
- Object-oriented programming concepts in a real-world context
- Inheritance and polymorphism implementation
- Business logic separation and encapsulation
- User interface design for console applications
- Error handling and input validation techniques

### Potential Enhancements

The system provides a solid foundation that could be extended with:
- Database integration for persistent data storage
- Web-based or GUI interface for improved user experience
- Advanced features like reservations, customer history, and reporting
- Integration with payment processing systems
- Multi-location inventory management

This car rental management system serves as an excellent example of applying object-oriented programming principles to solve real-world business problems while maintaining code quality, readability, and extensibility.
