# Author: Shane Cheek
# Date: Feb 6th 2019

# input
startBalance = float(input('Starting Bank Balance'))
monthlyDeposit = float(input('Give a Monthly Deposit'))
monthlyWithdrawal = float(input('Give a Monthly Withdrawal'))

# calc

endBal = startBalance
endBal += monthlyDeposit
endBal -= monthlyWithdrawal

# output
print('Ending balance is', endBal)
