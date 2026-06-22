# Powertrain Notes

## Reference motor: Bosch SMG180 OHW

The Bosch SMG180 OHW is currently used as a reference traction motor target because it is a 400 V-class motor with published specifications near the desired power level.

## Sourcing status

Bosch should be treated as a reference-spec and Tier 1 / B2B supplier, not a consumer parts source. The project should not assume that a new SMG180 OHW can be purchased directly by an individual builder.

The only currently tracked individual-builder sourcing path is a salvaged Bosch SMG-family motor from a Fiat 500e, usually through eBay, salvage yards, or EV dismantlers. Any salvaged unit must be validated as a complete usable system, not just a loose motor:

- Motor part number and variant.
- Matching inverter or proven compatible inverter/controller.
- Resolver/position-sensor interface.
- Coolant fittings and flow requirements.
- Gear reduction, differential, or shaft interface.
- HV connector family and safe cable termination.
- CAN/control documentation or a proven open controller path.

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

## Motor candidate direction

| Candidate | Current role | Why |
|---|---|---|
| Bosch SMG180 OHW / Fiat 500e salvage | Reference spec; salvage-only individual-builder path | Fits the voltage and power target, but Bosch direct sourcing is Tier 1 / B2B. |
| Nissan Leaf EM57 drive unit | Practical budget shortlist | Best current combination of salvage availability, inverter/reduction integration, and aftermarket controller support. |
| Chevrolet Bolt EV drive unit | Performance salvage alternate | Strong power and torque, but the repeatable open controller path needs more proof. |
| Cascadia Motion iM-225 | Premium benchmark alternate | Excellent integrated motor/inverter documentation, but likely too expensive for the first build. |
| Hypercraft R300Si / R300S | Turnkey premium alternate | Integrated powertrain package, VCU, harness, and cooling, but likely too expensive and less open. |
| NetGain HyPer 9 HV | Lower-voltage DIY alternate | Good kit ecosystem, but conflicts with the current 300-430V architecture and has lower continuous power. |
| HPEVS AC-50 / AC-51 | Low-speed mule candidate | Useful for lightweight prototypes, likely below the full utility-truck target. |
| NetGain WarP 9 / D&D brushed DC | DC prototype-only comparison | Brushed DC is real and purchasable, but not the main architecture due to voltage/current, maintenance, regen, and control tradeoffs. |
