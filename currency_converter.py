# made as part as a codedex python course 
print('Money exchange program')
co = int(input('How much co do you have?: '))
pe = int(input('How much pe do you have?: '))
br = int(input('How much br do you have?: '))
total_usd = (co * 0.00033) + (pe * 0.30) + (br * 0.19)
print(total_usd)
