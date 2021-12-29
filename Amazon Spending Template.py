{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f81bcdf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('') #insert file path name between single quotes\n",
    "df.head() #first five rows of data\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8191b0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.shape #number rows and columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0267dc8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.fillna(0) #overwriting df with new df that fills all NaN values with 0\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3509c567",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.dtypes #check data type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e6aa93d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"Total Charged\"] = df[\"Total Charged\"].str.replace(' ','') #get rid of spaces\n",
    "df[\"Total Charged\"] = df[\"Total Charged\"].str.replace(',','') #get rid of commas\n",
    "df[\"Total Charged\"] = df[\"Total Charged\"].str.replace('$','').astype(float)\n",
    "#replace $ with nothing, then change data type from object to float and overwrite column in df\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2277bd2",
   "metadata": {},
   "outputs": [],
   "source": [
    "total_purchase_sum=df[\"Total Charged\"].sum() #find the total sum of total charged\n",
    "print(total_purchase_sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf2951df",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"Total Charged\"].mean() #average cost of each purchase"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8312e284",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"Total Charged\"].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "641f64ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"Total Charged\"].max() #largest purchase"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ea8488d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"Total Charged\"].min() #smallest purchase"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "507f88a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"Tax Charged\"] = df[\"Tax Charged\"].str.replace('$','').astype(float)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f45da9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "total_tax_sum=df[\"Tax Charged\"].sum() #amount of sales tax paid\n",
    "print(total_tax_sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "06a2047c",
   "metadata": {},
   "outputs": [],
   "source": [
    "round((total_tax_sum/total_purchase_sum*100),2) #average of how much sales tax charged"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2db0d917",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Order Date'] = pd.to_datetime(df['Order Date']).dt.date  #convert date to datetime\n",
    "\n",
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0852b6c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "996fe9bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.plot.bar(x='Order Date',y='Total Charged',rot=90, figsize=(20,10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b05bd2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "daily_orders = df.groupby('Order Date').sum()[\"Total Charged\"]\n",
    "daily_orders.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91abbd83",
   "metadata": {},
   "outputs": [],
   "source": [
    "daily_orders.plot.bar(figsize=(20,10),color=('#61D198')) #group by order dates"
   ]
  }
 ],
 "metadata": {
  "celltoolbar": "Raw Cell Format",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
