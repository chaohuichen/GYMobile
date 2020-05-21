import pickle as pk


users = [
    {
      "ID": 1,
      "FirstName": 'Joe', 
      "LastName": 'Smith', 
      "Email": "Joe@gymobile.com",
      "BMI": 2.2,
      "Rating": 4.5,
      "Comment": "None"
    }, 
    {
      "ID": 2,
      "FirstName": 'Mary', 
      "LastName": 'Smith', 
      "Email": "Mary@gymobile.com",
      "BMI": 2.3,
      "Rating": 4.8,
      "Comment": "None"
    }
  ]

with open('data.pkl', 'wb') as load:
    pk.dump(users,load)
