{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e5b9bf1-1d39-4150-8efd-bf7d6da70016",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd9791a9-30e5-4f70-b9ff-8a531c44f38b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sample data\n",
    "categories = ['A', 'B', 'C', 'D']\n",
    "values1 = [4, 3, 2, 5]\n",
    "values2 = [2, 5, 3, 1]\n",
    "values3 = [3, 2, 4, 2]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "30f48076-a5e8-4726-b707-9d1b3cebfeed",
   "metadata": {},
   "source": [
    "**Basic Bar Chart**: A simple bar chart with one dataset, using  <span style=\"color:orange;\">plt.bar()</span>. It includes a grid and basic labels."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a805be8-0e63-471c-a12d-13951a8fed96",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Basic Bar Chart\n",
    "plt.figure(figsize=(8, 5))\n",
    "plt.bar(categories, values1, color='skyblue')\n",
    "plt.title('Basic Bar Chart')\n",
    "plt.xlabel('Categories')\n",
    "plt.ylabel('Values')\n",
    "plt.grid(True, axis='y', linestyle='--', alpha=0.7)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9629815f-017f-4524-b7e4-fe6b6815a0b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# If you want to download the chart\n",
    "plt.savefig('basic_bar.png')\n",
    "plt.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ca99c59-4473-4055-952f-af5c7d7f1492",
   "metadata": {},
   "source": [
    "**Grouped Bar Chart**: Displays multiple datasets side-by-side using offset positions ( <span style=\"color:orange;\">x - width, x, x + width</span>). Each group has a different color and a legend."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f07270b-f835-48b6-9a82-11981238de85",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Grouped Bar Chart\n",
    "x = np.arange(len(categories))\n",
    "width = 0.25\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.bar(x - width, values1, width, label='Group 1', color='salmon')\n",
    "plt.bar(x, values2, width, label='Group 2', color='lightgreen')\n",
    "plt.bar(x + width, values3, width, label='Group 3', color='skyblue')\n",
    "plt.xlabel('Categories')\n",
    "plt.ylabel('Values')\n",
    "plt.title('Grouped Bar Chart')\n",
    "plt.xticks(x, categories)\n",
    "plt.legend()\n",
    "plt.grid(True, axis='y', linestyle='--', alpha=0.7)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "65f07eae-2fc3-4f28-833a-fd9b8af47402",
   "metadata": {},
   "source": [
    "**Stacked Bar Chart**: Stacks datasets on top of each other using the  <span style=\"color:orange;\">bottom</span> parameter to specify the starting height of each bar."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "099f84dc-bfa6-4815-853c-44f8e5e5c846",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3. Stacked Bar Chart\n",
    "plt.figure(figsize=(8, 5))\n",
    "plt.bar(categories, values1, label='Group 1', color='salmon')\n",
    "plt.bar(categories, values2, bottom=values1, label='Group 2', color='lightgreen')\n",
    "plt.bar(categories, values3, bottom=np.array(values1) + np.array(values2), label='Group 3', color='skyblue')\n",
    "plt.title('Stacked Bar Chart')\n",
    "plt.xlabel('Categories')\n",
    "plt.ylabel('Values')\n",
    "plt.legend()\n",
    "plt.grid(True, axis='y', linestyle='--', alpha=0.7)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1cce287b-f1e1-4bda-98f9-42fc6474d6c0",
   "metadata": {},
   "source": [
    "**Horizontal Bar Chart**: Uses  <span style=\"color:orange;\">plt.barh()</span> for horizontal bars, useful when category names are long or for a different visual perspective."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48f5b80d-665a-420f-9b3e-1f520b0427d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4. Horizontal Bar Chart\n",
    "plt.figure(figsize=(8, 5))\n",
    "plt.barh(categories, values1, color='purple')\n",
    "plt.title('Horizontal Bar Chart')\n",
    "plt.xlabel('Values')\n",
    "plt.ylabel('Categories')\n",
    "plt.grid(True, axis='x', linestyle='--', alpha=0.7)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "97521cf3-303d-46fb-a774-2e65e08b15b5",
   "metadata": {},
   "source": [
    "**Customized Bar Chart with Error Bars**: Adds error bars ( <span style=\"color:orange;\">yerr</span>) to show variability and includes value labels on top of each bar for clarity."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "021b9f2d-2ae9-46dd-b4a4-f59c369e1afb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Customized Bar Chart with Error Bars\n",
    "errors = [0.5, 0.3, 0.4, 0.2]\n",
    "plt.figure(figsize=(8, 5))\n",
    "bars = plt.bar(categories, values1, color='teal', edgecolor='black', alpha=0.7, yerr=errors, capsize=5)\n",
    "plt.title('Customized Bar Chart with Error Bars')\n",
    "plt.xlabel('Categories')\n",
    "plt.ylabel('Values')\n",
    "plt.grid(True, axis='y', linestyle='--', alpha=0.7)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d9e2fc4-8689-44ee-904f-c9a8504c40ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add value labels on top of bars\n",
    "for bar in bars:\n",
    "    yval = bar.get_height()\n",
    "    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, yval, ha='center', va='bottom')\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
