import sys,math
import pickle

inputfile= sys.argv[1]
outputfile= sys.argv[2]
i=0
Dict={}
Dclass={}
Tot_dict={}
count=0
cnt=0
index=0
total_msg=0
vocab_size=0
extra_ct=0
total_dict={}
wcount=0
try:
    finame=open(inputfile,'r')
    foname=open(outputfile,'wb')
    for line in finame:
      total_msg += 1
      name=line.split()[0]
      if(name not in Dict): 
         Dclass[name]=index
         extra_ct += 1
         word_dir={}
         subd={'TOTAL':1,'PROB':0.0,'WD':word_dir,'NEW':0.0,'WCount':0}
         Dict[name]=subd
         index += 1
      elif(name in Dict):
         cnt=Dict[name]['TOTAL']
         cnt += 1
         Dict[name]['TOTAL']=cnt   
      list= line.lower().split()
      for i in range(len(list)):
         if(list[i] not in total_dict):
              total_dict[list[i]]=1
              
     
         if(list[i] not in Dict[name]['WD'] ):
            if(list[i] != name.lower()):
              Dict[name]['WD'][list[i]]=1
              wcount=Dict[name]['WCount']
              wcount += 1
              Dict[name]['WCount']=wcount
             
         else:
            count=Dict[name]['WD'].get(list[i])
            count += 1
            count=Dict[name]['WD'][list[i]]=count
            wcount=Dict[name]['WCount']
            wcount += 1
            Dict[name]['WCount']=wcount
             
    
    vocab_size=len(total_dict)-extra_ct
    for key,value in Dclass.items():
        cls=Dict[key]['TOTAL']
        p=math.log10(cls)-math.log10(total_msg)
        Dict[key]['PROB']=p
        wc=Dict[key]['WCount']
        for k,v in Dict[key]['WD'].items():
          val=math.log10(v+1) - math.log10(wc+vocab_size)
          Dict[key]['WD'][k]=val
        v=math.log10(1) - math.log10(wc+vocab_size)
        Dict[key]['NEW']=v 
    pickle.dump(Dict,foname)
    pickle.dump(Dclass,foname)
      
except IOError:
    print ('Error while reading from file') 
finally:
    finame.close()
    foname.close()
