import sys,math,pickle,operator

inputfile= sys.argv[1]
testfile= sys.argv[2]

main_dict={}
map_dict={}

#try:
finame=open(inputfile,'rb')
fintest=open(testfile,'r')
foname=open("output.txt",'w')
main_dict=pickle.load(finame)
map_dict=pickle.load(finame)

for line in fintest:
  list1=line.split()
  dict1={}
  for key,value in map_dict.items():
     val=main_dict[key]['PROB']
     for i in range(1,len(list1)):
        if list1[i] in main_dict[key]['WD']:
          val+=main_dict[key]['WD'][list1[i]]
        else:
          val+=main_dict[key]['NEW']
     dict1[key]=val
  maxValue=max(dict1.items(), key=operator.itemgetter(1))[1]
  for k,v in dict1.items():
    if v==maxValue:
      foname.write(k)
      print(k)
      foname.write('\n')  
            
#except:
 #   print ("Error in reading or writing file")
#finally:
finame.close()
fintest.close()
