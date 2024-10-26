import os
import pandas as pd


read = "/home/prasanjith/Desktop/Atr/Atr/NSE_BANKNIFTY, 1D.csv"
read1 = "/home/prasanjith/Desktop/Atr/Atr/NSE_NIFTY, 1D (1).csv"
read4 = "/home/prasanjith/Desktop/Atr/Atr/NSE_NIFTYJR, 1D.csv"

read2 = pd.read_csv(read)
read3 =pd.read_csv(read1)
read5 = pd.read_csv(read4)


read2.to_json("NSE_BANKNIFTY-1D", orient='records')
read3.to_json("NSE_NIFTY-1D",orient="records")
read5.to_json("NSE_NIFTYJR",orient="records")