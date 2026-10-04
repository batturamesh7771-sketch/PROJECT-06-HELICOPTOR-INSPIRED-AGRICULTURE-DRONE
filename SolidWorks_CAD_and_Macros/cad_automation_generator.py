"""
SolidWorks & CAD Parametric Automation Script
Project 06: Helicopter-Inspired Heavy-Lift Agricultural Drone
"""
import math
import os

SPECS = {
    "type": "Agricultural Spray Hexacopter",
    "diagonal_wheelbase_mm": 1500,
    "arm_count": 6,
    "boom_outer_diameter_mm": 32,
    "boom_wall_thickness_mm": 1.5,
    "propeller_diameter_inches": 30,
    "motor_type": "8318 / 100KV Brushless Outrunner",
    "payload_capacity_liters": 20,
    "nozzle_count": 6,
}

def print_cad_hierarchy():
    print("Agricultural Hexacopter CAD Model Hierarchy:")
    print("├── Top Central Plate (Toray 3K Carbon Fiber, 3.0 mm)")
    print("├── Bottom Central Plate with Power Distribution")
    print("├── 6x CNC Aluminum Arm Clamps (Radial 60 deg spacing)")
    print("├── 6x 32mm Carbon Fiber Booms (750 mm length)")
    print("├── 6x Motor Mount Plates with Atomizing Nozzle Brackets")
    print("├── 6x 8318 High-Torque Brushless Motors")
    print("├── 6x 30-inch Folding Carbon-Fiber Propellers")
    print("├── Undermount 20L Quick-Release Chemical Tank")
    print("└── A-Frame Landing Skids with Ground Buffer")

if __name__ == "__main__":
    print_cad_hierarchy()
