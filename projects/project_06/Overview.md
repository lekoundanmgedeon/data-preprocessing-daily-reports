# Project 06: Inventory Intelligence for SenLogistics

## 📦 Business Context

**SenLogistics** is a prominent logistics and distribution company operating multiple warehouses across various regions in Senegal, including Dakar, Kaolack, Ziguinchor, and Tambacounda. The company serves as a critical link in the supply chain, managing inventory for electronics, furniture, toys, and other consumer goods across the country.

Recently, the company has encountered several operational challenges:

- **Stock Management**: Frequent stockouts of popular items leading to lost sales
- **Overstocking**: Excess inventory tying up capital and warehouse space
- **Supplier Performance**: Inconsistent delivery times and quality from different suppliers
- **Regional Imbalances**: Some warehouses are overstocked while others face shortages
- **Product Category Optimization**: Unclear which product categories are most profitable
- **Restocking Efficiency**: Inefficient restocking schedules leading to operational costs
- **Warehouse Utilization**: Uneven distribution of inventory across warehouse locations
- **Pricing Strategy**: Need to understand pricing patterns across categories and locations

These inefficiencies are impacting the company's ability to meet customer demands, manage warehouse costs effectively, and maintain competitive advantage in Senegal's growing e-commerce and retail market.

As a newly hired **Supply Chain Data Analyst** at SenLogistics, you have been tasked with analyzing the warehouse data to uncover insights that can enhance the overall inventory and supplier management process.

---

## 📊 Dataset Description

You have been provided access to the company's warehouse database in a CSV file named `SenLogistics_warehouses.csv` containing comprehensive inventory information across all warehouse locations.

### Data Fields:
- **Product_ID**: Unique product identifier
- **Product_Name**: Name of the product
- **Category**: Product category (Electronics, Furniture, Toys, etc.)
- **Warehouse**: Warehouse location (Dakar Warehouse, Kaolack Warehouse, Ziguinchor Warehouse, Tambacounda Warehouse)
- **Quantity**: Current stock quantity
- **Price**: Product price in local currency
- **Status**: Stock status (In Stock, Out of Stock, Low Stock)
- **Date**: Date of last inventory update or restocking
- **Supplier**: Supplier name (e.g., Dieng Shipment, SenTrack Logistics, Bouba Livraison)

### Inventory Characteristics:
- **Multi-Location**: Data from warehouses across Senegal
- **Product Diversity**: Multiple product categories
- **Stock Status Tracking**: Real-time inventory status
- **Supplier Information**: Multiple supplier relationships
- **Temporal Data**: Historical inventory dates

---

## 🎯 Your Mission

Your client is particularly interested in understanding the status and management of various products in the warehouse, as this information is crucial for making informed decisions on inventory management, supplier optimization, and restocking policies.

### Expected Deliverables:

1. **Comprehensive Inventory Analysis**
   - Examine the structure and quality of the inventory dataset
   - Identify data quality issues, missing values, and outliers
   - Generate summary statistics for inventory levels and pricing
   - Understand the distribution of products across warehouses and categories

2. **Stock Status Analysis**
   - Analyze the distribution of stock statuses (In Stock, Out of Stock, Low Stock)
   - Identify products and categories with frequent stockouts
   - Examine overstocking patterns
   - Calculate stock availability rates across warehouses

3. **Product Category Performance**
   - Compare inventory levels across product categories
   - Analyze pricing patterns by category
   - Identify high-value and high-volume categories
   - Assess category profitability potential (price × quantity)

4. **Warehouse Performance Analysis**
   - Compare inventory distribution across warehouse locations
   - Analyze stock status by warehouse
   - Identify warehouses with capacity issues or inefficiencies
   - Examine regional inventory patterns

5. **Supplier Performance Analysis**
   - Compare inventory levels and stock status by supplier
   - Analyze supplier reliability (stockout rates)
   - Examine pricing patterns across suppliers
   - Identify high-performing and underperforming suppliers

6. **Inventory Value Analysis**
   - Calculate total inventory value by warehouse, category, and supplier
   - Identify high-value inventory items
   - Analyze capital tied up in inventory
   - Assess inventory turnover implications

7. **Temporal Analysis**
   - Analyze inventory age and restocking patterns
   - Identify slow-moving inventory
   - Examine seasonal or temporal patterns in restocking
   - Assess inventory freshness across warehouses

8. **Data Visualization**
   - Create compelling visualizations to communicate inventory insights
   - Use appropriate charts for inventory comparisons
   - Develop dashboards showing key inventory metrics
   - Ensure visualizations are suitable for operations management

9. **Actionable Insights and Recommendations**
   - Provide recommendations for optimizing stock levels
   - Suggest restocking policies to minimize stockouts and overstocking
   - Recommend supplier optimization strategies
   - Advise on warehouse capacity planning and inventory redistribution
   - Support pricing strategy with data-driven insights

---
