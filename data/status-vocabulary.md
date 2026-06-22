# Status Vocabulary

- `discovered`: candidate found but not investigated.
- `needs-datasheet`: public specs insufficient.
- `needs-quote`: datasheet exists but price/orderability unknown.
- `shortlisted`: technically promising and worth supplier follow-up.
- `verified`: specs, price, orderability, CAD, and integration docs confirmed.
- `alternate`: useful but not preferred.
- `performance-alternate`: strong power but lower capacity or non-preferred chemistry.
- `prototype-only`: useful for bench/low-speed prototype, not full vehicle reference.
- `rejected`: not suitable for current reference target.

## Unknown values

Use `UKN` for unknown CSV values. Do not leave cells blank.

## Verified status rule

A battery candidate can only move to `verified` when all of the following evidence has been received or linked:

- Datasheet.
- Supplier quote.
- CAD file or package drawing.
- Integration documentation, including CAN/DBC or equivalent interface notes.
