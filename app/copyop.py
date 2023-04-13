import os

# open a file
sample = open("/app/app/sample.txt","r")

# create a separate folder for each name and save the name in respective folder
for line in sample:

        first_name = line.split()[0]
        
        path=os.path.join(os.getcwd()+"/app",first_name)
        
        os.makedirs(path)
        
        try:
                name=open(path+"/"+first_name+".txt","w")
                name.write(line)
        except:
                print("Exception occured while writting the file")

# close the file
sample.close()
