# Codex Handoff Prompt

You are helping create an open-source electric American kei-truck project repository.

Use the files in this repo scaffold as the starting point. Your first tasks:

1. Convert the current docs into a clean, navigable GitHub repository.
2. Improve the `README.md` so a new contributor understands the scope in under 5 minutes.
3. Keep `data/battery-candidates.csv` as the source of truth for battery comparisons.
4. Add validation scripts that check the CSV for missing required fields.
5. Add markdown tables generated from the CSV into `docs/04-battery-shortlist.md`.
6. Add GitHub issue templates for battery candidates, supplier quotes, and design decisions.
7. Do not hard-code one battery. Keep the architecture based on a battery envelope and interface spec.
8. Treat all supplier data as unverified until a datasheet, quote, CAD file, and integration documentation are received.
9. Add clear statuses: discovered, needs-datasheet, needs-quote, shortlisted, verified, rejected.

Primary design target:
- 35–55 kWh usable energy target.
- LFP preferred.
- 300–430 V operating window.
- At least 60 kW continuous and 120 kW peak battery output.
- Integrated BMS, contactors, fuse, precharge, HVIL, isolation monitoring, CAN, and liquid cooling preferred.

Important caveat:
The Bosch SMG180 OHW is a reference target, not a locked motor. Battery voltage and inverter choice must be validated as a system.
