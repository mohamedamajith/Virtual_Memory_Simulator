Virtual Memory Simulator Mini Project

A simple virtual memory simulation tool built using Python and Tkinter. This project demonstrates how an operating system performs paging, 
detects page faults, manages frames, and translates logical addresses into physical addresses. 

📘 Project Overview

This project provides a visual, beginner-friendly simulation of virtual memory management.
It models:
⦁	  Logical memory with 8 pages (1 KB each)
⦁	  Physical memory with 4 frames (1 KB each)
⦁	  Single-level page table
⦁	  Page faults and page loading
⦁	  Logical-to-physical address translation
⦁	  GUI-based visualization of memory states

This tool is ideal for learning the fundamentals of operating system memory management.

🚀 Features

⦁	  GUI-Based Interface using Python Tkinter
⦁	  Live Page Table and Frame Table Visuals
⦁	  Color-coded Indicators for loaded/unloaded pages and used/free frames
⦁	  Page Fault Detection and automatic page loading
⦁	  Displays Physical Address Calculation
⦁	  Reset Simulation option
⦁	  Error Handling for invalid or out-of-range addresses

🧠 System Architecture

The project follows a simple, modular structure inspired by MVC:
⦁	  Model: VirtualMemorySimulator class
⦁	  View: Tkinter GUI (tables, input fields, log area)
⦁	  Controller: Event handler methods inside ui.py

📂 Code Structure

  Virtual_Memory_Simulator/
  |-- 
  main.py
  |-- 
  simulator.py 
  |-- 
  ui.py
  |-- 
  README.md


⚙️ How It Works
1. Logical Address Processing

  Logical address (0–8191) is split into:
  Page number = address // 1024
  Offset = address % 1024

2. Page Table Lookup

  If page is loaded → retrieve frame
  If not → page fault

3. Page Fault Handling

  Find first free frame
  Load page into frame
  Update page table and frame table

4. Physical Address Calculation
  Physical Address = (Frame Number * 1024) + Offset

5. Visualization

  Page/Frame tables refresh dynamically
  Page faults highlighted in the log

🖥️ Installation & Setup
Requirements

⦁	Python 3.x
⦁	Tkinter (included with most Python installations)
⦁	VS Code or any Python IDE

Run the Program
python main.py

👤 Author
Developed by: MJM.AMAJITH (721434768)
Course: EEX5563/EEX5564 – Computer Architecture & Operating Systems
Institute: The Open University of Sri Lanka
