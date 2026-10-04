# Technical Specifications: Project 06 Agricultural Spray Hexacopter

## 1. Frame Geometry & Structural Metrics
* **Configuration:** Hexacopter (6 radial arms, 60-degree radial symmetry)
* **Motor-to-Motor Diagonal:** 1,500 mm (1.5 m)
* **Boom Tube Outer Diameter:** 32 mm
* **Boom Tube Inner Diameter:** 29 mm (1.5 mm wall thickness, Toray 3K carbon-fiber weave)
* **Height:** 520 mm (Ground to canopy apex)
* **Center Frame Plate Thickness:** 3.0 mm high-modulus carbon-fiber dual plate sandwich
* **Arm Folding Mechanism:** CNC 6061-T6 aviation aluminum quick-fold clamps with dual safety locks

## 2. Propulsion System
* **Motor Specification:** 8318 / 100KV Brushless Outrunner Motors
* **Propeller Type:** 30-inch (762 mm) carbon-fiber folding blades (30x10.5 pitch)
* **ESC:** 12S 80A / 100A FOC High-Voltage Smart ESCs with CAN bus feedback
* **Maximum Thrust per Rotor:** 13.5 kg
* **Total Maximum Thrust:** 81.0 kg (Thrust-to-weight ratio > 2.1 at MTOW)

## 3. Agricultural Liquid Spray System
* **Spray Tank Capacity:** 16 L to 20 L with integrated anti-slosh baffle system
* **Pumps:** Dual 12S brushless high-pressure diaphragm pumps (Max flow rate: 5.5 L/min)
* **Spray Head Type:** 6 under-motor centrifugal atomizing spray nozzles
* **Droplet Size:** 50 – 300 μm adjustable
* **Effective Spray Width:** 5.5 m – 7.5 m depending on flight altitude (1.5 – 3.0 m above canopy)

## 4. Power & Flight Electronics
* **Battery:** Dual 6S / 12S 22,000 mAh High-Density LiPo / Solid-State packs
* **Flight Controller:** Dual IMU redundant flight control unit with RTK centimeter-level positioning
* **Obstacle Avoidance:** Front and rear spherical millimeter-wave radar + terrain-following bottom radar
* **Telemetry & Link:** 2.4 GHz / 5.8 GHz dual-frequency encrypted long-range link (5 km range)
