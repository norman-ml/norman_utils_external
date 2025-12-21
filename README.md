# Norman Utils (External)

`norman-utils-external` is a lightweight Python utility library intended for **external-facing services, SDKs, and integrations** that interact with the Norman AI platform.

Unlike `norman-objects`, this package focuses on **practical helpers and utilities**, not core domain models. It is safe to depend on from client libraries and edge services.

---

## 🎯 Purpose

Norman Utils (External) exists to:

* Provide **reusable utility functions** shared across external components
* Reduce boilerplate in SDKs and integrations
* Encapsulate common patterns (serialization, validation, helpers)
* Avoid leaking internal platform complexity to external consumers

This package is intentionally **thin, stable, and dependency-light**.

---

## Position in the Norman Ecosystem

| Package                 | Responsibility                        |
| ----------------------- | ------------------------------------- |
| `norman-objects`        | Core domain models & contracts        |
| `norman-utils-external` | Generic helpers safe for external use |
| Services / SDKs         | Business logic & workflows            |

If something is:

* **A contract** → it belongs in `norman-objects`
* **A helper or convenience** → it likely belongs here

---

## 📦 Typical Contents

This package may include:

* Serialization / deserialization helpers
* Encoding & decoding utilities
* Validation helpers
* Type conversion utilities
* Safe wrappers around common patterns
* Small, stateless helper functions

---

## Design Principles

* **External-safe**: no internal assumptions
* **No business logic**
* **Minimal dependencies**
* **Pure functions preferred**
* **Backward compatibility first**

If a utility requires deep knowledge of the Norman runtime, it does **not** belong here.

---

## Versioning & Stability

This package follows conservative versioning:

* Backward-compatible changes by default
* New utilities are additive
* Breaking changes are rare and explicit

External consumers should be able to upgrade with confidence.

---

## What Does *Not* Belong Here

* Domain models
* Invocation lifecycle logic
* Security-sensitive internals
* Infrastructure or orchestration code
* Anything requiring privileged context
---

## Intended Consumers

* External SDKs
* Edge services
* Integration layers
* Client-side tooling
* Third-party adapters


---

## License

Internal Norman AI project. Usage governed by internal and partner agreements.
