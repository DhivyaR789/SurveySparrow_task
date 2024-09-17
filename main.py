import streamlit as st

# Function to display input form and handle prediction
def show_form():
    st.title("Machine Learning Prediction Interface")

    inputs = {}
    
    st.header("Please provide the following inputs:")
    
    fields = ['geography', 'age', 'balance', 'estimatedsalary','preferredlogindevice', 'citytier', 'warehousetohome', 'gender','hourspendonapp', 'numberofdeviceregistered', 'preferedordercat',
       'satisfactionscore', 'maritalstatus', 'numberofaddress', 'complain','accountweeks', 'custservcalls', 'daymins', 'daycalls', 'monthlycharge',
       'overagefee', 'roammins']

    dataset1 = ['geography', 'age', 'balance', 'estimatedsalary'],
    dataset2 =  ['preferredlogindevice', 'citytier', 'warehousetohome', 'gender','hourspendonapp', 'numberofdeviceregistered', 'preferedordercat',
       'satisfactionscore', 'maritalstatus', 'numberofaddress', 'complain',],
    dataset3 = ['accountweeks', 'custservcalls', 'daymins', 'daycalls', 'monthlycharge',
       'overagefee', 'roammins'] 

    for i in range(1, 23):  
        field_name = fields[i-1]
        field_type = st.selectbox(f"Select type for {field_name}", ["int", "float"], key=f"type_{i}")
        if field_type == "int":
            value = st.number_input(f"Enter {field_name}", key=f"value_{i}", format="%d", step=1)
        else:
            value = st.number_input(f"Enter {field_name}", key=f"value_{i}", format="%f", step=0.01)
        inputs[field_name] = value

    if st.button("Predict"):
        st.write("Collected Inputs:")
        st.write(inputs)
        # res = model.predict(inputs)
        res = 1
        if res == 0:
            st.success("No he's not a churn")
        else:
            st.error("Yes he's a churn")


if __name__ == "__main__":
    show_form()
