# Sleep Cycle Calculator 🌙

[![Python Version](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)

A smart tool to calculate optimal wake-up times based on sleep cycles, helping you wake up feeling refreshed!

## Overview
This Python script calculates recommended wake-up times by considering:
- 90-minute sleep cycles
- 15-minute pre-sleep relaxation period
- Flexible input options for bedtime
- Multiple wake-up alternatives

## Features
✅ **Intelligent Time Handling**  
Automatically detects if entered time is in the past and defaults to current time

✅ **Flexible Input**  
Accepts either:  
- Specific time in HH:MM format (24-hour clock)  
- 'n' for immediate calculation using current time

✅ **Cycle Options**  
Shows three wake-up alternatives:  
- Primary recommendation (selected cycles)  
- Earlier option (-1 cycle when possible)  
- Later option (+1 cycle)

✅ **User-Friendly Output**  
Clear, formatted results with cycle counts and time comparisons

## How to Use
1. **Run the script**
```bash
python sleep_calculator.py