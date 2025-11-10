# Project 07: IT Infrastructure Intelligence for AIMS Senegal

## 🏫 Business Context

**African Institute for Mathematical Sciences (AIMS) Senegal** is a pan-African center of excellence in mathematical sciences, hosting students, researchers, and faculty from across Africa. The campus operates 24/7 with intensive computational needs, research activities, and administrative operations.

The IT and Facilities Management team faces several critical operational challenges:

- **Equipment Reliability**: Frequent equipment failures disrupt academic activities and research
- **Energy Costs**: High electricity consumption affecting operational budget
- **Maintenance Planning**: Reactive rather than proactive maintenance leading to costly downtime
- **Resource Optimization**: Inefficient utilization of computing resources and facilities
- **Security Concerns**: Need to monitor network activity and detect anomalies
- **Budget Constraints**: Limited funds require data-driven procurement and replacement decisions
- **Environmental Sustainability**: Need to reduce energy consumption and carbon footprint

The campus infrastructure includes 78 devices across 6 departments, generating hourly operational logs. The administration needs comprehensive insights to:
- Reduce operational costs through better resource management
- Improve service reliability for students and researchers
- Plan equipment procurement and replacement strategically
- Optimize energy consumption
- Enhance security and monitoring

As **Data Analysts** within the IT Department at AIMS Senegal, your team has been tasked with performing comprehensive log analysis across all equipment and departments on campus to support data-driven decision-making.

---

## 📊 Dataset Overview

### Data Collection Summary
- **Total Records**: 168,480 hourly log entries
- **Date Range**: January 1, 2025 - March 31, 2025 (3 months)
- **Departments**: 6 (Academic Director Office, Computer Lab, Finance & Logistics, Kitchen, Research Lab, TA Office)
- **Devices**: 78 devices across campus
- **Device Types**: 11 (laptops, desktops, printers, routers, AC units, stoves, refrigerators, displays, audio, supercomputer, water dispenser)
- **Brands**: 15 different manufacturers

### Device Distribution by Department:
- **Academic Director Office**: 4 devices
- **Computer Lab**: 35 devices (largest department)
- **Finance & Logistics**: 9 devices
- **Kitchen**: 11 devices
- **Research Lab**: 11 devices
- **TA Office**: 8 devices

### Device Distribution by Type:
- **Computing**: 33 desktops, 16 laptops, 1 supercomputer
- **Networking**: 7 routers
- **Peripherals**: 6 printers, 2 displays, 1 audio system
- **Facilities**: 4 AC units, 4 stoves, 3 refrigerators, 1 water dispenser

---

## 🏢 Campus Infrastructure Details

### Academic Director's Office
- 1 Laptop (Dell Latitude)
- 1 Printer (HP LaserJet)
- 1 Air Conditioner (Samsung)
- 1 Router (Cisco)

### Teaching Assistant (TA) Office
- 5 Laptops (3 Dell, 2 HP)
- 1 Printer (Canon)
- 1 Air Conditioner (LG)
- 1 Water Dispenser (hot/cold - Midea)

