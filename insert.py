a = ['Master', 'Online'] 
a.insert(1,'code')
print(a)

c = [4, 5, 6]
d = [1, 2, 3]
c.insert(0, d)
print(c)

company = ['Roger', 'Quebec', 'Manfred']
company.sort()
print(company)

company = ['Roger', 'Quebec', 'Manfred']
company.sort(reverse=True)
print(company)

company = ['Roger', 'Quebec', 'Manfred']
company.sort(reverse=True, key=len)
print(company)