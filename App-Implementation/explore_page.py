import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


def load_data():
    data = pd.read_csv(r'Files/Building Energy Efficiency.csv')
    return data

df = load_data()

def show_explore_page():
    st.title("Explore the Model")
    st.divider()

    st.write(
        """
    ## Exploring the dataset
    """
    )

    st.write("""The  dataset chosen for this application contains a list of 8 independent variables for each row. These variables were chosen for their high predictability of heating and cooling loads. This dataset contains a total of 768 rows and 11 columns. The sum of the two loads is its own column named 'Total Load' which our model is predicting.""")

    st.write('''#### Here is the snapshot of the entire dataset:-''')

    st.write(df.sample(frac = 1).head())

    st.write('''#### Distribution of each variable in the dataset:-''')

    st.image(r"Files/Variable Distribution.png", caption="As can be seen, the data needed to be normalised before being used in application")

    st.write("""#### Source of dataset:""")
    st.write("""Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools. / Tsanas, Athanasios; Xifara, Angeliki.
In: Energy and buildings, Vol. 49, 06.2012, p. 560-567.
""")
    st.link_button("Go to Source of Dataset", "https://www.research.ed.ac.uk/en/publications/accurate-quantitative-estimation-of-energy-performance-of-residen")
    
    st.divider()

    st.write('''## Model Selection and Performance''')

    st.write('''### Model Selection''')

    st.write('''The model chosen for this application is Gradient Boosting Regression. This model was chosen after it showed the best performance in testing both before and after hyperparameter tuning.''')

    st.write('''The model showed an cross-validation score and test score of 0.992 and 0.995 respectively''')

    st.write("#### CV-scores for the models after tuning compared:-")
    st.image(r"Files/Final Test Scores and CV Scores.png", caption="Another advantage is that this model is less prone to overfitting compared to the other tree-based models")
    st.write("")

    st.write('''### Model Performance''')
    st.write('''Now, let's visualise the performance of this model with some helpful graphs. As can be seen, this model is able to predict the heating and cooling loads of a building with a very high accuracy.''')

    st.write('''#### Difference between Prediction and Actual Value for this model:-''')
    st.image(r"Files/Predictions.png")
    st.write("")

    st.write('''Another helpful visualisation would be to calculate the relative deviation betweeen the prediction and actual value. Given below is equation for Relative Deviation used:''')
    st.latex(r'''\text{Relative Deviation (\%)} = \frac{\left| P - A \right|}{\left| A \right|} \times 100\%''')

    st.write('''#### Relative Deviation between Prediction and Actual Value:-''')
    st.image(r"Files/Relative Deviation.png", caption="Despite some outliers, the overall deviation remains close to zero.")

    st.write('''#### Feature Importance in the dataset:-''')
    st.image(r"Files/Feature Importance.png", caption="Although it might seem small, the importance of the orientation is not zero.")

    