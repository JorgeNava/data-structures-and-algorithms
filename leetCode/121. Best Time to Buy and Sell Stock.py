"""
  You are given an array prices where prices[i] is the price of a given stock on the ith day.
  You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
  Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

  Example 1:
  Input: prices = [7,1,5,3,6,4]
  Output: 5
  Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
  Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

  Example 2:
  Input: prices = [7,6,4,3,1]
  Output: 0
  Explanation: In this case, no transactions are done and the max profit = 0.
"""
def maxProfit(prices):
  """
    {
      5: [0,1]
      3: [3,4]
    }
    lowerPrice = [0]
    profitActual = 0
    higherPrice = 0
    Iterate through each price:
    If actPrice <= lowestPrice:
        Registrar profit hasta aqui
          profits.append(profitActual)
        Comenzar a calcular un nuevo profit
          profitActual = 0
        lowerPrice = actPrice
      elif actPrice > higherPrice:
        higherPrice = actPrice
        Actualizamos profit actual
          profitActual = higherPrice - lowerPrice
      else:
        COMO MANEJAR DONDE SON EL MISMO PRECIO EN AMBOS CASOS?
  [7,1,5,3,6,4]
  """
  profits = []
  lowestPrice = prices[0]
  higherPrice = 0
  actualProfit = 0
  for actPrice in prices:
    if actPrice <= lowestPrice:
      profits.append(actualProfit)
      lowestPrice = actPrice
    elif actPrice > higherPrice:
      higherPrice = actPrice
      actualProfit = higherPrice - lowestPrice
  print('profits', profits)



tests = [
    {
      "prices": [7,1,5,3,6,4],
      "expectedOutput": 5
    },
]

for test in tests:
  output = maxProfit(test["prices"])
  print('output',output)
  print('>', output == test["expectedOutput"])

"""     {
          "prices": [7,6,4,3,1],
          "expectedOutput": 0
        },
        {
          "prices": [1,2],
          "expectedOutput": 1
        },
        {
          "prices": [2,4,1],
          "expectedOutput": 2
        }, 
"""