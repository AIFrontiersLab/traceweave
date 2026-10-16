# TraceWeave

Generate accurate schematics and pinout maps from PCB images and logic traces.

# Task MVP

A simple task management API.

## Usage

Run server:
uvicorn main:app --reload

Test:
pytest -q

## Architecture

![Architecture](docs/architecture.png)

<details>
<summary>Mermaid source</summary>

```mermaid
flowchart LR
    A[PCB Image] --> B[TraceWeave Engine]
    C[Logic Trace] --> B
    B --> D[Schematic]
    B --> E[Pinout Map]
    F[FastAPI MVP] --> G[Task API]
```

</details>
