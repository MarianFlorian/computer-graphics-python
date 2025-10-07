# Computer Graphics (Python) — Course Assignments

## Overview
This repository contains 7 assignments developed during the **Computer Graphics** course.  
Each assignment demonstrates concepts such as coordinate transformations, interpolation, rasterization, and simple game development using Python.

---

## Assignments

### Tema 1 — Coordinate transformations
- Convert coordinates between Cartesian and polar (and vice versa).
- Rotate point A(2,4) around origin O(0,0) by 30°.
- Apply symmetry of point A(-3,-2) with respect to center M(5,5).
- **File:** `tema1.py`

---

### Tema 2 — Aitken’s Algorithm
- Implementation of Aitken’s Δ² method.
- **File:** `tema2.py`

---

### Tema 3 — Orthogonal axes and lines
- Generate OXY axes and draw:
  - one vertical line
  - one horizontal line
  - one oblique line  
- Each line has a different color.
- **File:** `tema3.py`

---

### Tema 4 — 3D Transformation
- Implementation of one 3D geometric transformation studied in class.
- **File:** `tema4.py`

---

### Tema 5 — Bresenham Rasterization Algorithm
- Implementation of Bresenham’s line rasterization.
- **File:** `tema5.py`

---

### Tema 6 — Pygame Scene
- Static objects: 2 snowmen.
- Animated objects: rotating snowflake, moving airplane.
- **File:** `tema6.py`

---

### Tema 7 — Space Invaders (Pygame)
- Features:
  - Player moves left (A) / right (D) and shoots (Space).
  - Destructible bunkers.
  - Enemies arranged in 5 rows.
  - Closest enemy in each column attacks.
  - Score & High-Score (saved between runs).
- **Files:**  
  - `tema7.py`  
  - `score.txt`  
  - `highscore.txt`

---

## How to Run
1. Install dependencies:
   ```bash
   pip install pygame numpy matplotlib
