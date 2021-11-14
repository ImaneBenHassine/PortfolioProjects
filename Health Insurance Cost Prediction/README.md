# Cost Prediction

This is the big question of our projects : Which Factors Influence the Price of Health Insurance?

Many factors that affects how much we pay for health insurance are not within our control and that's the Impact of Medicine to our Wallet.

the final result of the web app is here : https://health-cost-prediction.herokuapp.com/

### Data Source 
And today we will explore a data set dedicated to the cost of treatment of different patients where "Charge" is the dependent feature and here are our independent feature or factors that affect how much health insurance premiums cost :

 - age: age of primary beneficiary

 - sex: insurance contractor gender, female, male

 - bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, 
        objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9

 - children: Number of children covered by health insurance

 - smoker: Smoking

 - region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest
 
### Steps

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

![insurance](https://user-images.githubusercontent.com/26963240/140522884-c97e8c43-fce3-4504-bfe1-35b87c19918b.png)

The next step will be the creation of a Web App for this ML algorithm so any one can use it and make prediction of Health Insurance Cost using __Streamlit__ and __Heroku__

# Web App for ML
- using __Streamlit__ which is an open source Python library that turns data scripts into shareable web apps in minutes.
- using Anaconda Spyder as Python IDE because all the library for machine learning and data science are pre-installed
- using __Heroku__ a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

To install __Streamlit__ run in Anaconda prompt : 

          pip install streamlit
          streamlit hello # to check demo app of streamlit
![streamlit](https://user-images.githubusercontent.com/26963240/141477417-8f6753eb-1007-41c3-8286-cac94bdcea36.png)

- Create Health_Insurance.py in Spyder 

For now it contains only the html header in the main(), bu runing streamlit run Health_Insurance.py anaconda prompt, the Streamlit app in browser look like this :

![run health st](https://user-images.githubusercontent.com/26963240/141482709-3025e045-8cfa-4de4-b0ea-7651f7297dba.png)

those next lines in Health_Insurance.py will create the same shape of the GUI created with Python Tkinter package 


     """
      @author: Imane BH
     """
    import streamlit as st
    import joblib
    def main():
    
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black";text-align:center> Health Insurance Cost Prediction Using ML</h2>
    </div
 
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('model_joblib_gr')
    
    p1 = st.slider('Enter Your Age',18,100)
       
    s1 = st.selectbox('Sex',('Male','Female'))
    # for prediction it requires numerical values
    if s1=='Male':
        p2=1
    else:
        p2=0
    p3 = st.number_input("Enter Your BMI Value")
    
    p4 = st.slider("Enter Number of Children",0,4)
    
    s2 = st.selectbox("Smoker",("Yes","No"))
    
    #again with string values needs to use numerical values
    if s2=='Yes':
        p5=1
    else:
        p5=0
    
    p6 = st.slider("Enter Your Region",1,4) #or we can use this next alternative to show the label of region instead of just numbers
    s3=st.selectbox("Region",("southwest","southeast","northwest","northeast"))
    
    if s3=="southwest":
        p6=1
    elif s3=="southeast":
        p6=2
    elif s3=="northwest":
        p6=3
    elif s3=="northeast":
        p6=4
    
    # for the button predict
    if st.button('Predict'):
        pred= model.predict([[p1,p2,p3,p4,p5,p6]])
        
        st.balloons()
        st.success('Your Insurance Cost is {}http://localhost:8501/'.format(round(pred[0],2)))
if _name_== '_main_':
    main()

Now the app will run locally and be available via the URL :http://localhost:8501/

![st predict](https://user-images.githubusercontent.com/26963240/141681470-064f59a5-f241-4ae0-96a6-9820e4c9cc24.png)


But to share it, __Heroku Account__ allows deploying the prediction costs to the web.

to Setup Heroku Account, first need to register then install the __Heroku Command Line Interface (CLI)__. You use the CLI to manage and scale your applications, provision add-ons, view your application logs, and run your application locally.


- __requirements.txt__ :to create the requirement file run inside project repo

       pip install pipreqs 

- __setup.sh__ : create a txt.file and then save it as .sh it'is s streamlit folder with credentials.toml and a congif.tom file

- __Procfile__ : is used to first execute the setup.sh and then call streamlit to run the application 

           web: sh setup.sh && streamlit run Health_Insurance.py
     
Push the apllication to Heroku by using those commands 

          git init
          heroku login
          heroku create surveyresults
          git add .
          git commit -am "start app"
          git push heroku master

At this level i've got en error : ModuleNotFoundError: No module named 'sklearn' because creating the requirements.txt didn't not consider all the packages used so i had to add it manually by checking the version running 

          pip list
          
Now the app is life on the web : https://health-cost-prediction.herokuapp.com/
![st cost final](https://user-images.githubusercontent.com/26963240/141685091-df10def8-a93d-4c18-b945-a69b6c34d0c8.png)

to keep the application free set scaling dynos to 1: 

           heroku ps:scale web=1
           
### Kaffeine
As we are using the free tier of heroku it will set the application into a sleeping mode after 30 minutes of inactivity this is not a problem at all but it just takes some time whenever loading the page again ao to avoid that hiroku is falling into the sleeping mode Kaffeine ping it every 30 minutes so that the application stays awake by entering the app name here https://kaffeine.herokuapp.com/

# Conslusion 

In this project I went over the process of deploying a Streamlit app using Heroku, a platform as a service (PaaS) allowing you to run applications on the cloud. It achieves this by allowing you to create a website by only adding a few Streamlit function calls to an existing python projects where i create a machine learning algorithm to predict the Price of Health Insurance based on the influence of other factors.
