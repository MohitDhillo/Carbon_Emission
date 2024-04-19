import pandas as pd

def count_elements(string):
    # Remove the brackets and split the string by commas
    elements = string.strip("[]").split(", ")
    # Count the number of elements
    return len(elements)

def ordinal_encode_df(dff, order=None):
    # mapping = {}
    encoded_df = pd.DataFrame()
    
    # we will use our own order to encode 
    for col in dff.columns:
        if order and col in order:
            unique_categories = order[col]
            category_mapping = {category: idx for idx, category in enumerate(unique_categories)}
            # mapping[col] = category_mapping
            encoded_df[col] = dff[col].map(category_mapping)
        else:
            encoded_df[col] = dff[col]

            
        # category_mapping = {category: idx for idx, category in enumerate(unique_categories)}
        # mapping[col] = category_mapping
        # encoded_df[col] = dff[col].map(category_mapping)
    
    return encoded_df


def preprocess_df(df):

    df['Vehicle Type']=df['Vehicle Type'].fillna('No Vehicle')

    df['Recycling_count'] = df['Recycling'].apply(count_elements)
    df['Cook_count'] = df['Cooking_With'].apply(count_elements)

    df.drop(columns = ['Recycling', 'Cooking_With'], axis = 1 , inplace = True)

    orders = {
        'Body Type': {'overweight': 2, 'obese':3, 'underweight': 0, 'normal': 1},
    'Sex': {'female': 0, 'male': 1}, 
    'Diet': {'pescatarian': 0, 'vegetarian': 1, 'omnivore': 2, 'vegan': 3},
    'How Often Shower': {'daily': 1, 'less frequently': 0, 'more frequently': 3, 'twice a day': 2},
    'Heating Energy Source': {'coal':3, 'natural gas': 1, 'wood': 2, 'electricity': 0},
    'Transport': {'public': 1, 'walk/bicycle': 0, 'private': 2},
    'Vehicle Type': { 'No Vehicle': 0, 'petrol': 5, 'diesel': 4, 'hybrid': 3, 'lpg': 2, 'electric': 1},
    'Social Activity': {'often': 2, 'never': 0, 'sometimes': 1},
    'Frequency of Traveling by Air': {'frequently': 2, 'rarely': 1, 'never': 0, 'very frequently': 3},
    'Waste Bag Size': {'large': 2, 'extra large': 3, 'small': 0, 'medium': 1},
    'Energy efficiency': {'No': 2, 'Sometimes': 1, 'Yes': 0}
    }

    df_encoded, mapping = ordinal_encode_df(df, order=orders)
    return df_encoded


