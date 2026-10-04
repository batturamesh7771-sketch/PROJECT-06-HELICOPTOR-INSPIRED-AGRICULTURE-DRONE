# PROJECT 06: Helicopter-Inspired Agricultural Spray Drone

An advanced agricultural hexacopter drone engineering repository containing 3D models, SolidWorks CAD parts, assemblies, automation macros, simulation scripts, and local project assets.

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/CAD-SolidWorks-red.svg)](SolidWorks_CAD_and_Macros/)
[![3D Mesh](https://img.shields.io/badge/3D-STL%20%7C%20OBJ-green.svg)](3D_Models/)

## 📌 Project Overview
* **Type:** Heavy-Lift Agricultural Spray Hexacopter (6-Rotor Radial Symmetry)
* **Wheelbase:** 1,500 mm (1.5 m diagonal span)
* **Frame & Arms:** Toray 3K carbon-fiber radial tubes with CNC aluminum clamping mounts
* **Canopy:** 6-lobed aerodynamic shell finished in Safety Yellow
* **Propulsion:** 6 high-torque brushless motors (8318 / 100KV) with folding carbon-fiber propeller blades (30-inch)
* **Payload:** Undermount 16L–20L translucent chemical spray tank with centrifugal atomizing nozzles
* **Landing Gear:** Carbon-fiber A-frame legs with longitudinal ground skids

## 📂 Repository Structure
```text
PROJECT_06_HELICOPTOR_INSPIRED_AGRICULTURE_DRONE/
├── 3D_Models/                    # STL, OBJ, and MTL 3D printable/CAD mesh files
│   ├── Realistic_Agricultural_Hexacopter.obj
│   ├── Realistic_Agricultural_Hexacopter.mtl
│   └── Realistic_Agricultural_Hexacopter.stl
├── SolidWorks_CAD_and_Macros/    # Native SolidWorks parts, assemblies, and automation macros
│   ├── Drone_Flight_Assembly.SLDASM
│   ├── Drone_Hex_Frame.SLDPRT
│   ├── Drone_Propeller.SLDPRT
│   ├── Agricultural_Hexacopter_Builder.vba
│   └── cad_automation_generator.py
├── Documentation/                # Technical specs, system architecture, and AI prompt workflows
│   ├── README.md
│   ├── TECHNICAL_SPECIFICATIONS.md
│   ├── SYSTEM_ARCHITECTURE.md
│   └── AI_PROMPT_LOGS.md
├── Laptop_Scanned_Assets/        # Drone assets collected from local machine & audit manifest
│   └── scanned_assets_manifest.json
├── push_to_github.py             # Standalone GitHub deployment script
└── README.md                     # Root project documentation
```

## 🚀 Quick Start
1. **SolidWorks CAD**: Open `SolidWorks_CAD_and_Macros/Drone_Flight_Assembly.SLDASM` in SolidWorks 2021 or newer.
2. **3D Printing / Visualization**: Load `3D_Models/Realistic_Agricultural_Hexacopter.stl` into Cura, PrusaSlicer, or Blender.
3. **Macro Automation**: Import `SolidWorks_CAD_and_Macros/Agricultural_Hexacopter_Builder.vba` into SolidWorks Macro Editor.
