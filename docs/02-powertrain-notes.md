# Powertrain Notes

## Reference motor: Bosch SMG180 OHW

The Bosch SMG180 OHW is currently used as a reference traction motor target because it is a 400 V-class motor with published specifications near the desired power level.

Known reference specs gathered so far:
- Nominal power: 60 kW.
- Maximum power: 90 kW.
- Nominal torque: 95 Nm.
- Maximum torque: 200 Nm.
- Maximum speed: about 12,000–12,800 rpm depending source/version.
- Voltage: up to roughly 425–430 VDC depending source/version.
- Cooling: water-glycol, approximately 6–8 L/min.
- Weight: around 30 kg.

## Derived battery-output target

| Pack voltage | 60 kW current | 90 kW current | 120 kW current |
|---:|---:|---:|---:|
| 300 V | 200 A | 300 A | 400 A |
| 350 V | 171 A | 257 A | 343 A |
| 384 V | 156 A | 234 A | 313 A |
| 400 V | 150 A | 225 A | 300 A |

Lower-voltage packs are not automatically wrong, but the inverter and cabling must handle higher current for the same power.
