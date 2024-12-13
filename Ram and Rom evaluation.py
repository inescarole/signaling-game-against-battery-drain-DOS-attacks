import time
import sys
import matplotlib.pyplot as plt
import numpy as np

# Define Parameters
attackCost = 250  # y
successBenefit = 350  # x
lowEnergyCost = 45  # alpha
highEnergyCost = 100  # beta

# Define Prior Belief Range
priorBeliefs = np.arange(0, 1.1, 0.1)  # q from 0 to 1 with step of 0.1
ramUsage = []  # RAM usage tracker
romUsage = 0  # ROM usage tracker (static)

# Calculate Static ROM Usage
romVariables = {
    'attackCost': attackCost,
    'successBenefit': successBenefit,
    'lowEnergyCost': lowEnergyCost,
    'highEnergyCost': highEnergyCost
}
romUsage = sum(sys.getsizeof(value) for value in romVariables.values()) / 1024  # Convert to KB

# Simulation Start
print("Simulating Nash Equilibrium Algorithm...")

for q in priorBeliefs:
    # Calculate Prior Beliefs (Updated Bayesian Values)
    mu = q  # μ = (πh("H") * q) / (πh("H") * q + πℓ("H") * (1 − q))
    omega = 0  # ω = (πh("L") * q) / ((1 − q) * πℓ("L") + πh("L") * q)

    # Attacker's Expected Utility
    EU2_A_mu = -mu * attackCost + (1 - mu) * (successBenefit - attackCost)
    EU2_NA_mu = 0
    EU2_A_w = -omega * attackCost + (1 - omega) * (successBenefit - attackCost)
    EU2_NA_w = 0

    # Defender's Expected Utility for High and Low Signals (AA and NAA)
    EU_h1_H_AA = 0
    EU_h1_L_AA = -lowEnergyCost
    EU_h1_H_NAA = 0
    EU_h1_L_NAA = -lowEnergyCost

    EU_l1_H_NAA = -highEnergyCost
    EU_l1_L_NAA = -successBenefit

    # Defender's Expected Utility for "NANA"
    EU_h1_H_NANA = 0
    EU_h1_L_NANA = -lowEnergyCost
    EU_l1_H_NANA = -highEnergyCost
    EU_l1_L_NANA = 0

    # Perform Comparisons
    comparisonResults = {
        "Compare EU2_A_mu vs EU2_NA_mu": EU2_A_mu > EU2_NA_mu,
        "Compare EU2_A_w vs EU2_NA_w": EU2_A_w > EU2_NA_w,
        "Compare EU_h1_H_AA vs EU_h1_L_AA": EU_h1_H_AA > EU_h1_L_AA,
        "Compare EU_h1_H_NAA vs EU_h1_L_NAA": EU_h1_H_NAA > EU_h1_L_NAA,
        "Compare EU_l1_H_NAA vs EU_l1_L_NAA": EU_l1_H_NAA > EU_l1_L_NAA,
        "Compare EU_h1_H_NANA vs EU_h1_L_NANA": EU_h1_H_NANA > EU_h1_L_NANA,
        "Compare EU_l1_H_NANA vs EU_l1_L_NANA": EU_l1_H_NANA > EU_l1_L_NANA,
        "Best EU in NANA Set": max(EU_h1_H_NANA, EU_h1_L_NANA, EU_l1_H_NANA, EU_l1_L_NANA)
    }

    # Determine Attacker's Best Response
    attackerBestResponse = "Attack" if comparisonResults["Compare EU2_A_mu vs EU2_NA_mu"] else "Not Attack"

    # Track RAM Usage
    currentVars = {
        'mu': mu, 'omega': omega,
        'EU2_A_mu': EU2_A_mu, 'EU2_NA_mu': EU2_NA_mu,
        'EU2_A_w': EU2_A_w, 'EU2_NA_w': EU2_NA_w,
        'EU_h1_H_AA': EU_h1_H_AA, 'EU_h1_L_AA': EU_h1_L_AA,
        'EU_h1_H_NAA': EU_h1_H_NAA, 'EU_h1_L_NAA': EU_h1_L_NAA,
        'EU_l1_H_NAA': EU_l1_H_NAA, 'EU_l1_L_NAA': EU_l1_L_NAA,
        'EU_h1_H_NANA': EU_h1_H_NANA, 'EU_h1_L_NANA': EU_h1_L_NANA,
        'EU_l1_H_NANA': EU_l1_H_NANA, 'EU_l1_L_NANA': EU_l1_L_NANA,
        'attackerBestResponse': attackerBestResponse, 'priorBelief': q
    }
    ramUsage.append(sum(sys.getsizeof(value) for value in currentVars.values()) / 1024)  # Convert to KB

    # Print Comparisons
    print(f"Prior Belief (q={q:.1f}):")
    for key, value in comparisonResults.items():
        print(f"  {key}: {value}")
    print(f"  Attacker's Best Response: {attackerBestResponse}\n")

    # Simulate Processing Delay
    time.sleep(0.2)

# Plot RAM Usage
plt.figure(figsize=(10, 6))
plt.plot(priorBeliefs, ramUsage, marker='o', color='b', linewidth=2)
plt.xlabel('Prior Belief (q)')
plt.ylabel('RAM Usage (KB)')
plt.title('RAM Usage vs Prior Belief in Nash Equilibrium Evaluation')
plt.grid(True)
plt.show()

# Print Static ROM Usage
print(f'Total Static ROM Usage: {romUsage:.2f} KB')
