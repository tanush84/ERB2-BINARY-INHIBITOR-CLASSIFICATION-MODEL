ML model for the binary prediction of ERB2 inhibitors using python script. 

*****

After installing the requirements in an Virtual Environment
or creating a new environment using conda by using "ml.yml" file
just open the command prompt or Terminal in the above created virtual environment
run the command given below

### Using Random Forest Algorithm based prediction
python predict_RF_rdkit.py test.smi

### OR 

### Using LGBMC Algorithm based prediction
python predict_LGBMC_rdkit.py test.smi


similarly, for any unknown molecule when just use the command by specifying the path
of "*.smi" file.

python predict_name_of_algorithm.py [specify_path]*.smi


The result will be displayed in the terminal as Molecule to be active or Inactive.
The supplied test.smi molecule is an inactive molecule.

Images cm-erb2-rf.png displays confusion matrix of Random forest model. Lazypredict.png indicates the lazypredict statistical parameters of various models. roc-rf.png displays the ROC curve of Random forest model. 

 
