{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from IPython.display import display\n",
    "\n",
    "\n",
    "# Create table for missing data analysis\n",
    "def draw_missing_data_table(df):\n",
    "    total = df.isnull().sum().sort_values(ascending=False)\n",
    "    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)\n",
    "    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])\n",
    "    display(missing_data)\n",
    "\n",
    "def cut_levels(x, threshold, new_value):\n",
    "    value_counts = x.value_counts()\n",
    "    labels = value_counts.index[value_counts < threshold]\n",
    "    x[np.in1d(x, labels)] = new_value\n",
    "    return labels\n",
    "\n",
    "def cut_levels_new(x, threshold, new_value):\n",
    "    x = x.copy()\n",
    "    value_counts = x.value_counts()\n",
    "    labels = value_counts.index[value_counts < threshold]\n",
    "    x[np.in1d(x, labels)] = new_value\n",
    "    return x, labels\n",
    "\n",
    "def find_outliers(Data, col)\n",
    "    data_mean, data_std = np.mean(Data[col]), np.std(Data[col])\n",
    "    cut_off = data_std * 4\n",
    "    lower, upper = data_mean - cut_off, data_mean + cut_off\n",
    "    return Data.loc[(Data[col]<lower) | (Data[col]>upper), col ] #.index\n",
    "\n",
    "def basic_eda(df):\n",
    "    print(\"----------HEAD--------\")\n",
    "    display(df.head(5));\n",
    "    print(\"----------INFO-----------------\")\n",
    "    display(df.info() )\n",
    "    print(\"----------Describe-------------\")\n",
    "    display(df.describe())\n",
    "    print(\"----------Columns--------------\")\n",
    "    display(df.columns)\n",
    "    print(\"----------Data Types-----------\")\n",
    "    display(df.dtypes)\n",
    "    print(\"-------Missing Values----------\")\n",
    "    display(df.isnull().sum().loc[lambda x: x>0])\n",
    "    print(\"-------NULL values-------------\")\n",
    "    display(df.isna().sum().loc[lambda x: x>0])\n",
    "    print(\"-----Shape Of Data-------------\")\n",
    "    display(df.shape)\n",
    "    print(\"-----Sample-------------\")\n",
    "    display(df.sample(5))\n",
    "    print(\"******  Counts  ******* \\n\")\n",
    "    for c in df.columns[:(min(df.columns.shape[0],10))]:\n",
    "        print(\"---- %s ---\" % c)\n",
    "        display(df[c].value_counts().to_frame())\n",
    "#     display(df.apply(lambda x: x.value_counts() , axis = 0).T.stack().to_frame() )\n",
    "\n",
    "def Look_Date(data):\n",
    "    print(\"The data starts from the date {} and ends in {}\".format(data.min().date(),data.max().date()))\n",
    "    print(\"So we have {} of data\".format(data.max().date()-data.min().date()))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.3"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": "6",
    "lenType": "6",
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
