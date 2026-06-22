# Battery Shortlist

This table is generated from `data/battery-candidates.csv`. Edit the CSV first, then run:

```sh
python3 scripts/generate_battery_shortlist.py
```

Only candidates with `status` set to `shortlisted` appear here. Rejected, alternate, and needs-follow-up candidates stay in the CSV for tracking.

## Current shortlisted candidates

<!-- BEGIN GENERATED: battery-shortlist -->
| Priority | Candidate | Supplier | Chemistry | Energy kWh | Nominal V | Voltage range | Continuous kW | Peak kW | Packaging | Weight | Cooling | BMS | Contactors / precharge / isolation | CAN | Missing verification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AMPHERR LFP-400-052 1F30 | AMPHERR AG | LFP | 52.2 | 384 | 300-438; OCV 357-425 at 5-95% SoC | ~51.8 at 384V | ~181.6 at 384V | 2050 x 1000 x 145 | 445-535 kg depending housing | Liquid, 10-15 L/min | Integrated | Integrated BMS/PJB/precharge/isolation measurement; contactors/fuse shown | CANBus 2.0A-B | quote, CAD, integration docs |
| 2 | American Battery Solutions T350V-50 | American Battery Solutions | Lithium Ion, exact chemistry UKN | 52 | 354 | UKN - verify from datasheet | ~63.7 at 354V | UKN | 1361 x 772 x 286 | UKN | Integrated liquid cooling | State-of-the-art BMS, ASIL-C functional safety per ABS page | UKN - ask ABS | UKN - ask ABS | datasheet, quote, CAD, integration docs |
| 3 | Hypercraft HyperPack Energy EX-24S24P-E 400V stack | Hypercraft | Li-ion NMC | 40.6 | 400V-class stack | 400V stack per Hypercraft docs | 81.3 | 121.9 | 4 x HyperPack units; each 30.4 x 14 x 6.3 in | 520 lb / 235.9 kg | WEG active chilling/heating; water-to-air optional | Integrated | UKN - ask Hypercraft | UKN - ask Hypercraft | quote, CAD, integration docs |
<!-- END GENERATED: battery-shortlist -->

## Verification rule

A candidate cannot move to `verified` until the project has received all four evidence types:

- Datasheet.
- Supplier quote.
- CAD file or package drawing.
- Integration documentation, including CAN/DBC or equivalent interface notes.