### Research Lab
- 5 Laptops (Dell Precision workstations)
- 2 Printers (HP LaserJet)
- 1 Supercomputer (Custom build - 64 cores)
- 1 Router (Cisco)
- 1 Big Screen Display (Samsung 85")
- 1 Air Conditioner (Daikin - Industrial)

### Finance and Logistics Department
- 5 Laptops (4 Dell, 1 HP)
- 2 Printers (1 HP, 1 Canon)
- 1 Air Conditioner (Samsung)
- 1 Router (TP-Link)

### Kitchen Department
- 4 Electric Stoves (Bosch, Samsung, Huawei, Russell Hobbs)
- 3 Desktop Computers (All Dell OptiPlex)
- 3 Refrigerators (Samsung, LG, NAGU)
- 1 Router (TP-Link)

### Computer Lab
- 30 Desktop Stations (All Dell OptiPlex 7090)
- 1 Big Screen Display (Huawei 98")
- 1 Audio Equipment (Bose Conference System)
- 3 Routers (2 Cisco, 1 TP-Link)

---

## 📊 Detailed Dataset Description

### Data Collection Period
- **Duration**: 3 months (January 1, 2025 - March 31, 2025)
- **Frequency**: Hourly logs (24 readings per day)
- **Total Records**: 168,480 log entries

### Available Data Files
The data is organized in multiple CSV files in the `aims_senegal_logs_data` folder:
- **By Department**: Separate files for each department
- **By Device Type**: Separate files for each device type
- **Complete Dataset**: `aims_senegal_complete_logs.csv` containing all logs

### Log Data Structure

Each device generates hourly logs with the following attributes:

#### **Common Fields (All Devices)**
- `timestamp`: Date and time of log entry (hourly)
- `device_id`: Unique identifier (e.g., "LAP_ACAD_DIR_001")
- `device_type`: Type of equipment (laptop, printer, AC, router, etc.)
- `device_brand`: Manufacturer (Dell, HP, Samsung, etc.)
- `department`: Department name
- `office_location`: Specific office/room
- `status`: Operational status (online, offline, standby, error)
- `power_consumption_kwh`: Energy consumption in kWh
- `uptime_hours`: Hours since last restart
- `error_count`: Number of errors in the hour
- `warning_count`: Number of warnings in the hour

#### **Network Devices (Routers)**
- `network_traffic_gb`: Data transferred (GB)
- `connected_devices`: Number of connected devices
- `bandwidth_utilization_percent`: Bandwidth usage (%)
- `packet_loss_percent`: Network packet loss (%)
- `latency_ms`: Network latency (milliseconds)
- `failed_connections`: Failed connection attempts

#### **Computing Devices (Laptops, Desktops, Supercomputer)**
- `cpu_usage_percent`: CPU utilization (%)
- `memory_usage_percent`: RAM utilization (%)
- `disk_usage_percent`: Storage utilization (%)
- `temperature_celsius`: Device temperature (°C)
- `active_processes`: Number of running processes
- `login_count`: Number of user logins in the hour
- `session_duration_minutes`: Average session length

#### **Printers**
- `pages_printed`: Number of pages printed
- `ink_level_percent`: Ink/toner level (%)
- `paper_jams`: Number of paper jams
- `print_queue_length`: Jobs waiting to print

#### **Air Conditioners**
- `room_temperature_celsius`: Room temperature (°C)
- `set_temperature_celsius`: Target temperature (°C)
- `humidity_percent`: Room humidity (%)
- `fan_speed`: Fan speed (low, medium, high, auto)
- `mode`: Operating mode (cooling, heating, fan, auto)

#### **Kitchen Equipment (Stoves, Refrigerators)**
- `temperature_celsius`: Operating temperature
- `power_state`: On/Off/Standby
- `usage_duration_minutes`: Active usage time
- `door_open_count`: (Refrigerators only) Door openings

#### **Water Dispenser**
- `hot_water_dispensed_liters`: Hot water usage
- `cold_water_dispensed_liters`: Cold water usage
- `heating_element_status`: On/Off
- `cooling_element_status`: On/Off

---

## 🎯 Your Mission

The IT Department and Campus Administration need comprehensive insights to optimize operations, reduce costs, and improve service reliability. This project integrates all your data preprocessing skills: **tabular data manipulation**, **time series analysis**, and **data visualization**.

### Expected Deliverables:

#### 1. **Comprehensive Data Exploration and Integration**
   - Load and explore data from multiple CSV files (by department, by device type, or complete dataset)
   - Understand the structure and relationships between different data files
   - Identify data quality issues, missing values, and outliers
   - Generate summary statistics for key operational metrics
   - Integrate data from different sources as needed for analysis

#### 2. **Equipment Performance Analysis**
   - Analyze uptime and reliability across devices and departments
   - Identify devices with frequent errors or warnings
   - Examine equipment failure patterns
   - Compare performance across device brands and types
   - Provide recommendations for equipment replacement or maintenance

#### 3. **Energy Consumption Analysis**
   - Analyze power consumption patterns across devices and departments
   - Identify energy-intensive equipment
   - Examine temporal patterns in energy usage (hourly, daily, weekly)
   - Calculate energy costs and identify optimization opportunities
   - Provide recommendations for reducing electricity consumption

#### 4. **Time Series Analysis**
   - Analyze temporal patterns in equipment usage (peak hours, quiet periods)
   - Examine seasonal or weekly patterns in different departments
   - Identify optimal maintenance windows with minimal disruption
   - Analyze trends in equipment performance over the 3-month period
   - Detect anomalies and unusual patterns in time series data

#### 5. **Network Infrastructure Analysis** (Routers)
   - Analyze network traffic patterns across campus
   - Examine bandwidth utilization and identify congestion periods
   - Analyze network reliability (packet loss, latency, failed connections)
   - Compare network performance across departments
   - Provide recommendations for network optimization

#### 6. **Computing Resources Analysis** (Laptops, Desktops, Supercomputer)
   - Analyze CPU, memory, and disk utilization patterns
   - Identify underutilized or overutilized computing resources
   - Examine temperature patterns and cooling efficiency
   - Analyze user activity patterns (logins, session durations)
   - Compare performance between Research Lab and Computer Lab
   - Assess supercomputer utilization and efficiency

#### 7. **Facilities Management Analysis** (AC, Kitchen Equipment)
   - Analyze air conditioning efficiency and room temperature control
   - Examine kitchen equipment usage patterns
   - Analyze refrigerator performance and energy efficiency
   - Identify facilities optimization opportunities

#### 8. **Department-Level Analysis**
   - Compare operational metrics across departments
   - Analyze resource utilization by department
   - Identify departments with efficiency issues or high costs
   - Provide department-specific recommendations

#### 9. **Anomaly Detection and Security**
   - Identify unusual patterns in device behavior
   - Detect potential security issues (unusual network activity, login patterns)
   - Identify devices requiring immediate attention
   - Flag potential equipment failures before they occur

#### 10. **Data Visualization and Dashboards**
   - Create comprehensive visualizations for different stakeholder groups
   - Develop time series plots showing usage patterns and trends
   - Create comparative visualizations across departments and device types
   - Design executive dashboards with key performance indicators
   - Ensure visualizations are clear, informative, and actionable

#### 11. **Cost-Benefit Analysis**
   - Calculate operational costs (energy, maintenance) by department and device
   - Identify cost-saving opportunities
   - Provide ROI analysis for equipment upgrades or replacements
   - Support budget planning with data-driven projections

#### 12. **Actionable Insights and Recommendations**
   - Provide strategic recommendations for infrastructure improvements
   - Suggest equipment procurement priorities
   - Recommend energy optimization strategies
   - Advise on maintenance scheduling and resource allocation
   - Support decision-making with evidence-based insights

---