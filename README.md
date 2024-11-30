# IP Analysis and Visualization

This repository contains scripts and tools for analyzing and visualizing IP address data. It leverages data processing, bootstrap sampling, and Plotly-based 4D visualizations to identify patterns, filter trusted and excluded IPs, and visualize usage trends per account and per IP.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
   - [Data Processing](#data-processing)
   - [4D Visualizations](#4d-visualizations)
6. [Files Description](#files-description)
7. [Contributing](#contributing)
8. [License](#license)

## Overview

The repository analyzes IP address data and visualizes trends to determine trusted and excluded IPs. Key components include:
- Data filtering based on confidence intervals calculated via bootstrap sampling.
- 4D scatter plots for combined, excluded, and trusted IPs for accounts and IPs.

## Features

- **Bootstrap Sampling**: Calculates confidence intervals for IP metrics like usage and user numbers.
- **Filtering**: Identifies trusted and excluded IPs based on thresholds.
- **4D Visualizations**: Uses Plotly for detailed 3D plots with a fourth dimension represented by color or intensity.
- **Output Files**: Generates filtered datasets and visualization HTML files.

## Requirements

- Python 3.7+
- Libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `scipy`
  - `plotly`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ip-analysis.git
   cd ip-analysis
   ```
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Data Processing

Run `per acct per ip.py`:

```bash
python per\ acct\ per\ ip.py
```

This script processes account-level IP data and generates trusted and excluded datasets.

Run `per ip.py`:

```bash
python per\ ip.py
```

This script processes IP-level data and creates filtered datasets with visualizations.

### 4D Visualizations

Open the HTML files in a browser to view scatter plots:

#### For account-based visualizations:
- `per_acct_4DPlot_combined.html`
- `per_acct_4DPlot_trusted.html`
- `per_acct_4DPlot_excluded.html`

#### For IP-based visualizations:
- `per_ip_4DPlot_combined.html`
- `per_ip_4DPlot_trusted.html`
- `per_ip_4DPlot_excluded.html`

---

## Files Description

### Python Scripts

#### `per acct per ip.py`:
- Processes daily user and IP usage data for accounts.
- Filters and outputs trusted and excluded IPs for accounts.

#### `per ip.py`:
- Processes daily user and IP usage data for IPs.
- Filters and outputs trusted and excluded IPs for standalone IPs.

#### `per ip 4D visualization.py`:
- Generates 4D scatter plots for combined, trusted, and excluded IPs.

#### `tempCodeRunnerFile.py`:
- Temporary testing script with snippets for debugging.

---

### Data Files

#### Raw Data:
- `per acct per ip daily user num.csv`
- `per acct per ip daily ip usage.csv`
- `per ip daily user num.csv`
- `per ip daily ip usage.csv`

#### Filtered Data:
- `per acct per ip filtered and excluded.csv`
- `per acct per ip filtered.csv`
- `per ip filtered and excluded.csv`
- `per ip filtered.csv`

---

### HTML Files

#### Account-Level Visualizations:
- `per_acct_4DPlot_combined.html`: Combined IP data.
- `per_acct_4DPlot_trusted.html`: Trusted IP data.
- `per_acct_4DPlot_excluded.html`: Excluded IP data.

#### IP-Level Visualizations:
- `per_ip_4DPlot_combined.html`: Combined IP data.
- `per_ip_4DPlot_trusted.html`: Trusted IP data.
- `per_ip_4DPlot_excluded.html`: Excluded IP data.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
