To merge the files: mergeFiles.py
python3 mergeFiles.py /path-to-folder/ mergedFile

Learn the training set:nblearn.py
python3 nblearn.py mergedFile model

Classify the test data:nclassify.py
python3 nbclassify.py model testfile

Precision of SPAM: 0.946808
Recall of SPAM: 0.980716
F-Score of SPAM: 0.96346402

Precision of HAM: 0.992908
Recall of HAM: 0.98000
F-Score of HAM: 0.98641177

Precision of POS: 0.881175
Recall of POS: 0.758056
F-Score of POS: 0.814992

Precision of NEG: 0.787716
Recall of NEG: 0.897778
F-Score of NEG:0.839154

SVM:
 
Precision of SPAM: 0.956667
Recall of SPAM: 0.790634
F-Score of SPAM: 0.865762

Precision of HAM: 0.9285
Recall of HAM: 0.987
F-Score of HAM: 0.956859

Precision of POS: 0.955357
Recall of POS: 0.856000
F-Score of POS: 0.902954

Precision of NEG: 0.643564
Recall of NEG: 0.86667
F-Score of NEG: 0.738636

MEGAM:
I have used binary class instead of multiclass(mentioned in Piazza)

Precision of SPAM: 0.980080
Recall of SPAM: 0.984000
F-Score of SPAM: 0.982036

Precision of HAM: 0.955432
Recall of HAM: 0.944904
F-Score of HAM: 0.950139

Precision of POS: 0.936937
Recall of POS: 0.832000
F-Score of POS: 0.881356

Precision of NEG: 0.592233
Recall of NEG: 0.81333
F-Score of NEG: 0.685393

When training set is reduced to 10% of the original training set

Precision of SPAM: 0.7623
Recall of SPAM: 0.684
F-Score of SPAM: 0.7210

Precision of HAM: 0.725
Recall of HAM: 0.786
F-Score of HAM: 0.75426

Precision of POS: 0.56819
Recall of POS: 0.6135
F-Score of POS: 0.59002

Precision of NEG: 0.51264
Recall of NEG: 0.5986
F-Score of NEG: 0.55231

SVM:
 
Precision of SPAM: 0.7053
Recall of SPAM: 0.6754
F-Score of SPAM: 0.80638

Precision of HAM: 0.7234
Recall of HAM: 0.6912
F-Score of HAM: 0.87614

Precision of POS: 0.7125
Recall of POS: 0.6195
F-Score of POS: 0.7397

Precision of NEG: 0.593
Recall of NEG: 0.6123
F-Score of NEG: 0.657005

MEGAM:

Precision of SPAM: 0.7953
Recall of SPAM: 0.6951
F-Score of SPAM: 0.74183

Precision of HAM: 0.7865
Recall of HAM: 0.7312
F-Score of HAM: 0.75784

Precision of POS: 0.6951
Recall of POS: 0.6651
F-Score of POS: 0.71015

Precision of NEG: 0.5123
Recall of NEG: 0.6542
F-Score of NEG: 0.57461

The Precision,Recall and F-Score in Naive baye's classifier,SVM and Megam decreases as the training set is reduced because the number of unknown words increases in dev set as the training set is reduced and the classifier will not be able to decide whether the words belong to  SPAM and HAM.  
