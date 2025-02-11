# 🏆 Second-Price Auction: Modeling & Strategy  

## 📌 Overview
This project involves designing **bidding algorithms** for an **online ad auction**.  
The auction follows **a second-price sealed-bid format**, where multiple bidders compete for ad placement opportunities.  
The objective is to utilize classes to develop an **effective bidding strategy** that maximizes profits while competing against other algorithms.

## 🎯 Project Goals
- Implement a **bidding strategy** for an ad auction.
- Optimize bidding decisions using **exploration vs. exploitation** techniques.
- Compete against other bidding algorithms in a **class-wide competition**.
- Ensure **modular, well-structured, and PEP 8-compliant** Python code.

## 🔎 Auction Rules
- **Users & Click Probability:** Each user has a **fixed probability** (drawn from `U[0,1]`) of clicking an ad.
- **Bidding Process:** Bidders place **sealed** bids (not visible to competitors).
- **Winner Selection:** The highest bidder wins, but pays the **second-highest bid**.
- **Revenue & Costs:**
  - If the **user clicks** on the ad, the winning bidder gains **$1**.
  - The winning bidder **pays the second-highest bid**, regardless of whether the ad is clicked.
- **Elimination Condition:** If a bidder’s balance falls below **-1000**, they are disqualified.

## 🗂 Files & Notebooks##
| File | Description |
|------|------------|
| `auction_instructions.pdf` | Detailed assignment instructions and project guidelines. |
| `auction_rhoades.py` | Implementation of the auction mechanics, managing users and bidders. |
| `auction_run.ipynb` | Jupyter Notebook to run and analyze auction simulations. |
| `bidder_rhoades.py` | Bidding strategy implementation for optimizing auction performance. |



## 🚀 Implementation Details
### **🔹 User Class (`User`)**
- **`__init__(self)`** → Assigns a **random click probability** from `U[0,1]`.
- **`show_ad(self)`** → Determines whether the user **clicks** on the ad.

### **🔹 Bidder Class (`Bidder`)**
- **`__init__(self, num_users, num_rounds)`** → Initializes bidder memory for strategy.
- **`bid(self, user_id)`** → Returns a **non-negative bid** (rounded to 3 decimals).
- **`notify(self, auction_winner, price, clicked)`** → Updates strategy after each round.

### **🔹 Auction Class (`Auction`)**
- **`__init__(self, users, bidders)`** → Stores all **user and bidder objects**.
- **`execute_round(self)`** → Runs **one full round** of the auction.
- **`plot_history(self)`** → Generates **visualizations** of bidding patterns.

## 🏆 Performance & Results
Our bidding algorithm achieved a score of 104 out of a possible 105, demonstrating high efficiency and strategic optimization in the second-price auction.
This performance outscored most competing algorithms in the class competition, proving its effectiveness in maximizing profits while managing bidding risks.




