patient = input("Enter patient name:")
requestedDepartment = input("Enter requested departments:")
requestedDepartment = requestedDepartment.split(",")
requestedDepartment = [dep.strip() for dep in requestedDepartment]
availabledep = input("Enter available departments:")
availabledep = availabledep.split(",")
previouslyVisited = input("ENter previously visited departments:")
previouslyVisited = previouslyVisited.split(",")
prefDoc = input("Enter preferred doctors:")
prefDoc = prefDoc.split(",")
availDoc = input("Enter available doctor: ")
availDoc=availDoc.split(",")
emergency = input("Enter emergency department:")
emergency = emergency.split(",")
emergency = [dep.strip() for dep in emergency]

reqSet = set(requestedDepartment)
availSet = set(availabledep)
visitSet = set(previouslyVisited)
prefDocSet = set(prefDoc)
avaiDocSet = set(availDoc)
emergencySet = set(emergency)

commonDep = reqSet.intersection(availSet)
unavailDep = reqSet.difference(availSet)
visitDep = reqSet.intersection(visitSet)
commonDoc = prefDocSet.intersection(avaiDocSet)
emergencyDep = reqSet.intersection(emergencySet)
allDep = reqSet.union(availSet)

if "Cardiology" in reqSet:
    print("Cardiology is requested.")

if "Cardiology" in availSet:
    print("Cardiology Available.")

dupReq = []
for dep in requestedDepartment:
    if requestedDepartment.count(dep) > 1:
        if dep not in dupReq:
            dupReq.append(dep)

firstDep = requestedDepartment[0]

firstTwo = requestedDepartment[:2]

requestedDepartment.append("General medicine")

if "General medicine" in requestedDepartment:
    requestedDepartment.remove("General medicine")

if len(emergencyDep) > 0:
    recDep = list(emergency)[0]
    appStatus = "Emergency appointment required"
elif len(commonDep)>0:
    recDep=list(commonDep)[0]
    appStatus = "appointment can be scheduled"
else:
    recDep = "Not Available"
    appStatus = "Cannot schedule"

print("\n Final Appointment Report")
print("Patient Name", patient)
print("Requested department:",requestedDepartment)
print("Available department:",list(commonDep))
print("Unavailable departments:",list(unavailDep))
print("Common department:",list(commonDep))
print("Previous Department:", list(visitDep))
print("Duplicate Requests:", dupReq)
print("Emergency:",list(emergencyDep))
print("Recommended Department:", recDep)
print("Final Status:", appStatus)