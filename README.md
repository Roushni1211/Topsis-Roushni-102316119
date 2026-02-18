# Topsis-Roushni-102316119

## What is TOPSIS?

TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) is a multi-criteria decision-making method used to rank alternatives based on their distance from ideal best and ideal worst solutions.

## Installation

Install the package using:

pip install Topsis-Roushni-102316119

## Usage

After installation, run the following command:

topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>

Example:

topsis data.csv "1,1,1,2" "+,+,-,+" output.csv

## Input Requirements

- Input file must contain at least three columns.
- First column must contain alternatives.
- Remaining columns must contain numeric values.
- Number of weights must equal number of impacts.
- Impacts must be either '+' or '-'.
- Weights and impacts must be separated by commas.

## Output

The output file will contain:
- Original data
- Topsis Score
- Rank
