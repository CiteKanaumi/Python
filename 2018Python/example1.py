WL = ['70.11%', '60.00%']

for A in WL :
    A = A.split('%')
    A = A[0]
    if float(A) >= 65 :
            A = '<font color="#FF00FF">'+A+'%</font>'
    else :
        A = A+'%'
    print(A)
