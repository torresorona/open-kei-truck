# Next Steps

## Immediate

1. Create a public GitHub repository.
2. Commit this scaffold.
3. Open issues for AMPHERR, ABS, Hypercraft, CTS, and Bosch.
4. Request quotes and CAD.
5. Request CAN/DBC or integration manuals.
6. Add weight data as soon as each supplier responds.
7. Do not freeze the chassis until battery envelope and motor/inverter voltage are validated.

## First technical milestone

Create a validated battery bay envelope for:
- AMPHERR 1F30 flat slab.
- ABS T350V-50 compact/tall block.
- Hypercraft 4-pack modular stack.
- CTS custom 96S/108S/120S block layout.

## First repo automation

Create a simple script that:
- Reads `data/battery-candidates.csv`.
- Flags missing fields.
- Calculates approximate continuous and peak kW from voltage/current when possible.
- Generates a markdown shortlist table.
