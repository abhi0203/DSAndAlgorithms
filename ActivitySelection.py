'''
In this problem we have been given a list of activities that can be performed and its start and end time. We need to maxiumize the number of activties that we can do.

- To achieve this, we need to use the greedy algorithgm.
- The basic of greedy algorithm is we find and fix something and then move on to next best thing. Then finally cumulatively we get the best solution.

activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
                ]

Activities comes as a multi dimnesional array
- Also, there cannot be an overlap of the activities.
- What we can do is, we can sort this activtiy by the end timings in the ascending order.
- So the one that ends sooner allows us to start the next activty. 
- Finally we compare the beginning time of next activty with the ending time of previous activty.
- If the beginning time > current time, we add it to the list and so on.
- Else we move to the next activity.
- Finally we print the list of the activities.
'''

def activitySelection(activities):
    activities.sort(key= lambda x:x[2])
    #Now we have the sorted actvities in descending order.
    #Next what we want to do is, first activtiy will be in the list as we will do it bare minimum
    activity=[]
    activity.append(activities[0])
    #Start with the second item in the list.
    #Compare the starting time of second item with end time of first item
    #If the match, append the array
    #Else move to the next item.
    for i in range(1,len(activities)):
        if activity[-1][2]< activities[i][1]:
            #This means we can add this activity to the list
            activity.append(activities[i])
    
    for i in range(len(activity)):
        print(activity[i][0])


activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
                ]

activitySelection(activities)
