correctMachineNumber = 3
correctTaskNumber = 9
taskProcessingTimes = [12,7,3,22,24,13,15,9,10]
machineSpeeds = [1,2,5]

def calcMachineCompletionTime(machineNumber, tasks) :
	#get task process time for each task
	processingTimes = []
	for taskNumber in tasks:
		processingTimes.append(taskProcessingTimes[taskNumber-1])
	#sum processingTimes list
	sumProcessingTimes = float(sum(processingTimes))
	#get machine speed
	completionTime = float(sumProcessingTimes/(float(machineSpeeds[machineNumber-1])))
	return float(completionTime)
	
def validateNumberOfTasks(countedTasks):
	if(countedTasks == correctTaskNumber):
		print "Congratulations, you assigned all of the tasks to a machine! Tasks counted: %d" % countedTasks
		return True
	else:
		print "Oh no! You did not assign each task to a machine. You had %d tasks instead of the correct number, %d" % (countedTasks, correctTaskNumber)
		return False
	
def validateCompletionTime(calculatedCompletionTime, givenCompletionTime):
	if(round(calculatedCompletionTime,2) == round(givenCompletionTime,2)):
		print "Congratulations, you calculated the completion time correctly! Completion time: %.2f" % calculatedCompletionTime
		return True
	else: 
		print "Oh no! You did not calculate the completion time correctly. You had %.2f instead of the correct number, %.2f" % (givenCompletionTime, calculatedCompletionTime)
		return False

def processFile() :
		maxCompletionTime = 0
		checkTaskNumbers = 0
		solutionFile = "testInputs.txt"
		listOfAssignedTasks = []
		tempList = []
		with open(solutionFile) as f:
			tempList = f.readlines()
		listOfAssignedTasks = [x.strip('\n') for x in tempList]
		tempListOfAssignedTasks = [x for x in listOfAssignedTasks if x.strip()]
		fileCompletionTime = float(tempListOfAssignedTasks[-1])
		unusedMachines = []
		for machineNumber in range(0, len(listOfAssignedTasks)):
			if(not listOfAssignedTasks[machineNumber]):
				unusedMachines.append(machineNumber+1)
		newlistOfAssignedTasks = [x for x in listOfAssignedTasks if x]
		newlistOfAssignedTasks.pop()
		numberOfTasks = 0
		numberOfMachines = 0
		for tasks in newlistOfAssignedTasks:
			numberOfMachines = numberOfMachines + 1
			while((numberOfMachines in unusedMachines)):
				numberOfMachines = numberOfMachines + 1
			if (tasks):
				tempTaskList = tasks.split(' ')
				tempTaskList = [x for x in tempTaskList if x.strip()]
				tempTaskList = [int(x) for x in tempTaskList]
				numberOfTasks = numberOfTasks + len(tempTaskList)
				tempCompletionTime = float(calcMachineCompletionTime(numberOfMachines, tempTaskList))
				if(tempCompletionTime > maxCompletionTime):
					maxCompletionTime = tempCompletionTime
				print "Temp completion time for machine %d : %f " % (numberOfMachines, tempCompletionTime)
		if(validateNumberOfTasks(numberOfTasks) and validateCompletionTime(maxCompletionTime, fileCompletionTime)):
			print "Success! You have been validated!"
		else:
			print "Fail! You have not been validated!"
		
		

processFile()
		
	

	
	



