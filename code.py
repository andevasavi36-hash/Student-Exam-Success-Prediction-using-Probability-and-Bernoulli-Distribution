# Probability & Bernoulli Distribution Project
# =========================================

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Generate Student Data
# -------------------------------

# 1 = Pass
# 0 = Fail

np.random.seed(42)

# Assume pass probability = 0.7
p = 0.7

# Generate 100 student results
student_results = np.random.binomial(1, p, 100)

# Create DataFrame
students = pd.DataFrame({
    'Student_ID': range(1, 101),
    'Result': student_results
    })

print("First 10 Student Results:\n")
print(students.head(10))


# STEP 2: Probability Calculation
# -------------------------------

pass_probability = students['Result'].mean()
fail_probability = 1 - pass_probability

print("\nPass Probability:", pass_probability)
print("Fail Probability:", fail_probability)

# -------------------------------
# STEP 3: Bernoulli Distribution
# -------------------------------

print("\nBernoulli Distribution:")
print("P(X=1) =", pass_probability)
print("P(X=0) =", fail_probability)

# -------------------------------
# STEP 4: Mean, Variance, Mode
# -------------------------------

mean_value = np.mean(student_results)
variance_value = np.var(student_results)
mode_value = students['Result'].mode()[0]

print("\nMean:", mean_value)
print("Variance:", variance_value)
print("Mode:", mode_value)


# -------------------------------
# STEP 5: PMF Table
# -------------------------------

pmf = students['Result'].value_counts(normalize=True)

print("\nProbability Mass Function (PMF):")
print(pmf)


 #STEP 6: Visualization
# -------------------------------

counts = students['Result'].value_counts()

plt.figure(figsize=(6,4))
plt.bar(['Fail (0)', 'Pass (1)'], counts.sort_index())
plt.xlabel('Exam Result')
plt.ylabel('Number of Students')
plt.title('Bernoulli Distribution of Student Results')
plt.show()


# -------------------------------
# STEP 7: Interpretation
# -------------------------------

print("\nProject Interpretation:")

if pass_probability > 0.5:
    print("Most students are passing the exam.")
else:
    print("Most students are failing the exam.")

print("The data follows Bernoulli Distribution because only two outcomes exist.")


