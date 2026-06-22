# Contributing

This project is still in research and architecture definition. Contributions are most useful when they make the evidence trail clearer.

## Working Rules

- Keep `data/battery-candidates.csv` as the source of truth for battery comparisons.
- Keep `data/component-candidates.csv` as the source of truth for whole-vehicle component sourcing.
- Use `UKN` for unknown CSV values instead of leaving cells blank.
- Do not move a candidate to `verified` until datasheet, quote, CAD/package file, and integration documentation are all received.
- Treat supplier pages, marketplace listings, screenshots, and emails as unverified until evidence is attached or linked.
- Keep the vehicle architecture based on a battery envelope and interface spec, not a single locked battery.
- Keep the Bosch SMG180 OHW as a reference motor target only; Bosch direct sourcing should be treated as Tier 1 / B2B, while individual-builder sourcing should focus on complete Fiat 500e salvage packages until proven otherwise.

## Before Opening a Pull Request

Run:

```sh
python3 scripts/validate_battery_candidates.py
python3 scripts/validate_component_candidates.py
python3 scripts/generate_battery_shortlist.py --check
```

If you edit `data/battery-candidates.csv`, regenerate the shortlist table:

```sh
python3 scripts/generate_battery_shortlist.py
```

## Issue Types

- Use the battery candidate template for new packs, corrections, and status changes.
- Use the supplier quote template for quote, MOQ, lead-time, CAD, and CAN/DBC follow-up.
- Use the design decision template when a change affects requirements, architecture, safety, or supplier strategy.
