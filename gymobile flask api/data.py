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

exercises = [
    userid: 1,
    exercises:{
      {
        "Exercise_id": 1,
        "Name": "push up", 
        "BodyPart": "", 
        "Category": "",
        "Description": "None"
      }, 
      {
        "Exercise_id": 2,
        "Name": "set up", 
        "BodyPart": "", 
        "Category": "",
        "Description": "None"
      },
    }
    
    user_id : 2,
    exercise : {
      {
        "Exercise_id": 1,
        "Name": "swimming", 
        "BodyPart": "full", 
        "Category": "",
        "Description": "None"
      },
      {
        "Exercise_id": 2,
        "Name": "running", 
        "BodyPart": "lower", 
        "Category": "",
        "Description": "None"
      }
    }
  ]

with open('data.pkl', 'wb') as user_load:
    pk.dump(users,user_load)

with open('exercise.pkl', 'wb') as exe_load:
    pk.dump(exercises, exe_load)
