# Interactive_Recognition_System
This project attempts to recognize facial expressions/mood of the user by evaluating his/her image from web cam against the machine learning trained model. Once the mood of the user is known some pre feeded songs, videos, etc. depending on the mood can be played.   


## Getting Started

The [eClassifier.py](https://github.com/mohitgoel188/Interactive_Recognition_System/blob/master/eClassifier.py) file is the main file which contains all relevant code.     
The [predict.py](https://github.com/mohitgoel188/Interactive_Recognition_System/blob/master/predict.py) is used to load pre-saved model to predict.   
The [imgcap.py](https://github.com/mohitgoel188/Interactive_Recognition_System/blob/master/imgcap.py) is used to capture image of the user and do necessary pre-processing before prediction can be done.  
The [playfunc.py](https://github.com/mohitgoel188/Interactive_Recognition_System/blob/master/playfunc.py) is used to play desired files based on the prediction.  

### Prerequisites

Python 3.6.x is required with following modules with their dependencies:-
* sklearn    
    -- For constructing model,training,predicting
* jupyter notebook                            
    -- For interactive feedback
* numpy                                       
    -- For numerical computation on arrays
* pandas  
    -- For loading data from .csv file and doing manipulation on it if required
* beakerx (optional)    
    -- For getting more interactive table view
* matplotlib (optional)                         
    -- For text image visualization
* os  
    -- For playing files
* cv2  
    -- For image processing
* joblib  
    -- For storing and loading ML models

### Installing

Python 3 can be found at [this link](https://www.python.org/downloads/)
All further modules can be installed by passing: `pip install module_name` in the command shell(cmd, Windows Powershell,etc.) 
