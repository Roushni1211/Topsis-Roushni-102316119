# TOPSIS Implementation in Python  
### Topsis-Roushni-102316119

---

## 📌 Overview

This project implements **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** — a multi-criteria decision-making (MCDM) method used to rank alternatives based on their distance from the ideal best and ideal worst solutions.

The project includes:

- ✔ Command Line Interface (CLI)
- ✔ Complete input validation & error handling
- ✔ Python package uploaded to PyPI
- ✔ Proper packaging using setuptools
- ✔ Public GitHub repository

---

## 🧠 Mathematical Steps of TOPSIS

1. Construct the decision matrix  
2. Normalize the matrix  
3. Multiply by weights  
4. Determine Ideal Best and Ideal Worst  
5. Calculate Euclidean distances  
6. Compute TOPSIS score  
7. Rank alternatives  

---

## 📦 Installation (From PyPI)

Install directly from PyPI:

```bash
pip install Topsis-Roushni-102316119
```

---

## 💻 Usage

After installation, run:

```bash
topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

### Example:

```bash
topsis data.csv "1,1,1,2" "+,+,-,+" output.csv
```

---

## 📄 Input Requirements

- Input file must contain at least **three columns**
- First column → Alternatives
- Remaining columns → Numeric values only
- Number of weights = number of impacts
- Impacts must be either `+` (benefit) or `-` (cost)
- Weights and impacts must be comma-separated

---

## 📊 Output

The output CSV file contains:

- Original data  
- TOPSIS Score  
- Rank (1 = Best)

---

## 🔒 Error Handling Implemented

The program checks for:

- Incorrect number of parameters  
- File not found  
- Insufficient columns  
- Non-numeric values  
- Mismatch in weights and impacts  
- Invalid impact symbols  

---

## 🚀 Live Package

🔗 PyPI Link:  
https://pypi.org/project/Topsis-Roushni-102316119/

---

## 👩‍💻 Author

**Roushni Sharma**  
B.Tech Student  
Thapar Institute of Engineering and Technology
