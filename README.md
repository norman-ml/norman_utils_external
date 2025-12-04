# Utils External

The Utils External package contains helper utilities that are shared across Norman SDKs and backend services but are not part of the core object model or the primary SDK interfaces. These utilities provide common functionality that supports serialization, validation, formatting, hashing, encoding, and other cross-cutting concerns used throughout the Norman ecosystem.

If you’re building internal Norman services or maintaining the SDKs, this package provides the building blocks that keep everything consistent and predictable.

# Why Utils External Exists

Different Norman services often need to perform the same kinds of operations:

- validating parameters
- hashing files
- normalizing text
- encoding/decoding data formats
- generating timestamps and IDs
- converting objects to JSON-proof structures
- Without shared utilities, each service would re-implement its own version, leading to drift and subtle inconsistencies.

Utils External ensures all Norman components behave the same way.