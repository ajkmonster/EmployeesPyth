employees = [{'id':'001', 'name':'Mary', 'payRate': 15.00, 'hoursWorked':40},
{'id': '002','name':'John','payRate':22.00,'hoursWorked':25},
{'id':'003','name': 'Bob','payRate':35.00,'hoursWorked':4},
{'id':'004','name':'Mel','payRate':43.00,'hoursWorked':62},
{'id':'005','name':'Jen','payRate':17.00,'hoursWorked':33},
{'id':'006','name':'Sue','payRate':29.00,'hoursWorked':45},
{'id':'007','name':'Ken','payRate':40.00,'hoursWorked':36},
{'id':'008','name':'Dave','payRate':20.00,'hoursWorked':17},
{'id':'009','name':'Beth','payRate':37.00,'hoursWorked':37},
{'id':'010','name':'Ray','payRate':16.50,'hoursWorked':80}]
for  x in employees:
    if x['hoursWorked'] > 40:
        otRate= x['payRate']*1.5
        otHours = x['hoursWorked'] - 40
        hoursWorked = 40
        print(x['name'],' Normal pay: ', x['payRate']*hoursWorked,
              '\nExtra pay: ', otRate*otHours,
              '\nSalary: ',(x['payRate']*hoursWorked + otRate*otHours))
    else:
        salary = x['payRate'] * x['hoursWorked']
        print(x['name'],' Salary: ', salary) 
