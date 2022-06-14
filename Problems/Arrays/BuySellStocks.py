"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

def buy_sell_stock(arr):
    
    minim=arr[0]
    index_min=0
    for i in range(len(arr)):
        if arr[i]<minim:
            minim=arr[i]
            index_minim=i 

    index_max=index_min
    maxim=minim
 
    for j in range(index_minim, len(arr)):
        if arr[j]>maxim:
            maxim=arr[j]
            index_max=j
 

    if index_max>index_min:
        return maxim-minim
    else:
        return 0
