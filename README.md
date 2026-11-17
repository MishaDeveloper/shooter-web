# Shooter Game

A simple 2D space shooter developed in Python using Pygame and adapted to run in a web browser with Pygbag and WebAssembly.

## Play Online

**[Play Shooter Game](https://mishadeveloper.github.io/shooter-web/)**

No installation required. Play directly in your browser on desktop or mobile.

## Features

- Player-controlled spaceship
- Alien targets with increasing speed
- Projectile shooting and collision detection
- Score tracking
- Keyboard, mouse, and touchscreen controls
- Browser support using WebAssembly

## Controls

**Desktop**
- Left / Right Arrow — Move spaceship
- Space — Shoot
- On-screen buttons — Mouse controls

**Mobile**
- `<` / `>` — Move spaceship
- FIRE — Shoot

Note: Simultaneous movement and shooting using two fingers is not fully supported in this version.

## Technologies

- Python
- Pygame
- Pygbag
- WebAssembly

## Run Locally

Install dependencies:

```bash
pip install pygame pygbag
```

Run the desktop version:

```bash
python main.py
```

Run the browser version:

```bash
python -m pygbag .
```

## About

This is a Python learning project focused on game development, event handling, object-oriented programming, and adapting a desktop Pygame application for web browsers.
