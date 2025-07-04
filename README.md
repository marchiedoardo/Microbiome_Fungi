# Microbiome_Fungi

Codes and Data to reproduce the results of "Fungal Communities as Indicators of Soil Health: Land-Use and Climate Effects in Mediterranean and Semi-Arid Agroecosystems” by Y. Steinberg et al. (submitted)

The repository contains:
- `SoilHealth-Fungi_mod.xlsx` -> complete raw dataset
- `pca_rda.ipynb` -> jupyter notebook (in R) that performs PCA and RDA analysis on the phyla abundances
- `pictures_for_paper.ipynb` -> jupyter notebook (in python) to reproduce all the relevant pictures and tables to include in the manuscript
- `network_analysis.ipynb` -> jupyter notebook that perform network analysis of genera communities based on correlation between genera
- `funguild.ipynb` -> jupyter notebook that used the FUNguild database to classify the genera in our dataset into functional fungal guilds.

---

## 📦 Dependencies and Module Versions

The code was written and tested in **Python 3.11.9** and **R 4.4.2**. The following libraries were used:

### Python packages:
- `pandas` 1.5.3  
- `numpy` 1.26.4
- `scipy` 1.13.1
- `statsmodels` 0.14.3
- `ipywidgets` 8.1.5 
- `matplotlib` 3.7.3  
- `seaborn` 0.11.2  
- `networkx` 3.4.2  
- `statannotations` 0.6.0  
- `bio` 1.7.1

### R packages:
- `vegan` 2.7.0  
- `ggplot2` 3.5.1 
- `readxl` 1.4.3  

## Running jupyter notebooks with R kernel

To run notebooks that use the R kernel, you need to have R installed.

- **On Windows or macOS**:  
  Download and install R from the official CRAN website:  
  👉 https://cran.r-project.org/

- **On Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt update
  sudo apt install r-base

Then, install the IRkernel (the Jupyter R kernel):
In R or RStudio:

```
install.packages("IRkernel")
IRkernel::installspec()  # registers the R kernel with Jupyter
```

Finally, the notebook can be opened in Jupyter Notebook or Jupyter Lab and run after selecting the R kernel (that should be now available).
