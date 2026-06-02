import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# --- 1. Load Data ONCE ---
# Load the dataset at the start and store it
iris = load_iris()
target_names = iris.target_names

# Create the DataFrame from the 'iris' object
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# --- 2. Model Training ---
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species']) # Use df for training

# --- 3. Streamlit Sidebar ---
st.sidebar.title("Iris Species Prediction")
sepal_length = st.sidebar.slider("Sepal Length (cm)", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
sepal_width = st.sidebar.slider("Sepal Width (cm)", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
petal_length = st.sidebar.slider("Petal Length (cm)", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
petal_width = st.sidebar.slider("Petal Width (cm)", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))

# --- 4. Prediction ---
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_data)
predicted_species = target_names[prediction][0]

st.write(f"## Predicted Iris Species: {predicted_species}")

# --- 5. Display Information ---
# Now you can just reuse the 'iris' and 'df' variables
# No need to call load_iris() ever again!

st.write("### Input Features")
input_df = pd.DataFrame(input_data, columns=iris.feature_names)
st.write(input_df)

st.write("### Iris Dataset Sample")
st.write(df.sample(5))

st.write("### Iris Dataset Description")
st.write(iris.DESCR)

st.write("### Iris Dataset Feature Names")
st.write(iris.feature_names)

st.write("### Iris Dataset Target Names")
st.write(iris.target_names)

st.write("### Iris Dataset Data")
st.write(iris.data)

st.write("### Iris Dataset Target")
st.write(iris.target)

st.write("### Iris Dataset Frame")
# You already created this as 'df', but if you want a new one:
st.write(pd.DataFrame(iris.data, columns=iris.feature_names))

st.write("### Iris Dataset Keys")
st.write(iris.keys())

st.write("### Iris Dataset Shape")
st.write(iris.data.shape)

st.write("### Iris Dataset Type")
st.write(type(iris))