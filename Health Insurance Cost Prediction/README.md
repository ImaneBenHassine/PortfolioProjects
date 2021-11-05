This is the big question of our projects : Which Factors Influence the Price of Health Insurance?

Many factors that affect how much we pay for health insurance are not within our control and that's the Impact of Medicine to our Wallet.

And today we will explore a data set dedicated to the cost of treatment of different patients xhere "Charge" is the dependent feature and here are our independent feature or factors that affect how much health insurance premiums cost :

 - age: age of primary beneficiary

 - sex: insurance contractor gender, female, male

 - bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, 
        objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9

 - children: Number of children covered by health insurance

 - smoker: Smoking

 - region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest

TABLE OF CONTENTS :
- 1- Importing Libraries
- 2- Load data
- 3- Missing Values
- 4- Duplicated Rows
- 5- EDA
- 6- Feature Engineering
- 7- Create & Train Model
- 8- Evaluating the Algorithm
- 9- Save Model using Joblib
- 10- GUI


Conclusion: like we previously noticed smoking is the greatest factor that affects medical cost charges, then it's bmi and age or localisation.
GradientBoostingRegressor turned out to be the best model and before the deployement we trained it on the entire dataset and save it using joblib. 
Finally, we create a Graphical User Interface using Tkinter package where we enter the dependent variables and it returned the predictable value of charges by pressing the button predict.
