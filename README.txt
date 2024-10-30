To use the single and multistage models provided here, a single Excel file is enough for each instance. 
The file should contain the following sheets:

"CD" : List of off-grid costs of all nodes in the order of node IDs without a heading

"CGI": List of grid internal costs of all nodes in the order of node IDs without a heading

"CGE": Matrix of the costs of medium/high voltage lines between the nodes in the order of node IDs for the grid option

"CMGI": List of mini-grid internal costs of all nodes in the order of node IDs without a heading (In case MVMC model or multistage MVMC model is run, it is needed.)

"CMGE": Matrix of the costs of medium/high voltage lines between the nodes in the order of node IDs for the mini-grid option (In case MVMC model or multistage MVMC model is run, it is needed.)

"Pop": List of populations of all nodes in the order of node IDs

Notes: 

You can find "21_instance.xlsx" file as the sample file.

Throughout "Mathematical Programming Models for Multistage Rural Electrification Planning: Off-Grid, Grid and Mini-Grid Options" 
study, the costs are kept fixed while the multistage models are being solved. Therefore, the Excel file includes costs for only one stage. If the user wants to use different costs for the different stages, the Python codes should be updated accordingly.



